"""
==============================================================================
Email Service

Purpose
-------
Sends OTP codes by email, in this priority order:

    1. Brevo (HTTP API, port 443) - if BREVO_API_KEY is configured.
       Works everywhere, including hosts that block outbound SMTP
       ports (e.g. Render's free tier blocks 25/465/587).

    2. Direct SMTP (Gmail-ready) - if SMTP_USERNAME/PASSWORD are
       configured. Works for local development, but will fail on
       hosts that block SMTP ports.

    3. Console fallback - if neither is configured, or if sending
       fails for any reason, the code is printed to the server
       console so the register/login flow keeps working end-to-end.

Author
------
Sandipan Choudhury
==============================================================================
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

from backend.auth_config import (

    SMTP_HOST,
    SMTP_PORT,
    SMTP_USERNAME,
    SMTP_PASSWORD,
    SMTP_FROM_EMAIL,
    BREVO_API_KEY,
    BREVO_SENDER_EMAIL,
    BREVO_SENDER_NAME

)

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"


class EmailService:

    def __init__(self):

        self.brevo_configured = bool(BREVO_API_KEY and BREVO_SENDER_EMAIL)

        self.smtp_configured = bool(SMTP_HOST and SMTP_USERNAME and SMTP_PASSWORD)

    def send_otp(self, to_email: str, code: str, full_name: str = "") -> bool:

        greeting = f"Hi {full_name}," if full_name else "Hi,"

        subject = "Your verification code - Intelligent Security Analytics Platform"

        body = (

            f"{greeting}\n\n"
            f"Your Intelligent Security Analytics Platform "
            f"verification code is:\n\n"
            f"    {code}\n\n"
            f"This code will expire in 5 minutes. If you did not "
            f"request this, you can safely ignore this email.\n\n"
            f"- Intelligent Security Analytics Platform"

        )

        if self.brevo_configured:

            if self._send_via_brevo(to_email, subject, body):

                return True

        if self.smtp_configured:

            if self._send_via_smtp(to_email, subject, body):

                return True

        print("\n" + "=" * 80)

        print(f"[DEV MODE - EMAIL NOT SENT] OTP for {to_email}: {code}")

        print("=" * 80 + "\n")

        return True

    def _send_via_brevo(self, to_email: str, subject: str, body: str) -> bool:

        try:

            response = requests.post(

                BREVO_API_URL,

                headers={

                    "accept": "application/json",

                    "api-key": BREVO_API_KEY,

                    "content-type": "application/json"

                },

                json={

                    "sender": {

                        "email": BREVO_SENDER_EMAIL,

                        "name": BREVO_SENDER_NAME

                    },

                    "to": [{"email": to_email}],

                    "subject": subject,

                    "textContent": body

                },

                timeout=10

            )

            if response.status_code in (200, 201):

                return True

            print(

                f"\nBrevo send failed ({response.status_code}): "
                f"{response.text}\n"

            )

            return False

        except Exception as error:

            print(f"\nBrevo send failed, falling back: {error}\n")

            return False

    def _send_via_smtp(self, to_email: str, subject: str, body: str) -> bool:

        try:

            message = MIMEMultipart()

            message["From"] = SMTP_FROM_EMAIL

            message["To"] = to_email

            message["Subject"] = subject

            message.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as server:

                server.starttls()

                server.login(SMTP_USERNAME, SMTP_PASSWORD)

                server.sendmail(

                    SMTP_USERNAME, to_email, message.as_string()

                )

            return True

        except Exception as error:

            print(

                f"\nSMTP send failed, falling back: {error}\n"

            )

            return False
