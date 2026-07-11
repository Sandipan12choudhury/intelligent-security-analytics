"""
==============================================================================
LLM Service

Purpose
-------
Provides a unified interface for interacting with the configured
Large Language Model (LLM).

Responsibilities
----------------
• Initialize the Gemini client
• Generate AI responses
• Return structured AIResponse objects

This module does NOT:

    • Read enterprise datasets
    • Build enterprise prompts
    • Perform analytics
    • Store AI responses

Author
------
Sandipan Choudhury

==============================================================================
"""
from .context_engine import build_context
from .ai_prompt_builder import build_prompt

from dataclasses import dataclass
from datetime import datetime
import time

from google import genai
from google.genai import types
from .config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    TEMPERATURE,
    MAX_OUTPUT_TOKENS
)

# =============================================================================
# AI Response Model
# =============================================================================

@dataclass
class AIResponse:

    success: bool

    artifact_type: str

    generated_text: str

    model: str

    generated_at: datetime

    response_time: float

    error_message: str | None = None

# =============================================================================
# Gemini Client Initialization
# =============================================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)

# =============================================================================
# LLM Service
# =============================================================================

class LLMService:

    """
    Enterprise wrapper around Gemini.
    """

    def __init__(self):

        self.client = client

        self.model = GEMINI_MODEL

        self.temperature = TEMPERATURE

        self.max_output_tokens = MAX_OUTPUT_TOKENS

    def get_model_information(self):

        """
        Returns current model configuration.
        """

        return {

            "provider": "Google Gemini",

            "model": self.model,

            "temperature": self.temperature,

            "max_output_tokens": self.max_output_tokens

        }

    # =============================================================================
    # Generate AI Response
    # =============================================================================

    def generate_response(
        self,
        prompt: str,
        artifact_type: str
    ) -> AIResponse:

        """
        Sends a prompt to Gemini and returns
        a structured AIResponse.
        """

        start_time = time.perf_counter()

        try:

            response = self.client.models.generate_content(

                model=self.model,

                contents=prompt,

                config=types.GenerateContentConfig(

                    temperature=self.temperature,

                    max_output_tokens=self.max_output_tokens

                )

            )

            generated_text = (response.text or "").strip()

            if not generated_text:

                raise ValueError(
                    "Gemini returned an empty response."
                )

            elapsed_time = round(
                time.perf_counter() - start_time,
                2
            )

            return AIResponse(

                success=True,

                artifact_type=artifact_type,

                generated_text=generated_text,

                model=self.model,

                generated_at=datetime.now(),

                response_time=elapsed_time

            )

        except Exception as error:

            elapsed_time = round(
                time.perf_counter() - start_time,
                2
            )

            return AIResponse(

                success=False,

                artifact_type=artifact_type,

                generated_text="",

                model=self.model,

                generated_at=datetime.now(),

                response_time=elapsed_time,

                error_message=str(error)

            )
    
# =============================================================================
# Validation
# =============================================================================

def validate_llm_service():

    print()

    print("=" * 80)
    print("Validating LLM Service...")
    print("=" * 80)

    service = LLMService()

    print()

    print("Building Enterprise AI Context...")

    context = build_context(

        observation_id="OBS-0001",

        artifact_type="ROOT_CAUSE",

        user_prompt="Generate a professional technical root cause."

    )

    print("Context Ready.")

    print()

    print("Building Enterprise Prompt...")

    prompt = build_prompt(context)

    print("Prompt Ready.")

    print()

    print("Generating AI Response...")

    response = service.generate_response(

        prompt=prompt,

        artifact_type="ROOT_CAUSE"

    )

    if not response.success:

        raise RuntimeError(response.error_message)

    print("AI Response Generated Successfully.")

    return response

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    response = validate_llm_service()

    print()

    print("=" * 80)
    print("GENERATED AI RESPONSE")
    print("=" * 80)

    print()

    print(response.generated_text)

    print()

    print("=" * 80)
    print("AI RESPONSE METADATA")
    print("=" * 80)

    print(f"Model              : {response.model}")
    print(f"Response Time      : {response.response_time} sec")
    print(f"Generated At       : {response.generated_at}")

    print()

    print("=" * 80)
    print("BUILD SUMMARY")
    print("=" * 80)

    print("Context Engine      : Passed")
    print("Prompt Builder      : Passed")
    print("Gemini Connection   : Passed")
    print("Response Generated  : Passed")
    print("LLM Service Status  : Ready")

    print("=" * 80)