"""
==============================================================================
Artifact API

Purpose
-------
REST endpoints for Enterprise AI Artifact Generation.

Author
------
Sandipan Choudhury
==============================================================================
"""

from fastapi import APIRouter, HTTPException

from backend.models.artifact_models import (
    ArtifactRequest,
    ArtifactResponse
)

from backend.services.artifact_service import ArtifactService

# =============================================================================
# Router
# =============================================================================

router = APIRouter(

    prefix="/api/v1/artifacts",

    tags=["AI Artifacts"]

)

service = ArtifactService()

# =============================================================================
# Root Cause
# =============================================================================

@router.post(

    "/generate",

    response_model=ArtifactResponse

)

def generate_artifact(request: ArtifactRequest):

    try:

        response = service.generate_artifact(

            observation_id=request.observation_id,

            artifact_type=request.artifact_type

        )

    except ValueError as error:

        raise HTTPException(

            status_code=400,

            detail=str(error)

        )

    if not response.success:

        raise HTTPException(

            status_code=500,

            detail=response.error_message

        )

    return ArtifactResponse(

        success=response.success,

        artifact_type=response.artifact_type,

        generated_text=response.generated_text,

        model=response.model,

        response_time=response.response_time,

        generated_at=str(response.generated_at)

    )