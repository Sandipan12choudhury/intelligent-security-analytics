"""
==============================================================================
Artifact Service

Purpose
-------
Business logic layer for AI artifact generation.

Responsibilities
----------------
• Receive requests from API layer
• Invoke Artifact Generator
• Return AI responses

Future Responsibilities
-----------------------
• Authentication
• Authorization
• Audit Logging
• Database Storage
• Caching
• Rate Limiting

Author
------
Sandipan Choudhury
==============================================================================
"""

from ai.artifact_generator import ArtifactGenerator
from ai.llm_service import AIResponse


# =============================================================================
# Artifact Service
# =============================================================================

class ArtifactService:

    """
    Service layer for enterprise AI artifact generation.
    """

    def __init__(self):

        self.generator = ArtifactGenerator()

    # =========================================================================
    # Generic Artifact Generation
    # =========================================================================

    def generate_artifact(

        self,

        observation_id: str,

        artifact_type: str

    ) -> AIResponse:

        artifact_type = artifact_type.upper()

        if artifact_type == "ROOT_CAUSE":

            return self.generator.generate_root_cause(
                observation_id
            )

        elif artifact_type == "RECOMMENDATION":

            return self.generator.generate_recommendation(
                observation_id
            )

        elif artifact_type == "BUSINESS_IMPACT":

            return self.generator.generate_business_impact(
                observation_id
            )

        elif artifact_type == "EXECUTIVE_SUMMARY":

            return self.generator.generate_executive_summary(
                observation_id
            )

        elif artifact_type == "RISK_JUSTIFICATION":

            return self.generator.generate_risk_justification(
                observation_id
            )

        elif artifact_type == "PREVENTIVE_CONTROL":

            return self.generator.generate_preventive_controls(
                observation_id
            )

        raise ValueError(

            f"Unsupported artifact type: {artifact_type}"

        )