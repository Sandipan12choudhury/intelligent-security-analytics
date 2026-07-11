"""
==============================================================================
Artifact Generator

Purpose
-------
Acts as the orchestration layer for enterprise AI artifact generation.

Responsibilities
----------------
• Build enterprise AI context
• Generate enterprise prompt
• Invoke the LLM service
• Return structured AI responses

This module is the single entry point for AI generation.

It does NOT:

    • Read Excel datasets directly
    • Perform analytics
    • Connect directly to Gemini
    • Store generated responses

Author
------
Sandipan Choudhury

==============================================================================
"""

from .context_engine import build_context
from .ai_prompt_builder import build_prompt
from .llm_service import LLMService, AIResponse

# =============================================================================
# Artifact Generator
# =============================================================================

class ArtifactGenerator:

    """
    Orchestrates the complete AI generation pipeline.
    """

    def __init__(self):

        self.llm_service = LLMService()

    def generate_artifact(

        self,

        observation_id: str,

        artifact_type: str,

        user_prompt: str | None = None

    ) -> AIResponse:

        """
        Executes the complete AI generation workflow.
        """
        artifact_prompts = {
            "ROOT_CAUSE":
            "Generate a professional technical root cause.",

            "RECOMMENDATION":
            "Generate professional remediation recommendations.",

            "BUSINESS_IMPACT":
            "Generate a professional business impact analysis.",

            "EXECUTIVE_SUMMARY":
            "Generate an executive-level security summary.",

            "RISK_JUSTIFICATION":
            "Justify the assigned security risk.",

            "PREVENTIVE_CONTROL":
            "Generate preventive security controls."
        }

        if user_prompt is None:
            user_prompt = artifact_prompts.get(
                artifact_type,
                "Generate a professional cybersecurity artifact."
            )
        
        context = build_context(

            observation_id=observation_id,

            artifact_type=artifact_type,

            user_prompt=user_prompt

        )

        prompt = build_prompt(context)

        response = self.llm_service.generate_response(

            prompt=prompt,

            artifact_type=artifact_type

        )

        return response

    # =============================================================================
    # Convenience Methods
    # =============================================================================

    def generate_root_cause(
        self,
        observation_id: str
    ) -> AIResponse:

        return self.generate_artifact(

            observation_id=observation_id,

            artifact_type="ROOT_CAUSE",

            

        )
        

    def generate_recommendation(
        self,
        observation_id: str
    ) -> AIResponse:

        return self.generate_artifact(

            observation_id=observation_id,

            artifact_type="RECOMMENDATION",

            

        )

    def generate_business_impact(
        self,
        observation_id: str
    ) -> AIResponse:

        return self.generate_artifact(

            observation_id=observation_id,

            artifact_type="BUSINESS_IMPACT",

            

        )

    def generate_executive_summary(
        self,
        observation_id: str
    ) -> AIResponse:

        return self.generate_artifact(

            observation_id=observation_id,

            artifact_type="EXECUTIVE_SUMMARY",

            

        )

    def generate_risk_justification(
        self,
        observation_id: str
    ) -> AIResponse:

        return self.generate_artifact(

            observation_id=observation_id,

            artifact_type="RISK_JUSTIFICATION",

            

        )

    def generate_preventive_controls(
        self,
        observation_id: str
    ) -> AIResponse:

        return self.generate_artifact(

            observation_id=observation_id,

            artifact_type="PREVENTIVE_CONTROL",

            
        )
    

# =============================================================================
# Validation
# =============================================================================

def validate_artifact_generator():

    print()

    print("=" * 80)
    print("Validating Artifact Generator...")
    print("=" * 80)

    generator = ArtifactGenerator()

    response = generator.generate_root_cause(

    observation_id="OBS-0001"
    )

    if not response.success:
     raise RuntimeError(response.error_message)

    print()

    print("Artifact Generator validation completed successfully.")

    return response

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    response = validate_artifact_generator()

    print()

    print("=" * 80)
    print("GENERATED ARTIFACT")
    print("=" * 80)

    print()

    print(response.generated_text)

    print()

    print("=" * 80)
    print("ARTIFACT METADATA")
    print("=" * 80)

    print(f"Model            : {response.model}")
    print(f"Response Time    : {response.response_time} sec")
    print(f"Generated At     : {response.generated_at}")

    print()

    print("=" * 80)
    print("BUILD SUMMARY")
    print("=" * 80)

    print("Context Engine      : Passed")
    print("Prompt Builder      : Passed")
    print("LLM Service         : Passed")
    print("Artifact Generator  : Ready")

    print("=" * 80) 