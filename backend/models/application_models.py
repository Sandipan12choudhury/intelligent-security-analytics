"""
==============================================================================
Application Models

Purpose
-------
Pydantic response models for Enterprise Applications.

Author
------
Sandipan Choudhury
==============================================================================
"""

from typing import List

from pydantic import BaseModel


class ApplicationResponse(BaseModel):

    applications: List[dict]