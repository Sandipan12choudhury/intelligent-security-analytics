"""
==============================================================================
Email Service

Purpose
-------
Sends OTP codes by email via SMTP (works with Gmail using an App
Password out of the box). If SMTP is not configured in .env, or the
send fails for any reason, the code is printed to the server console
instead - same fallback pattern as the SMS service.

Author
------
Sandipan Choudhury
==============================================================================
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from backend.auth_config import (

    SMTP_HOST,
    SMTP_PORT,
    SMTP_USERNAME,
    SMTP_PASSWORD,
    SMTP_FROM_EMAIL

)


class EmailService:

    def __init__(self):

        self.configured = bool(SMTP_HOST and SMTP_USERNAME and SMTP_PASSWORD)

    def send_otp(self, to_email: str, code: str, full_name: str = "") -> bool:

        greeting = f"Hi {full_name}," if full_name else "Hi,"

        body = (

            f"{greeting}\n\n"
            f"Your Intelligent Security Analytics Platform "
            f"verification code is:\n\n"
            f"    {code}\n\n"
            f"This code will expire in 5 minutes. If you did not "
            f"request this, you can safely ignore this email.\n\n"
            f"- Intelligent Security Analytics Platform"

        )

        if self.configured:

            try:

                message = MIMEMultipart()

                message["From"] = SMTP_FROM_EMAIL

                message["To"] = to_email

                message["Subject"] = (

                    "Your verification code - "
                    "Intelligent Security Analytics Platform"

                )

                message.attach(MIMEText(body, "plain"))

                with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:

                    server.starttls()

                    server.login(SMTP_USERNAME, SMTP_PASSWORD)

                    server.sendmail(

                        SMTP_USERNAME, to_email, message.as_string()

                    )

                return True

            except Exception as error:

                print(

                    f"\nEmail send failed, falling back to "
                    f"console: {error}\n"

                )

        print("\n" + "=" * 80)

        print(f"[DEV MODE - EMAIL NOT SENT] OTP for {to_email}: {code}")

        print("=" * 80 + "\n")

        return True
