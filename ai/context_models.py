"""
==============================================================================
AI Context Models

Purpose
-------
Defines the standard context models used throughout the AI Intelligence Layer.

These models act as the data contract between:

    • Context Engine
    • Prompt Builder
    • LLM Service
    • Artifact Generator
    • FastAPI APIs

This file is considered a core architectural component and should remain
stable once finalized.

Author
------
Sandipan Choudhury

==============================================================================
"""

from dataclasses import dataclass
from typing import Optional


# =============================================================================
# Identity Context
# =============================================================================

@dataclass
class IdentityContext:

    observation_id: str

    observation: str

    activity: str

    domain: str

    severity: str


# =============================================================================
# Application Context
# =============================================================================

@dataclass
class ApplicationContext:

    application_id: str

    application_name: str

    department: str

    business_domain: str

    business_criticality: str

    application_type: str

    environment: str

    status: str


# =============================================================================
# Knowledge Context
# =============================================================================

@dataclass
class KnowledgeContext:

    control_objective: str

    security_principle: str

    reference_standard: str

    keywords: str

    prompt_context: str


# =============================================================================
# Analytics Context
# =============================================================================

@dataclass
class AnalyticsContext:

    application_risk_score: float

    department_risk_score: float

    activity_risk_score: float

    enterprise_risk_score: float

    application_compliance: float

    department_compliance: float

    enterprise_compliance: float

    application_rank: int

    department_rank: int

    activity_rank: int

    enterprise_rank: int

    risk_category: str


# =============================================================================
# Executive Context
# =============================================================================

@dataclass
class ExecutiveContext:

    executive_priority: str

    dominant_severity: str

    top_activity: str

    top_risk_application_id: str

    top_risk_application_name: str

    highest_risk_department: str


# =============================================================================
# Request Context
# =============================================================================

@dataclass
class RequestContext:

    artifact_type: str

    user_prompt: Optional[str] = None

    regenerate: bool = False

    response_version: int = 1


# =============================================================================
# Root AI Context
# =============================================================================

@dataclass
class AIContext:

    identity: IdentityContext

    application: ApplicationContext

    knowledge: KnowledgeContext

    analytics: AnalyticsContext

    executive: ExecutiveContext

    request: RequestContext

if __name__ == "__main__":

    print("=" * 80)
    print("AI Context Models")
    print("=" * 80)

    print("IdentityContext            ✓")
    print("ApplicationContext         ✓")
    print("KnowledgeContext          ✓")
    print("AnalyticsContext          ✓")
    print("ExecutiveContext          ✓")
    print("RequestContext            ✓")
    print("AIContext                 ✓")

    print()
    print("All AI Context Models loaded successfully.")