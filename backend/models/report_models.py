"""
==============================================================================
Report Models

Purpose
-------
Pydantic request/response models used by the Reports API.

Author
------
Sandipan Choudhury
==============================================================================
"""

from typing import Optional

from pydantic import BaseModel


class GenerateReportRequest(BaseModel):

    # "application" | "department" | "enterprise"

    report_type: str

    # Application ID (for "application") or Department name
    # (for "department"). Not required for "enterprise".

    scope: Optional[str] = None
