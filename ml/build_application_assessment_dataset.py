"""
==============================================================================
Application Assessment Dataset Builder

Purpose
-------
Creates the Application Assessment Dataset template.

Unlike the Knowledge Layer, this dataset is operational.

The Enterprise Portal appends new assessment records to this dataset whenever
an auditor submits observations during an application assessment.

Output
------
application_assessment_dataset.xlsx

Author
------
Sandipan Choudhury

==============================================================================
"""
print("Script Started")

import os
import pandas as pd
from pathlib import Path


# =============================================================================
# Project Paths
# =============================================================================

CURRENT_FILE = Path(__file__).resolve()

PROJECT_ROOT = CURRENT_FILE.parent.parent

DATASET_DIR = PROJECT_ROOT / "dataset"

APPLICATION_ASSESSMENT_DATASET_PATH = (

    DATASET_DIR /

    "application_assessment_dataset.xlsx"

)

os.makedirs(

    DATASET_DIR,

    exist_ok=True

)

# =============================================================================
# Assessment Dataset Schema
# =============================================================================

ASSESSMENT_COLUMNS = [

    "Assessment ID",

    "Assessment Cycle",

    "User ID",

    "Application ID",

    "Activity",

    "Observation ID",

    "Severity",

    "Assessment Timestamp",

    "Source"

]

print("=" * 80)
print("Creating Application Assessment Dataset...")
print("=" * 80)

# =============================================================================
# Create Empty Assessment Dataset
# =============================================================================

assessment_dataset_df = pd.DataFrame(

    columns=ASSESSMENT_COLUMNS

)

print(

    f"Dataset Columns : {len(assessment_dataset_df.columns)}"

)

print(

    "Initial Records : 0"

)

# =============================================================================
# Validate Assessment Dataset
# =============================================================================

print()

print("=" * 80)
print("Validating Assessment Dataset...")
print("=" * 80)


# -------------------------------------------------------------------------
# Validate Column Count
# -------------------------------------------------------------------------

EXPECTED_COLUMNS = 9

assert (

    len(assessment_dataset_df.columns)

    ==

    EXPECTED_COLUMNS

), (

    f"Expected {EXPECTED_COLUMNS} columns, "
    f"but found {len(assessment_dataset_df.columns)}."

)


# -------------------------------------------------------------------------
# Validate Mandatory Columns
# -------------------------------------------------------------------------

expected_schema = [

    "Assessment ID",

    "Assessment Cycle",

    "User ID",

    "Application ID",

    "Activity",

    "Observation ID",

    "Severity",

    "Assessment Timestamp",

    "Source"

]

assert (

    list(assessment_dataset_df.columns)

    ==

    expected_schema

), (

    "Assessment Dataset schema mismatch."

)

print(

    "Assessment Dataset validation completed successfully."

)

# =============================================================================
# Export Assessment Dataset
# =============================================================================

assessment_dataset_df.to_excel(

    APPLICATION_ASSESSMENT_DATASET_PATH,

    index=False

)

print()

print(

    "Application Assessment Dataset exported successfully."

)

# =============================================================================
# Build Summary
# =============================================================================

print()

print("=" * 80)
print("BUILD SUMMARY")
print("=" * 80)

print(

    f"Assessment Records : "
    f"{len(assessment_dataset_df)}"

)

print(

    f"Dataset Columns    : "
    f"{len(assessment_dataset_df.columns)}"

)

print(

    "Status             : Template Created"

)

print("=" * 80)

