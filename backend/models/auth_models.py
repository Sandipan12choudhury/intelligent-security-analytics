"""
==============================================================================
Auth Models

Purpose
-------
Pydantic request models used by the Auth API.

Author
------
Sandipan Choudhury
==============================================================================
"""

from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):

    full_name: str = Field(min_length=2, max_length=100)

    username: str = Field(min_length=3, max_length=30)

    email: EmailStr

    phone: str = Field(min_length=10, max_length=15)

    password: str = Field(min_length=8, max_length=100)


class LoginRequest(BaseModel):

    username: str

    password: str


class VerifyOtpRequest(BaseModel):

    otp_session_id: str

    code: str = Field(min_length=6, max_length=6)


class ResendOtpRequest(BaseModel):

    otp_session_id: str


class ForgotPasswordRequest(BaseModel):

    identifier: str


class ResetPasswordRequest(BaseModel):

    otp_session_id: str

    code: str = Field(min_length=6, max_length=6)

    new_password: str = Field(min_length=8, max_length=100)


class RequestUsernameChangeRequest(BaseModel):

    new_username: str = Field(min_length=3, max_length=30)


class RequestPasswordChangeRequest(BaseModel):

    current_password: str

    new_password: str = Field(min_length=8, max_length=100)


class RequestAccountDeletionRequest(BaseModel):

    current_password: str


class ConfirmChangeRequest(BaseModel):

    otp_session_id: str

    code: str = Field(min_length=6, max_length=6)
