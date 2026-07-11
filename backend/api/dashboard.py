"""
==============================================================================
Dashboard API

Purpose
-------
Enterprise Dashboard APIs.

Author
------
Sandipan Choudhury
==============================================================================
"""

from fastapi import APIRouter

from backend.services.dashboard_service import DashboardService

router = APIRouter(

    prefix="/api/v1/dashboard",

    tags=["Dashboard"]

)

service = DashboardService()


@router.get("/")

def dashboard():

    return service.get_dashboard()