"""
==============================================================================
Application Dataset Builder

Purpose
-------
Creates the Enterprise Application Dataset.

This dataset represents the current operational security snapshot
for every enterprise application.

Each row corresponds to one application.

The dataset is later enriched by:

    • Application Analytics Builder
    • Feature Engineering Builder
    • Machine Learning Engine

Output
------
application_dataset.xlsx

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

APPLICATION_MASTER_PATH = (

    DATASET_DIR /

    "application_master.xlsx"

)

APPLICATION_DATASET_PATH = (

    DATASET_DIR /

    "application_dataset.xlsx"

)

os.makedirs(

    DATASET_DIR,

    exist_ok=True

)

# =============================================================================
# Load Application Master
# =============================================================================

print("=" * 80)
print("Loading Application Master...")
print("=" * 80)

application_master_df = pd.read_excel(

    APPLICATION_MASTER_PATH

)


print(

    f"Loaded {len(application_master_df)} applications."

)

print()

print("=" * 80)
print("Building Enterprise Application Dataset...")
print("=" * 80)

# =============================================================================
# Load Observation Library
# =============================================================================

OBSERVATION_LIBRARY_PATH = (

    DATASET_DIR /

    "observation_library.xlsx"

)

OBSERVATION_APPLICATION_MAPPING_PATH = (

    DATASET_DIR /

    "observation_application_mapping.xlsx"

)

print()

print("=" * 80)
print("Loading Supporting Datasets...")
print("=" * 80)

observation_df = pd.read_excel(

    OBSERVATION_LIBRARY_PATH

)

mapping_df = pd.read_excel(

    OBSERVATION_APPLICATION_MAPPING_PATH

)

print(

    f"Loaded {len(observation_df)} observations."

)

print(

    f"Loaded {len(mapping_df)} observation mappings."

)

# =============================================================================
# Generate Temporary Observation IDs
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

# =============================================================================
# Merge Observation Library with Application Mapping
# =============================================================================

merged_df = pd.merge(

    observation_df,

    mapping_df,

    on="Observation ID",

    how="inner"

)
# =============================================================================
# Resolve Duplicate Activity Columns
# =============================================================================

merged_df = merged_df.drop(columns=["Activity_x"])

merged_df = merged_df.rename(
    columns={
        "Activity_y": "Activity"
    }
)
print()

print(

    f"Merged Records : {len(merged_df)}"

)



# =============================================================================
# Aggregate Enterprise Application Metrics
# =============================================================================

print()

print("=" * 80)
print("Aggregating Enterprise Application Metrics...")
print("=" * 80)


application_dataset_records = []


for _, application in application_master_df.iterrows():

    application_id = application["Application ID"]

    application_name = application["Application Name"]


    app_data = merged_df[

        merged_df["Application ID"] == application_id

    ]


    total_observations = len(app_data)


    high_count = (

        app_data["Severity"]

        .eq("High")

        .sum()

    )

    medium_count = (

        app_data["Severity"]

        .eq("Medium")

        .sum()

    )

    low_count = (

        app_data["Severity"]

        .eq("Low")

        .sum()

    )


    itgc_count = (

        app_data["Activity"]

        .eq("ITGC")

        .sum()

    )

    database_review_count = (

        app_data["Activity"]

        .eq("Database")

        .sum()

    )

    dfra_count = (

        app_data["Activity"]

        .eq("DFRA")

        .sum()

    )

    dfa_count = (

        app_data["Activity"]

        .eq("DFA / DFD")

        .sum()

    )

    sna_count = (

        app_data["Activity"]

        .eq("SNA")

        .sum()

    )


    application_dataset_records.append({

    "Application ID": application["Application ID"],

    "Application Name": application["Application Name"],

    "Department": application["Department"],

    "Application Type": application["Application Type"],

    "Technology Domain": application["Technology Domain"],

    "Business Criticality": application["Business Criticality"],

    "Environment": application["Environment"],

    "Status": application["Status"],

    "Total Observations": total_observations,

    "High Count": high_count,

    "Medium Count": medium_count,

    "Low Count": low_count,

    "ITGC Count": itgc_count,

    "Database Review Count": database_review_count,

    "DFRA Count": dfra_count,

    "DFA Count": dfa_count,

    "SNA Count": sna_count

})


application_dataset_df = pd.DataFrame(

    application_dataset_records

)

print(

    f"Generated {len(application_dataset_df)} application records."

)

# =============================================================================
# Validate Application Dataset
# =============================================================================

print()

print("=" * 80)
print("Validating Application Dataset...")
print("=" * 80)


assert (

    len(application_dataset_df)

    ==

    len(application_master_df)

), (

    "Application count mismatch."

)


assert (

    application_dataset_df["Application ID"].is_unique

), (

    "Duplicate Application IDs detected."

)


assert (

    application_dataset_df.isnull().sum().sum()

    ==

    0

), (

    "Missing values detected."

)


total_observations = (

    application_dataset_df[

        "Total Observations"

    ].sum()

)

assert (

    total_observations

    ==

    len(observation_df)

), (

    "Observation aggregation mismatch."

)


print(

    "Application Dataset validation completed successfully."

)

# =============================================================================
# Export Application Dataset
# =============================================================================

application_dataset_df.to_excel(

    APPLICATION_DATASET_PATH,

    index=False

)

print()

print(

    "Application Dataset exported successfully."

)

# =============================================================================
# Build Summary
# =============================================================================

print()

print("=" * 80)
print("BUILD SUMMARY")
print("=" * 80)

print(

    f"Applications Processed : {len(application_dataset_df)}"

)

print(

    f"Observations Aggregated : "

    f"{application_dataset_df['Total Observations'].sum()}"

)

print(

    f"High Severity Findings : "

    f"{application_dataset_df['High Count'].sum()}"

)

print(

    f"Medium Severity Findings : "

    f"{application_dataset_df['Medium Count'].sum()}"

)

print(

    f"Low Severity Findings : "

    f"{application_dataset_df['Low Count'].sum()}"

)

print("=" * 80)