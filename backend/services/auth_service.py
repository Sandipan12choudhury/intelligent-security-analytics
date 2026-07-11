"""
==============================================================================
Auth Service

Purpose
-------
Registration, login, forgot/reset password, account-settings changes
(username, password, deletion), and OTP verification (MFA) - every
one of these sends a code to BOTH the user's phone (SMS) and email
at once, and every one of them requires that code before completing.

Flow
----
Register:          create account (unverified) -> OTP -> verified -> JWT
Login:              verify password -> OTP -> JWT
Forgot Password:    look up account -> OTP -> submit new password + code
Change Username:    (logged in) submit new username -> OTP -> confirm
Change Password:    (logged in) verify current password -> OTP -> confirm
Delete Account:     (logged in) verify current password -> OTP -> confirm

Author
------
Sandipan Choudhury
==============================================================================
"""

import random
import string
import uuid
from datetime import datetime, timedelta, timezone

import bcrypt
import jwt

from backend.database import database
from backend.auth_config import (

    JWT_SECRET_KEY,
    JWT_ALGORITHM,
    JWT_EXPIRY_HOURS,
    OTP_LENGTH,
    OTP_EXPIRY_MINUTES,
    OTP_MAX_ATTEMPTS

)
from backend.services.sms_service import SmsService
from backend.services.email_service import EmailService
from backend.logging_config import auth_logger


class AuthError(Exception):

    def __init__(self, message, status_code=400):

        self.message = message

        self.status_code = status_code

        super().__init__(message)


def _hash(value: str) -> str:

    return bcrypt.hashpw(value.encode(), bcrypt.gensalt()).decode()


def _check(value: str, hashed: str) -> bool:

    try:

        return bcrypt.checkpw(value.encode(), hashed.encode())

    except ValueError:

        return False


def _generate_otp() -> str:

    return "".join(random.choices(string.digits, k=OTP_LENGTH))


def _mask_phone(phone: str) -> str:

    if len(phone) <= 4:

        return phone

    return ("*" * (len(phone) - 4)) + phone[-4:]


def _mask_email(email: str) -> str:

    if "@" not in email:

        return email

    local, domain = email.split("@", 1)

    if len(local) <= 2:

        masked_local = local[0] + "*" * max(len(local) - 1, 0)

    else:

        masked_local = local[:2] + "*" * (len(local) - 2)

    return f"{masked_local}@{domain}"


class AuthService:

    def __init__(self):

        self.sms_service = SmsService()

        self.email_service = EmailService()

    # ============================================================
    # Registration
    # ============================================================

    def register(self, full_name, username, email, phone, password):

        connection = database.get_connection()

        try:

            existing = connection.execute(

                "SELECT id FROM users WHERE username = ? OR email = ? "
                "OR phone = ?",

                (username, email, phone)

            ).fetchone()

            if existing:

                raise AuthError(

                    "An account with this username, email, or phone "
                    "number already exists.",

                    409

                )

            password_hash = _hash(password)

            created_at = datetime.now().isoformat()

            cursor = connection.execute(

                """
                INSERT INTO users
                    (full_name, username, email, phone,
                     password_hash, is_verified, created_at)
                VALUES (?, ?, ?, ?, ?, 0, ?)
                """,

                (full_name, username, email, phone, password_hash, created_at)

            )

            connection.commit()

            user_id = cursor.lastrowid

            auth_logger.info(

                "New account registered",

                extra={"extra_data": {

                    "user_id": user_id,

                    "username": username

                }}

            )

            return self._start_otp_session(

                connection, user_id, phone, "register",

                email=email, full_name=full_name

            )

        finally:

            connection.close()

    # ============================================================
    # Login
    # ============================================================

    def login(self, username, password):

        connection = database.get_connection()

        try:

            user = connection.execute(

                "SELECT * FROM users WHERE username = ?", (username,)

            ).fetchone()

            if not user or not _check(password, user["password_hash"]):

                auth_logger.warning(

                    "Failed login attempt",

                    extra={"extra_data": {"username": username}}

                )

                raise AuthError("Invalid username or password.", 401)

            auth_logger.info(

                "Password verified, OTP challenge sent",

                extra={"extra_data": {

                    "user_id": user["id"],

                    "username": username

                }}

            )

            return self._start_otp_session(

                connection, user["id"], user["phone"], "login",

                email=user["email"], full_name=user["full_name"]

            )

        finally:

            connection.close()

    # ============================================================
    # Forgot Password
    # ============================================================

    def start_forgot_password(self, identifier):

        connection = database.get_connection()

        try:

            user = connection.execute(

                "SELECT * FROM users WHERE username = ? OR email = ?",

                (identifier, identifier)

            ).fetchone()

            if not user:

                raise AuthError(

                    "No account found with that username or email.",

                    404

                )

            return self._start_otp_session(

                connection, user["id"], user["phone"], "forgot_password",

                email=user["email"], full_name=user["full_name"]

            )

        finally:

            connection.close()

    def reset_password(self, otp_session_id, code, new_password):

        connection = database.get_connection()

        try:

            session = self._check_and_consume_otp(

                connection, otp_session_id, code, "forgot_password"

            )

            new_hash = _hash(new_password)

            connection.execute(

                "UPDATE users SET password_hash = ? WHERE id = ?",

                (new_hash, session["user_id"])

            )

            connection.commit()

            auth_logger.info(

                "Password reset via forgot-password flow",

                extra={"extra_data": {"user_id": session["user_id"]}}

            )

            return {"success": True}

        finally:

            connection.close()

    # ============================================================
    # Change Username (must be logged in)
    # ============================================================

    def request_username_change(self, user_id, new_username):

        connection = database.get_connection()

        try:

            user = self._get_user_or_raise(connection, user_id)

            if new_username == user["username"]:

                raise AuthError(

                    "That is already your current username.", 400

                )

            existing = connection.execute(

                "SELECT id FROM users WHERE username = ? AND id != ?",

                (new_username, user_id)

            ).fetchone()

            if existing:

                raise AuthError("That username is already taken.", 409)

            return self._start_otp_session(

                connection, user_id, user["phone"], "change_username",

                email=user["email"], full_name=user["full_name"],

                pending_value=new_username

            )

        finally:

            connection.close()

    def confirm_username_change(self, user_id, otp_session_id, code):

        connection = database.get_connection()

        try:

            session = self._check_and_consume_otp(

                connection, otp_session_id, code, "change_username",

                expected_user_id=user_id

            )

            new_username = session["pending_value"]

            connection.execute(

                "UPDATE users SET username = ? WHERE id = ?",

                (new_username, user_id)

            )

            connection.commit()

            auth_logger.info(

                "Username changed",

                extra={"extra_data": {

                    "user_id": user_id,

                    "new_username": new_username

                }}

            )

            return self.get_profile(user_id)

        finally:

            connection.close()

    # ============================================================
    # Change Password (must be logged in)
    # ============================================================

    def request_password_change(self, user_id, current_password, new_password):

        connection = database.get_connection()

        try:

            user = self._get_user_or_raise(connection, user_id)

            if not _check(current_password, user["password_hash"]):

                raise AuthError("Your current password is incorrect.", 401)

            if len(new_password) < 8:

                raise AuthError(

                    "New password must be at least 8 characters long.",

                    400

                )

            new_hash = _hash(new_password)

            return self._start_otp_session(

                connection, user_id, user["phone"], "change_password",

                email=user["email"], full_name=user["full_name"],

                pending_value=new_hash

            )

        finally:

            connection.close()

    def confirm_password_change(self, user_id, otp_session_id, code):

        connection = database.get_connection()

        try:

            session = self._check_and_consume_otp(

                connection, otp_session_id, code, "change_password",

                expected_user_id=user_id

            )

            new_hash = session["pending_value"]

            connection.execute(

                "UPDATE users SET password_hash = ? WHERE id = ?",

                (new_hash, user_id)

            )

            connection.commit()

            auth_logger.info(

                "Password changed",

                extra={"extra_data": {"user_id": user_id}}

            )

            return {"success": True}

        finally:

            connection.close()

    # ============================================================
    # Delete Account (must be logged in)
    # ============================================================

    def request_account_deletion(self, user_id, current_password):

        connection = database.get_connection()

        try:

            user = self._get_user_or_raise(connection, user_id)

            if not _check(current_password, user["password_hash"]):

                raise AuthError("Your current password is incorrect.", 401)

            return self._start_otp_session(

                connection, user_id, user["phone"], "delete_account",

                email=user["email"], full_name=user["full_name"]

            )

        finally:

            connection.close()

    def confirm_account_deletion(self, user_id, otp_session_id, code):

        connection = database.get_connection()

        try:

            self._check_and_consume_otp(

                connection, otp_session_id, code, "delete_account",

                expected_user_id=user_id

            )

            auth_logger.warning(

                "Account deleted",

                extra={"extra_data": {"user_id": user_id}}

            )

            connection.execute(

                "DELETE FROM otp_sessions WHERE user_id = ?", (user_id,)

            )

            connection.execute(

                "DELETE FROM users WHERE id = ?", (user_id,)

            )

            connection.commit()

            return {"success": True}

        finally:

            connection.close()

    # ============================================================
    # Shared OTP bootstrap (sends to BOTH phone and email)
    # ============================================================

    def _start_otp_session(

        self, connection, user_id, phone, purpose,

        email=None, full_name=None, pending_value=None

    ):

        code = _generate_otp()

        session_id = str(uuid.uuid4())

        expires_at = (

            datetime.now() + timedelta(minutes=OTP_EXPIRY_MINUTES)

        ).isoformat()

        connection.execute(

            """
            INSERT INTO otp_sessions
                (id, user_id, purpose, otp_code_hash, attempts,
                 expires_at, verified, pending_value, created_at)
            VALUES (?, ?, ?, ?, 0, ?, 0, ?, ?)
            """,

            (

                session_id, user_id, purpose, _hash(code),
                expires_at, pending_value, datetime.now().isoformat()

            )

        )

        connection.commit()

        self.sms_service.send_otp(phone, code)

        if email:

            self.email_service.send_otp(email, code, full_name or "")

        return {

            "otp_session_id": session_id,

            "masked_phone": _mask_phone(phone),

            "masked_email": _mask_email(email) if email else None,

            "expires_in_seconds": OTP_EXPIRY_MINUTES * 60

        }

    # ============================================================
    # Shared OTP validation
    # ============================================================

    def _check_and_consume_otp(

        self, connection, otp_session_id, code,
        expected_purpose, expected_user_id=None

    ):

        session = connection.execute(

            "SELECT * FROM otp_sessions WHERE id = ?", (otp_session_id,)

        ).fetchone()

        if not session:

            raise AuthError("Invalid or expired verification session.", 400)

        if session["purpose"] != expected_purpose:

            raise AuthError("Invalid verification session.", 400)

        if expected_user_id is not None and session["user_id"] != expected_user_id:

            raise AuthError("Invalid verification session.", 403)

        if session["verified"]:

            raise AuthError(

                "This verification session has already been used.", 400

            )

        if datetime.fromisoformat(session["expires_at"]) < datetime.now():

            raise AuthError(

                "Verification code has expired. Please request a "
                "new one.",

                400

            )

        if session["attempts"] >= OTP_MAX_ATTEMPTS:

            raise AuthError(

                "Too many incorrect attempts. Please request a new "
                "code.",

                429

            )

        if not _check(code, session["otp_code_hash"]):

            connection.execute(

                "UPDATE otp_sessions SET attempts = attempts + 1 "
                "WHERE id = ?",

                (otp_session_id,)

            )

            connection.commit()

            raise AuthError("Incorrect verification code.", 400)

        connection.execute(

            "UPDATE otp_sessions SET verified = 1 WHERE id = ?",
            (otp_session_id,)

        )

        connection.commit()

        return session

    # ============================================================
    # Verify OTP -> issue JWT (Register / Login only)
    # ============================================================

    def verify_otp(self, otp_session_id, code):

        connection = database.get_connection()

        try:

            session = connection.execute(

                "SELECT * FROM otp_sessions WHERE id = ?",
                (otp_session_id,)

            ).fetchone()

            if not session or session["purpose"] not in ("register", "login"):

                raise AuthError(

                    "Invalid or expired verification session.", 400

                )

            session = self._check_and_consume_otp(

                connection, otp_session_id, code, session["purpose"]

            )

            user = connection.execute(

                "SELECT * FROM users WHERE id = ?",
                (session["user_id"],)

            ).fetchone()

            if session["purpose"] == "register" and not user["is_verified"]:

                connection.execute(

                    "UPDATE users SET is_verified = 1 WHERE id = ?",
                    (user["id"],)

                )

                connection.commit()

            connection.execute(

                "UPDATE users SET last_login = ? WHERE id = ?",

                (datetime.now().isoformat(), user["id"])

            )

            connection.commit()

            auth_logger.info(

                f"{session['purpose'].capitalize()} completed - OTP verified",

                extra={"extra_data": {

                    "user_id": user["id"],

                    "username": user["username"],

                    "purpose": session["purpose"]

                }}

            )

            token = self._issue_token(user["id"])

            return {

                "token": token,

                "user": self._serialize_user(dict(user))

            }

        finally:

            connection.close()

    # ============================================================
    # Resend OTP (works for any purpose)
    # ============================================================

    def resend_otp(self, otp_session_id):

        connection = database.get_connection()

        try:

            session = connection.execute(

                "SELECT * FROM otp_sessions WHERE id = ?",
                (otp_session_id,)

            ).fetchone()

            if not session:

                raise AuthError("Invalid verification session.", 400)

            if session["verified"]:

                raise AuthError(

                    "This session has already been verified.", 400

                )

            user = connection.execute(

                "SELECT * FROM users WHERE id = ?",
                (session["user_id"],)

            ).fetchone()

            code = _generate_otp()

            expires_at = (

                datetime.now() + timedelta(minutes=OTP_EXPIRY_MINUTES)

            ).isoformat()

            connection.execute(

                "UPDATE otp_sessions SET otp_code_hash = ?, "
                "attempts = 0, expires_at = ? WHERE id = ?",

                (_hash(code), expires_at, otp_session_id)

            )

            connection.commit()

            self.sms_service.send_otp(user["phone"], code)

            self.email_service.send_otp(

                user["email"], code, user["full_name"]

            )

            return {"expires_in_seconds": OTP_EXPIRY_MINUTES * 60}

        finally:

            connection.close()

    # ============================================================
    # JWT
    # ============================================================

    def _issue_token(self, user_id):

        payload = {

            "user_id": user_id,

            "exp": datetime.now(timezone.utc) + timedelta(

                hours=JWT_EXPIRY_HOURS

            )

        }

        return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    def decode_token(self, token):

        try:

            payload = jwt.decode(

                token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM]

            )

            return payload["user_id"]

        except jwt.ExpiredSignatureError:

            raise AuthError("Session expired. Please log in again.", 401)

        except jwt.InvalidTokenError:

            raise AuthError("Invalid session. Please log in again.", 401)

    # ============================================================
    # Profile / helpers
    # ============================================================

    def get_profile(self, user_id):

        connection = database.get_connection()

        try:

            user = self._get_user_or_raise(connection, user_id)

            return self._serialize_user(dict(user))

        finally:

            connection.close()

    def _get_user_or_raise(self, connection, user_id):

        user = connection.execute(

            "SELECT * FROM users WHERE id = ?", (user_id,)

        ).fetchone()

        if not user:

            raise AuthError("User not found.", 404)

        return user

    def _serialize_user(self, user: dict):

        return {

            "id": user["id"],

            "full_name": user["full_name"],

            "username": user["username"],

            "email": user["email"],

            "phone": user["phone"],

            "member_since": user["created_at"],

            "last_login": user["last_login"],

            "is_verified": bool(user["is_verified"])

        }
