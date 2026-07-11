"""
==============================================================================
Applications API

Purpose
-------
Enterprise Applications APIs.

Author
------
Sandipan Choudhury
==============================================================================
"""

from fastapi import APIRouter

from backend.services.application_service import ApplicationService

router = APIRouter(

    prefix="/api/v1/applications",

    tags=["Applications"]

)

service = ApplicationService()


# ============================================================
# All Applications
# ============================================================

@router.get("/")

def applications():

    return service.get_applications()


# ============================================================
# Single Application
# ============================================================

@router.get("/{application_id}")

def application(application_id: str):

    return service.get_application(application_id)