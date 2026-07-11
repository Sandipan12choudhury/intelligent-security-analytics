"""
==============================================================================
AI Repository Dataset Builder

Purpose
-------
Builds the Enterprise AI Repository Dataset.

This dataset serves as the knowledge layer for the AI engine.
It stores reusable security knowledge and contextual information
for every enterprise observation.

The repository DOES NOT store AI-generated responses.

Output
------
ai_repository_dataset.xlsx

Author
------
Sandipan Choudhury

==============================================================================
"""

import os
import pandas as pd
from pathlib import Path

# =============================================================================
# Project Paths
# =============================================================================

CURRENT_FILE = Path(__file__).resolve()

PROJECT_ROOT = CURRENT_FILE.parent.parent

DATASET_DIR = PROJECT_ROOT / "dataset"

OBSERVATION_LIBRARY_PATH = (

    DATASET_DIR /

    "observation_library.xlsx"

)

AI_REPOSITORY_DATASET_PATH = (

    DATASET_DIR /

    "ai_repository_dataset.xlsx"

)

os.makedirs(

    DATASET_DIR,

    exist_ok=True

)

# =============================================================================
# Load Observation Library
# =============================================================================

print("=" * 80)
print("Loading Observation Library...")
print("=" * 80)

observation_df = pd.read_excel(

    OBSERVATION_LIBRARY_PATH

)

# =============================================================================
# Generate Stable Observation IDs
# =============================================================================

observation_df = observation_df.copy()

observation_df.insert(

    0,

    "Observation ID",

    [

        f"OBS-{i:04d}"

        for i in range(

            1,

            len(observation_df) + 1

        )

    ]

)

print(

    f"Loaded {len(observation_df)} observations."

)

print()

print("=" * 80)
print("Building AI Repository Dataset...")
print("=" * 80)

# =============================================================================
# Initialize Repository
# =============================================================================

repository_records = []

# =============================================================================
# Build AI Repository Dataset
# =============================================================================

print()

print("=" * 80)
print("Building AI Repository...")
print("=" * 80)

# =============================================================================
# Static Knowledge Dictionaries
# =============================================================================

CONTROL_OBJECTIVES = {

    "ITGC":
        "Ensure effective governance, access control and operational security.",

    "Database":
        "Protect enterprise databases through secure configuration, access management and monitoring.",

    "DFRA":
        "Ensure digital forensic readiness for timely investigation and evidence preservation.",

    "DFA / DFD":
        "Maintain secure application architecture and accurate enterprise data flows.",

    "SNA":
        "Protect enterprise networks against unauthorized access and cyber attacks."

}

SECURITY_PRINCIPLES = {

    "ITGC":
        "Confidentiality, Integrity and Availability",

    "Database":
        "Confidentiality",

    "DFRA":
        "Integrity and Accountability",

    "DFA / DFD":
        "Integrity",

    "SNA":
        "Availability and Confidentiality"

}

REFERENCE_STANDARDS = {

    "ITGC":
        "ISO 27001 | NIST CSF | RBI Cyber Security Framework",

    "Database":
        "CIS Database Benchmark | ISO 27001",

    "DFRA":
        "NIST SP 800-61 | ISO 27037",

    "DFA / DFD":
        "OWASP ASVS | Secure SDLC",

    "SNA":
        "NIST CSF | CIS Controls"

}

# =============================================================================
# Repository Creation
# =============================================================================

for _, observation in observation_df.iterrows():

    activity = observation["Activity"]

    severity = observation["Severity"]

    domain = observation["Domain"]

    observation_text = observation["Observation"]

    observation_id = observation["Observation ID"]

    # -------------------------------------------------------------------------
    # Security Knowledge
    # -------------------------------------------------------------------------

    control_objective = CONTROL_OBJECTIVES.get(

        activity,

        "Ensure enterprise security compliance."

    )

    security_principle = SECURITY_PRINCIPLES.get(

        activity,

        "CIA Triad"

    )

    reference_standard = REFERENCE_STANDARDS.get(

        activity,

        "Enterprise Security Standards"

    )

    # -------------------------------------------------------------------------
    # AI Context
    # -------------------------------------------------------------------------

    keywords = (

        f"{activity}, "

        f"{severity}, "

        f"{domain}"

    )

    prompt_context = (

        f"This observation belongs to the "

        f"{activity} activity with "

        f"{severity} severity."

    )

    root_cause_hint = (

        "Identify the most probable technical and process-related root cause."

    )

    impact_hint = (

        "Describe the business and security impact if left unresolved."

    )

    recommendation_hint = (

        "Recommend practical remediation aligned with enterprise best practices."

    )

    executive_summary_hint = (

        "Summarize the issue for executive management using professional audit language."

    )

    # -------------------------------------------------------------------------
    # Governance Metadata
    # -------------------------------------------------------------------------

    knowledge_version = "1.0"

    knowledge_status = "Active"

    # -------------------------------------------------------------------------
    # Store Repository Record
    # -------------------------------------------------------------------------

    repository_records.append({

        # Identity

        "Observation ID": observation_id,

        "Observation": observation_text,

        "Activity": activity,

        "Domain": domain,

        "Severity": severity,

        # Security Knowledge

        "Control Objective": control_objective,

        "Security Principle": security_principle,

        "Reference Standard": reference_standard,

        # AI Context

        "Keywords": keywords,

        "Prompt Context": prompt_context,

        "Root Cause Hint": root_cause_hint,

        "Impact Hint": impact_hint,

        "Recommendation Hint": recommendation_hint,

        "Executive Summary Hint": executive_summary_hint,

        # Governance Metadata

        "Knowledge Version": knowledge_version,

        "Knowledge Status": knowledge_status

    })

repository_df = pd.DataFrame(

    repository_records

)

print()

print(

    f"Generated {len(repository_df)} AI Repository records."

)

# =============================================================================
# Validate AI Repository Dataset
# =============================================================================

print()

print("=" * 80)
print("Validating AI Repository Dataset...")
print("=" * 80)

# -------------------------------------------------------------------------
# Validate Record Count
# -------------------------------------------------------------------------

assert (

    len(repository_df)

    ==

    len(observation_df)

), (

    "Repository record count mismatch."

)

# -------------------------------------------------------------------------
# Validate Unique Observation IDs
# -------------------------------------------------------------------------

assert (

    repository_df["Observation ID"].is_unique

), (

    "Duplicate Observation IDs detected."

)

# -------------------------------------------------------------------------
# Validate Missing Values
# -------------------------------------------------------------------------

assert (

    repository_df.isnull().sum().sum()

    ==

    0

), (

    "Missing values detected in repository."

)

print(

    "AI Repository Dataset validation completed successfully."

)

# =============================================================================
# Export AI Repository Dataset
# =============================================================================

repository_df.to_excel(

    AI_REPOSITORY_DATASET_PATH,

    index=False

)

print()

print(

    "AI Repository Dataset exported successfully."

)

# =============================================================================
# Build Summary
# =============================================================================

print()

print("=" * 80)
print("BUILD SUMMARY")
print("=" * 80)

print(

    f"Knowledge Records Created : {len(repository_df)}"

)

print(

    f"Activities Covered        : "

    f"{repository_df['Activity'].nunique()}"

)

print(

    f"Domains Covered           : "

    f"{repository_df['Domain'].nunique()}"

)

print(

    f"High Severity Records     : "

    f"{(repository_df['Severity'] == 'High').sum()}"

)

print(

    f"Medium Severity Records   : "

    f"{(repository_df['Severity'] == 'Medium').sum()}"

)

print(

    f"Low Severity Records      : "

    f"{(repository_df['Severity'] == 'Low').sum()}"

)

print(

    f"Repository Version        : "

    f"{repository_df['Knowledge Version'].iloc[0]}"

)

print("=" * 80)