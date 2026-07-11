"""
==============================================================================
Auth Configuration

Purpose
-------
Loads authentication-related settings from .env:

    • JWT_SECRET_KEY   - signs session tokens (falls back to a fixed
                          dev key with a console warning if unset -
                          set a real one in .env before deploying)
    • TWILIO_ACCOUNT_SID / TWILIO_AUTH_TOKEN / TWILIO_PHONE_NUMBER
                        - optional. If not configured, OTP codes are
                          printed to the server console instead of
                          being sent by SMS, so the login/register
                          flow still works end-to-end during
                          development.

Author
------
Sandipan Choudhury
==============================================================================
"""

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / ".env")

# =============================================================================
# JWT
# =============================================================================

_DEV_FALLBACK_SECRET = "dev-only-secret-change-me-in-env"

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

if not JWT_SECRET_KEY:

    JWT_SECRET_KEY = _DEV_FALLBACK_SECRET

    print(

        "\nWARNING: JWT_SECRET_KEY is not set in .env - using a "
        "fixed development fallback. Add a real random "
        "JWT_SECRET_KEY to .env before deploying.\n"

    )

JWT_ALGORITHM = "HS256"

JWT_EXPIRY_HOURS = int(os.getenv("JWT_EXPIRY_HOURS", "12"))

# =============================================================================
# Twilio (optional)
# =============================================================================

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")

TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

# =============================================================================
# SMTP Email (optional)
# =============================================================================

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")

SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))

SMTP_USERNAME = os.getenv("SMTP_USERNAME")

SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

SMTP_FROM_EMAIL = os.getenv("SMTP_FROM_EMAIL") or SMTP_USERNAME

# =============================================================================
# Brevo (HTTP email API - works even on hosts that block SMTP ports,
# e.g. Render's free tier blocks 25/465/587 outbound). Preferred over
# raw SMTP whenever configured.
# =============================================================================

BREVO_API_KEY = os.getenv("BREVO_API_KEY")

BREVO_SENDER_EMAIL = os.getenv("BREVO_SENDER_EMAIL") or SMTP_FROM_EMAIL

BREVO_SENDER_NAME = os.getenv(

    "BREVO_SENDER_NAME", "Intelligent Security Analytics Platform"

)

# =============================================================================
# OTP
# =============================================================================

OTP_LENGTH = 6

OTP_EXPIRY_MINUTES = 5

OTP_MAX_ATTEMPTS = 5
