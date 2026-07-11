"""
==============================================================================
Auth API

Purpose
-------
Registration, login, forgot/reset password, MFA (OTP) verification,
account settings changes (username / password / deletion), and
profile retrieval.

Author
------
Sandipan Choudhury
==============================================================================
"""

from fastapi import APIRouter, HTTPException, Depends

from backend.models.auth_models import (

    RegisterRequest,
    LoginRequest,
    VerifyOtpRequest,
    ResendOtpRequest,
    ForgotPasswordRequest,
    ResetPasswordRequest,
    RequestUsernameChangeRequest,
    RequestPasswordChangeRequest,
    RequestAccountDeletionRequest,
    ConfirmChangeRequest

)
from backend.services.auth_service import AuthService, AuthError
from backend.auth_dependency import get_current_user

router = APIRouter(

    prefix="/api/v1/auth",

    tags=["Authentication"]

)

service = AuthService()


def _raise(error: AuthError):

    raise HTTPException(status_code=error.status_code, detail=error.message)


# ============================================================
# Register / Login / Verify / Resend
# ============================================================

@router.post("/register")

def register(request: RegisterRequest):

    try:

        return service.register(

            request.full_name, request.username, request.email,
            request.phone, request.password

        )

    except AuthError as error:

        _raise(error)


@router.post("/login")

def login(request: LoginRequest):

    try:

        return service.login(request.username, request.password)

    except AuthError as error:

        _raise(error)


@router.post("/verify-otp")

def verify_otp(request: VerifyOtpRequest):

    try:

        return service.verify_otp(request.otp_session_id, request.code)

    except AuthError as error:

        _raise(error)


@router.post("/resend-otp")

def resend_otp(request: ResendOtpRequest):

    try:

        return service.resend_otp(request.otp_session_id)

    except AuthError as error:

        _raise(error)


# ============================================================
# Forgot / Reset Password
# ============================================================

@router.post("/forgot-password")

def forgot_password(request: ForgotPasswordRequest):

    try:

        return service.start_forgot_password(request.identifier)

    except AuthError as error:

        _raise(error)


@router.post("/reset-password")

def reset_password(request: ResetPasswordRequest):

    try:

        return service.reset_password(

            request.otp_session_id, request.code, request.new_password

        )

    except AuthError as error:

        _raise(error)


# ============================================================
# Profile
# ============================================================

@router.get("/me")

def me(user_id: int = Depends(get_current_user)):

    try:

        return service.get_profile(user_id)

    except AuthError as error:

        _raise(error)


# ============================================================
# Change Username
# ============================================================

@router.post("/request-username-change")

def request_username_change(

    request: RequestUsernameChangeRequest,
    user_id: int = Depends(get_current_user)

):

    try:

        return service.request_username_change(

            user_id, request.new_username

        )

    except AuthError as error:

        _raise(error)


@router.post("/confirm-username-change")

def confirm_username_change(

    request: ConfirmChangeRequest,
    user_id: int = Depends(get_current_user)

):

    try:

        return service.confirm_username_change(

            user_id, request.otp_session_id, request.code

        )

    except AuthError as error:

        _raise(error)


# ============================================================
# Change Password
# ============================================================

@router.post("/request-password-change")

def request_password_change(

    request: RequestPasswordChangeRequest,
    user_id: int = Depends(get_current_user)

):

    try:

        return service.request_password_change(

            user_id, request.current_password, request.new_password

        )

    except AuthError as error:

        _raise(error)


@router.post("/confirm-password-change")

def confirm_password_change(

    request: ConfirmChangeRequest,
    user_id: int = Depends(get_current_user)

):

    try:

        return service.confirm_password_change(

            user_id, request.otp_session_id, request.code

        )

    except AuthError as error:

        _raise(error)


# ============================================================
# Delete Account
# ============================================================

@router.post("/request-account-deletion")

def request_account_deletion(

    request: RequestAccountDeletionRequest,
    user_id: int = Depends(get_current_user)

):

    try:

        return service.request_account_deletion(

            user_id, request.current_password

        )

    except AuthError as error:

        _raise(error)


@router.post("/confirm-account-deletion")

def confirm_account_deletion(

    request: ConfirmChangeRequest,
    user_id: int = Depends(get_current_user)

):

    try:

        return service.confirm_account_deletion(

            user_id, request.otp_session_id, request.code

        )

    except AuthError as error:

        _raise(error)
