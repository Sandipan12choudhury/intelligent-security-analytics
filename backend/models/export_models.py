"""
==============================================================================
Export Models

Purpose
-------
Pydantic request models used by the Export API.

The frontend sends the observation's identity fields together with
whichever AI artifacts have already been generated for it
(Root Cause, Business Impact, Recommendation, etc). The backend does
not regenerate anything here - it only formats what already exists
into a downloadable file.

Author
------
Sandipan Choudhury
==============================================================================
"""

from typing import Dict, Optional

from pydantic import BaseModel


class ExportRequest(BaseModel):

    observation_id: str

    observation: str

    severity: Optional[str] = None

    domain: Optional[str] = None

    activity: Optional[str] = None

    application_name: Optional[str] = None

    department: Optional[str] = None

    # Maps artifact_type (e.g. "ROOT_CAUSE") -> generated text

    artifacts: Dict[str, str] = {}
