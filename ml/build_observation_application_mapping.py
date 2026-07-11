"""
==============================================================================
Observation-Application Mapping Builder

Purpose
-------
Creates the mapping between enterprise observations and enterprise
applications.

Every observation is deterministically assigned to exactly one
enterprise application.

Output
------
observation_application_mapping.xlsx

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

APPLICATION_MASTER_PATH = (
    DATASET_DIR /
    "application_master.xlsx"
)

OBSERVATION_APPLICATION_MAPPING_PATH = (
    DATASET_DIR /
    "observation_application_mapping.xlsx"
)

os.makedirs(
    DATASET_DIR,
    exist_ok=True
)

# =============================================================================
# Load Enterprise Datasets
# =============================================================================

print("=" * 80)
print("Loading Enterprise Datasets...")
print("=" * 80)

observation_df = pd.read_excel(
    OBSERVATION_LIBRARY_PATH
)

application_df = pd.read_excel(
    APPLICATION_MASTER_PATH
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

print(
    f"Loaded {len(application_df)} applications."
)

print()

print("=" * 80)
print("Building Observation-Application Mapping...")
print("=" * 80)

# =============================================================================
# Enterprise Application Pools
# =============================================================================

DEPARTMENT_WEIGHTS = {

    "IT-Treasure Support Services": 0.35,

    "NG-Data Ware House": 0.25,

    "Network Technology": 0.15,

    "Cloud Solutions": 0.10,

    "IT-Regulatory Applications": 0.10,

    "Trade Finance": 0.05

}


# =============================================================================
# Create Department-wise Application Pools
# =============================================================================

APPLICATION_POOLS = {}

for department in DEPARTMENT_WEIGHTS.keys():

    department_apps = application_df[

        application_df["Department"] == department

    ].copy()

    APPLICATION_POOLS[department] = (

        department_apps
        .sort_values("Application Name")
        .reset_index(drop=True)

    )


print()

print("=" * 80)
print("Enterprise Application Pools")
print("=" * 80)

for department, apps in APPLICATION_POOLS.items():

    print(

        f"{department:<35} : {len(apps)} applications"

    )

# =============================================================================
# Generate Observation → Application Mapping
# =============================================================================

ACTIVITY_MATRIX = {

    "ITGC": list(DEPARTMENT_WEIGHTS.keys()),

    "Database": [
        "IT-Treasure Support Services",
        "Trade Finance",
        "IT-Regulatory Applications",
        "Cloud Solutions",
        "NG-Data Ware House"
    ],

    "DFRA": list(DEPARTMENT_WEIGHTS.keys()),

    "DFA / DFD": [
        "IT-Treasure Support Services",
        "Trade Finance",
        "IT-Regulatory Applications",
        "Network Technology",
        "NG-Data Ware House"
    ],

    "SNA": [
        "IT-Treasure Support Services",
        "IT-Regulatory Applications",
        "Cloud Solutions",
        "Network Technology",
        "NG-Data Ware House"
    ]

}


MAPPING_RECORDS = []



print()

print("=" * 80)
print("Generating Observation → Application Mapping...")
print("=" * 80)


# =============================================================================
# Process Each Activity Independently
# =============================================================================

for activity in observation_df["Activity"].unique():

    activity_df = observation_df[
        observation_df["Activity"] == activity
    ].reset_index(drop=True)

    total_activity = len(activity_df)

    eligible_departments = ACTIVITY_MATRIX[activity]

    # -------------------------------------------------------------------------
    # Normalize department weights
    # -------------------------------------------------------------------------

    eligible_weight_sum = sum(

        DEPARTMENT_WEIGHTS[d]

        for d in eligible_departments

    )

    normalized_weights = {

        d: DEPARTMENT_WEIGHTS[d] / eligible_weight_sum

        for d in eligible_departments

    }

    # -------------------------------------------------------------------------
    # Department-wise allocation
    # -------------------------------------------------------------------------

    department_allocations = {}

    allocated = 0

    for index, department in enumerate(eligible_departments):

        if index == len(eligible_departments) - 1:

            allocation = total_activity - allocated

        else:

            allocation = int(

                total_activity *

                normalized_weights[department]

            )

            allocated += allocation

        department_allocations[department] = allocation

    # -------------------------------------------------------------------------
    # Round Robin Allocation inside each department
    # -------------------------------------------------------------------------

    activity_pointer = 0

    for department in eligible_departments:

        application_pool = APPLICATION_POOLS[department]

        application_count = len(application_pool)

        allocation = department_allocations[department]

        for i in range(allocation):

            if activity_pointer >= total_activity:

                break

            application = application_pool.iloc[

                i % application_count

            ]

            MAPPING_RECORDS.append({

                "Observation ID":
                    activity_df.iloc[activity_pointer]["Observation ID"],

                "Activity":
                    activity,

                "Application ID":
                    application["Application ID"],

                "Application Name":
                    application["Application Name"],

                "Department":
                    department

            })

            

            activity_pointer += 1


mapping_df = pd.DataFrame(

    MAPPING_RECORDS

)

print()

print(

    f"Generated {len(mapping_df)} mappings."

)

# =============================================================================
# Validate Observation-Application Mapping
# =============================================================================

print()

print("=" * 80)
print("Validating Observation-Application Mapping...")
print("=" * 80)

# -------------------------------------------------------------------------
# Validate Record Count
# -------------------------------------------------------------------------

assert (

    len(mapping_df)

    ==

    len(observation_df)

), (

    "Mismatch between observations and generated mappings."

)

# -------------------------------------------------------------------------
# Validate Unique Observation IDs
# -------------------------------------------------------------------------

assert (

    mapping_df["Observation ID"].is_unique

), (

    "Duplicate Observation IDs detected."

)

# -------------------------------------------------------------------------
# Validate Missing Values
# -------------------------------------------------------------------------

assert (

    mapping_df.isnull().sum().sum()

    ==

    0

), (

    "Missing values detected in mapping dataset."

)

print(

    "Observation-Application Mapping validation completed successfully."

)

# =============================================================================
# Export Observation-Application Mapping
# =============================================================================

mapping_df.to_excel(

    OBSERVATION_APPLICATION_MAPPING_PATH,

    index=False

)

print()

print(

    "Observation-Application Mapping exported successfully."

)

# =============================================================================
# Build Summary
# =============================================================================

print()

print("=" * 80)
print("BUILD SUMMARY")
print("=" * 80)

print(

    f"Observations Processed : {len(observation_df)}"

)

print(

    f"Applications Covered   : {application_df['Application ID'].nunique()}"

)

print(

    f"Mappings Generated     : {len(mapping_df)}"

)

print("=" * 80)

