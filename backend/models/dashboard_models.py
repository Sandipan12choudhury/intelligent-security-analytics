"""
==============================================================================
Dashboard Models

Purpose
-------
Request/Response models for Dashboard APIs.

Author
------
Sandipan Choudhury
==============================================================================
"""

from pydantic import BaseModel


class DashboardResponse(BaseModel):

    enterprise: dict

    applications: list

    departments: list

    activities: list