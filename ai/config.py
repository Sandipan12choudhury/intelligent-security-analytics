"""
==============================================================================
AI Configuration

Purpose
-------
Loads and validates configuration required by the AI modules.

This module is responsible only for reading configuration from
the environment and exposing validated settings.

It does NOT:

    • Connect to Gemini
    • Build prompts
    • Generate AI responses
    • Read enterprise datasets

Author
------
Sandipan Choudhury

==============================================================================
"""

from pathlib import Path
import os

from dotenv import load_dotenv

# =============================================================================
# Load Environment Variables
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / ".env")

# =============================================================================
# Gemini Configuration
# =============================================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        "0.3"
    )
)

MAX_OUTPUT_TOKENS = int(
    os.getenv(
        "MAX_OUTPUT_TOKENS",
        "2048"
    )
)

# =============================================================================
# Configuration Validation
# =============================================================================

def validate_configuration():

    """
    Validates all required AI configuration.
    """

    print()

    print("=" * 80)
    print("Validating AI Configuration...")
    print("=" * 80)

    if not GEMINI_API_KEY:

        raise ValueError(
            "GEMINI_API_KEY was not found in the .env file."
        )

    if TEMPERATURE < 0 or TEMPERATURE > 2:

        raise ValueError(
            "TEMPERATURE must be between 0 and 2."
        )

    if MAX_OUTPUT_TOKENS <= 0:

        raise ValueError(
            "MAX_OUTPUT_TOKENS must be greater than zero."
        )

    print()

    print("AI Configuration validated successfully.")

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    validate_configuration()

    print()

    print("=" * 80)
    print("CURRENT CONFIGURATION")
    print("=" * 80)

    print(f"Model                : {GEMINI_MODEL}")
    print(f"Temperature          : {TEMPERATURE}")
    print(f"Max Output Tokens    : {MAX_OUTPUT_TOKENS}")

    print()

    print("=" * 80)
    print("BUILD SUMMARY")
    print("=" * 80)

    print("Configuration Status : Ready")
    print("Environment Loaded   : Yes")
    print("API Key Loaded       : Yes")

    print("=" * 80)