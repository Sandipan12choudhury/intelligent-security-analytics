"""
==============================================================================
Observations API

Purpose
-------
Enterprise Observations APIs - list, retrieve, form metadata, and
create new user-generated observations.

Author
------
Sandipan Choudhury
==============================================================================
"""

from fastapi import APIRouter

from backend.models.observation_models import (
    CreateObservationRequest,
    DeleteObservationsRequest
)
from backend.services.observation_service import ObservationService

router = APIRouter(

    prefix="/api/v1/observations",

    tags=["Observations"]

)

service = ObservationService()


# ============================================================
# All Observations
# ============================================================

@router.get("/")

def observations():

    return service.get_observations()


# ============================================================
# Metadata for the "Add Observation" form
# ============================================================

@router.get("/meta")

def observation_meta():

    return service.get_meta()


# ============================================================
# Recent user-generated observations (Dashboard widget)
# ============================================================

@router.get("/recent")

def recent_observations():

    return {

        "recent_observations": service.get_recent_observations()

    }


# ============================================================
# Create a new user-generated observation
# ============================================================

@router.post("/")

def create_observation(request: CreateObservationRequest):

    return service.create_observation(request)


# ============================================================
# Delete Observations (bulk)
# ============================================================

@router.post("/delete")

def delete_observations(request: DeleteObservationsRequest):

    return service.delete_observations(request.observation_ids)


# ============================================================
# Single Observation
# ============================================================

@router.get("/{observation_id}")

def observation(observation_id: str):

    return service.get_observation(observation_id)
