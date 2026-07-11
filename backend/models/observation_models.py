"""
==============================================================================
Observation Models

Purpose
-------
Pydantic response models for Enterprise Observations.

Author
------
Sandipan Choudhury
==============================================================================
"""

from typing import List, Optional

from pydantic import BaseModel


class ObservationResponse(BaseModel):

    observations: List[dict]


class ObservationDetailResponse(BaseModel):

    success: bool

    observation: Optional[dict] = None

    message: Optional[str] = None


class ObservationMetaResponse(BaseModel):

    departments: List[str]

    applications: List[dict]

    activities: List[str]

    domains: List[dict]


class CreateObservationRequest(BaseModel):

    department: str

    application_name: str

    activity: str

    domain: str

    observation: str

    severity: str


class CreateObservationResponse(BaseModel):

    success: bool

    observation_id: Optional[str] = None

    observation: Optional[dict] = None

    message: Optional[str] = None


class DeleteObservationsRequest(BaseModel):

    observation_ids: List[str]
