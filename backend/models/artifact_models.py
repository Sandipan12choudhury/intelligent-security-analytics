"""
==============================================================================
Artifact API Models

Purpose
-------
Pydantic request/response models used by Artifact APIs.

Author
------
Sandipan Choudhury
==============================================================================
"""

from pydantic import BaseModel


# =============================================================================
# Request Model
# =============================================================================

class ArtifactRequest(BaseModel):

    observation_id: str
    artifact_type: str


# =============================================================================
# Response Model
# =============================================================================

class ArtifactResponse(BaseModel):

    success: bool

    artifact_type: str

    generated_text: str

    model: str

    response_time: float

    generated_at: str