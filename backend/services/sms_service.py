"""
==============================================================================
SMS Service

Purpose
-------
Sends OTP codes by SMS via Twilio. If Twilio credentials are not
configured in .env (or the send fails for any reason), the code is
printed to the server console instead - so the register/login flow
keeps working end-to-end during development without a live Twilio
account.

Author
------
Sandipan Choudhury
==============================================================================
"""

from backend.auth_config import (

    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER

)


class SmsService:

    def __init__(self):

        self.configured = bool(

            TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN and TWILIO_PHONE_NUMBER

        )

        self.client = None

        if self.configured:

            try:

                from twilio.rest import Client

                self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

            except Exception as error:

                print(f"\nTwilio client failed to initialize: {error}\n")

                self.configured = False

    def send_otp(self, phone: str, code: str) -> bool:

        message = (

            f"Your Intelligent Security Analytics Platform "
            f"verification code is {code}. It expires in 5 minutes."

        )

        if self.configured:

            try:

                self.client.messages.create(

                    body=message,

                    from_=TWILIO_PHONE_NUMBER,

                    to=phone

                )

                return True

            except Exception as error:

                print(

                    f"\nTwilio SMS send failed, falling back to "
                    f"console: {error}\n"

                )

        print("\n" + "=" * 80)

        print(f"[DEV MODE - SMS NOT SENT] OTP for {phone}: {code}")

        print("=" * 80 + "\n")

        return True
