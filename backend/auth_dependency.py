"""
==============================================================================
Auth Dependency

Purpose
-------
Reusable FastAPI dependency that reads the "Authorization: Bearer
<token>" header, validates it, and returns the authenticated user's
id - for use on any route that should require login.

Author
------
Sandipan Choudhury
==============================================================================
"""

from fastapi import Header, HTTPException

from backend.services.auth_service import AuthService, AuthError

_auth_service = AuthService()


def get_current_user(authorization: str = Header(None)) -> int:

    if not authorization or not authorization.startswith("Bearer "):

        raise HTTPException(

            status_code=401,

            detail="Not authenticated."

        )

    token = authorization.split(" ", 1)[1]

    try:

        return _auth_service.decode_token(token)

    except AuthError as error:

        raise HTTPException(

            status_code=error.status_code,

            detail=error.message

        )
