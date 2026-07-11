"""
==============================================================================
Activity Analytics Dataset Builder

Purpose
-------
Builds the Enterprise Activity Analytics Dataset.

Each row represents one enterprise security assessment activity.

The dataset powers:

    • Activity Dashboard
    • Activity Comparison
    • Executive Reporting
    • AI Intelligence Engine
    • Machine Learning Engine

Input
-----
observation_library.xlsx

observation_application_mapping.xlsx

application_master.xlsx

Output
------
activity_analytics_dataset.xlsx

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

OBSERVATION_APPLICATION_MAPPING_PATH = (

    DATASET_DIR /

    "observation_application_mapping.xlsx"

)

APPLICATION_MASTER_PATH = (

    DATASET_DIR /

    "application_master.xlsx"

)

ACTIVITY_ANALYTICS_DATASET_PATH = (

    DATASET_DIR /

    "activity_analytics_dataset.xlsx"

)

os.makedirs(

    DATASET_DIR,

    exist_ok=True

)

# =============================================================================
# Enterprise Configuration
# =============================================================================

LOW_RISK_THRESHOLD = 63

HIGH_RISK_THRESHOLD = 77

# =============================================================================
# Load Enterprise Datasets
# =============================================================================

print("=" * 80)
print("Loading Enterprise Datasets...")
print("=" * 80)

observation_df = pd.read_excel(

    OBSERVATION_LIBRARY_PATH

)

mapping_df = pd.read_excel(

    OBSERVATION_APPLICATION_MAPPING_PATH

)

application_df = pd.read_excel(

    APPLICATION_MASTER_PATH

)

print(

    f"Loaded {len(observation_df)} observations."

)

print(

    f"Loaded {len(mapping_df)} mappings."

)

print(

    f"Loaded {len(application_df)} applications."

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

# =============================================================================
# Merge Enterprise Datasets
# =============================================================================

merged_df = pd.merge(

    observation_df,

    mapping_df,

    on="Observation ID",

    how="inner"

)

merged_df = pd.merge(

    merged_df,

    application_df,

    on=[

        "Application ID",

        "Application Name",

        "Department"

    ],

    how="left"

)

# =============================================================================
# Resolve Duplicate Columns
# =============================================================================

if "Activity_x" in merged_df.columns:

    merged_df = merged_df.drop(

        columns=["Activity_x"]

    )

if "Activity_y" in merged_df.columns:

    merged_df = merged_df.rename(

        columns={

            "Activity_y": "Activity"

        }

    )

print()

print(

    f"Merged Records : {len(merged_df)}"

)

print()

print("=" * 80)
print("Building Activity Analytics Dataset...")
print("=" * 80)




# =============================================================================
# Compute Activity Analytics
# =============================================================================

print()

print("=" * 80)
print("Computing Activity Analytics...")
print("=" * 80)

activity_records = []

ACTIVITIES = [

    "ITGC",

    "Database",

    "DFRA",

    "DFA / DFD",

    "SNA"

]

for activity in ACTIVITIES:

    activity_df = merged_df[

        merged_df["Activity"] == activity

    ]

    # -------------------------------------------------------------------------
    # Coverage
    # -------------------------------------------------------------------------

    department_count = activity_df["Department"].nunique()

    application_count = activity_df["Application ID"].nunique()

    total_observations = len(activity_df)

    # -------------------------------------------------------------------------
    # Severity Counts
    # -------------------------------------------------------------------------

    high_count = (

        activity_df["Severity"]

        .eq("High")

        .sum()

    )

    medium_count = (

        activity_df["Severity"]

        .eq("Medium")

        .sum()

    )

    low_count = (

        activity_df["Severity"]

        .eq("Low")

        .sum()

    )

    # -------------------------------------------------------------------------
    # Severity %
    # -------------------------------------------------------------------------

    if total_observations > 0:

        high_percentage = round(

            high_count / total_observations * 100,

            2

        )

        medium_percentage = round(

            medium_count / total_observations * 100,

            2

        )

        low_percentage = round(

            low_count / total_observations * 100,

            2

        )

    else:

        high_percentage = 0

        medium_percentage = 0

        low_percentage = 0

    # -------------------------------------------------------------------------
    # Risk Score
    # -------------------------------------------------------------------------

    risk_score = round(

        (

            high_percentage * 1.0 +

            medium_percentage * 0.6 +

            low_percentage * 0.3

        ),

        2

    )

    compliance_percentage = round(

        100 - risk_score,

        2

    )

    # -------------------------------------------------------------------------
    # Risk Category
    # -------------------------------------------------------------------------

    if risk_score < LOW_RISK_THRESHOLD:

        risk_category = "Low"

    elif risk_score < HIGH_RISK_THRESHOLD:

        risk_category = "Medium"

    else:

        risk_category = "High"

    # -------------------------------------------------------------------------
    # Compliance Grade
    # -------------------------------------------------------------------------

    if compliance_percentage >= 90:

        compliance_grade = "A"

    elif compliance_percentage >= 80:

        compliance_grade = "B"

    elif compliance_percentage >= 70:

        compliance_grade = "C"

    elif compliance_percentage >= 60:

        compliance_grade = "D"

    else:

        compliance_grade = "F"

    # -------------------------------------------------------------------------
    # Department Distribution
    # -------------------------------------------------------------------------

    department_distribution = (

        activity_df

        .groupby("Department")

        .size()

        .sort_values(

            ascending=False

        )

    )

    # -------------------------------------------------------------------------
    # Application Distribution
    # -------------------------------------------------------------------------

    application_distribution = (

        activity_df

        .groupby(

            [

                "Application ID",

                "Application Name"

            ]

        )

        .size()

        .sort_values(

            ascending=False

        )

    )

    # -------------------------------------------------------------------------
    # Technology Domain Distribution
    # -------------------------------------------------------------------------

    technology_distribution = (

        activity_df

        .groupby(

            "Technology Domain"

        )

        .size()

        .sort_values(

            ascending=False

        )

    )

    # -------------------------------------------------------------------------
    # Business Criticality Distribution
    # -------------------------------------------------------------------------

    criticality_distribution = (

        activity_df

        .groupby(

            "Business Criticality"

        )

        .size()

        .sort_values(

            ascending=False

        )

    )

    # -------------------------------------------------------------------------
    # Average Observations
    # -------------------------------------------------------------------------

    average_observations_per_application = round(

        total_observations /

        application_count,

        2

    )

    average_observations_per_department = round(

        total_observations /

        department_count,

        2

    )

    # -------------------------------------------------------------------------
    # Most / Least Affected Departments
    # -------------------------------------------------------------------------

    most_department = department_distribution.index[0]

    most_department_observations = int(

        department_distribution.iloc[0]

    )

    least_department = department_distribution.index[-1]

    least_department_observations = int(

        department_distribution.iloc[-1]

    )

    top_departments = list(

        department_distribution.head(3).index

    )

    while len(top_departments) < 3:

        top_departments.append(

            top_departments[-1]

        )

    # -------------------------------------------------------------------------
    # Most / Least Affected Applications
    # -------------------------------------------------------------------------

    most_application = application_distribution.index[0]

    least_application = application_distribution.index[-1]

    top_applications = list(

        application_distribution.head(3).index

    )

    while len(top_applications) < 3:

        top_applications.append(

            top_applications[-1]

        )

    # -------------------------------------------------------------------------
    # Technology Analytics
    # -------------------------------------------------------------------------

    technology_domains_covered = technology_distribution.shape[0]

    top_technology_domain = technology_distribution.index[0]

    top_technology_percentage = round(

        technology_distribution.iloc[0]

        /

        total_observations

        * 100,

        2

    )

    # -------------------------------------------------------------------------
    # AI Metadata
    # -------------------------------------------------------------------------

    severity_dictionary = {

        "High": high_percentage,

        "Medium": medium_percentage,

        "Low": low_percentage

    }

    dominant_severity = max(

        severity_dictionary,

        key=severity_dictionary.get

    )

    dominant_severity_percentage = round(

        severity_dictionary[dominant_severity],

        2

    )

    most_common_business_criticality = (

        criticality_distribution.index[0]

    )

    # -------------------------------------------------------------------------
    # Executive Priority
    # -------------------------------------------------------------------------

    if risk_score >= 85:

        executive_priority = "Critical"

    elif risk_score >= 70:

        executive_priority = "High"

    elif risk_score >= 40:

        executive_priority = "Medium"

    else:

        executive_priority = "Low"

    # -------------------------------------------------------------------------
    # Store Activity Analytics
    # -------------------------------------------------------------------------

    activity_records.append({

        # Identity

        "Activity": activity,

        # Coverage

        "Departments Covered": department_count,

        "Applications Covered": application_count,

        "Total Observations": total_observations,

        # Severity

        "High Count": high_count,

        "Medium Count": medium_count,

        "Low Count": low_count,

        # Severity %

        "High %": high_percentage,

        "Medium %": medium_percentage,

        "Low %": low_percentage,

        # Risk

        "Risk Score": risk_score,

        "Risk Category": risk_category,

        "Compliance %": compliance_percentage,

        "Compliance Grade": compliance_grade,

        # Department Analytics

        "Most Affected Department": most_department,

        "Most Department Observations":

            most_department_observations,

        "Least Affected Department": least_department,

        "Least Department Observations":

            least_department_observations,

        "Top 1 Department": top_departments[0],

        "Top 2 Department": top_departments[1],

        "Top 3 Department": top_departments[2],

        # Application Analytics

        "Most Affected Application ID":

            most_application[0],

        "Most Affected Application Name":

            most_application[1],

        "Least Affected Application ID":

            least_application[0],

        "Least Affected Application Name":

            least_application[1],

        "Top 1 Application ID":

            top_applications[0][0],

        "Top 1 Application Name":

            top_applications[0][1],

        "Top 2 Application ID":

            top_applications[1][0],

        "Top 2 Application Name":

            top_applications[1][1],

        "Top 3 Application ID":

            top_applications[2][0],

        "Top 3 Application Name":

            top_applications[2][1],

        # Technology

        "Technology Domains Covered":

            technology_domains_covered,

        "Top Technology Domain":

            top_technology_domain,

        "Top Technology Domain %":

            top_technology_percentage,

        # AI Metadata

        "Dominant Severity":

            dominant_severity,

        "Dominant Severity %":

            dominant_severity_percentage,

        "Most Common Business Criticality":

            most_common_business_criticality,

        "Average Observations per Application":

            average_observations_per_application,

        "Average Observations per Department":

            average_observations_per_department,

        # Executive

        "Executive Priority":

            executive_priority

    })

# =============================================================================
# Create Activity Analytics DataFrame
# =============================================================================

activity_analytics_df = pd.DataFrame(

    activity_records

)

# =============================================================================
# Enterprise Activity Ranking
# =============================================================================

print()

print("=" * 80)
print("Computing Enterprise Activity Rankings...")
print("=" * 80)

activity_analytics_df = (

    activity_analytics_df

    .sort_values(

        by="Risk Score",

        ascending=False

    )

    .reset_index(drop=True)

)

activity_analytics_df.insert(

    0,

    "Enterprise Rank",

    range(

        1,

        len(activity_analytics_df) + 1

    )

)

print(

    "Enterprise Activity Ranking completed."

)

# =============================================================================
# Validate Activity Analytics Dataset
# =============================================================================

print()

print("=" * 80)
print("Validating Activity Analytics Dataset...")
print("=" * 80)

assert len(activity_analytics_df) == 5, (

    "Activity count mismatch."

)

assert activity_analytics_df["Activity"].is_unique, (

    "Duplicate activities detected."

)

assert activity_analytics_df.isnull().sum().sum() == 0, (

    "Missing values detected."

)

assert (

    activity_analytics_df["Total Observations"].sum()

    ==

    len(observation_df)

), (

    "Observation aggregation mismatch."

)

print(

    "Activity Analytics Dataset validation completed successfully."

)

# =============================================================================
# Export Activity Analytics Dataset
# =============================================================================

activity_analytics_df.to_excel(

    ACTIVITY_ANALYTICS_DATASET_PATH,

    index=False

)

print()

print(

    "Activity Analytics Dataset exported successfully."

)

# =============================================================================
# Build Summary
# =============================================================================

print()

print("=" * 80)
print("BUILD SUMMARY")
print("=" * 80)

print(

    f"Activities Processed : {len(activity_analytics_df)}"

)

print(

    f"Observations Aggregated : "

    f"{activity_analytics_df['Total Observations'].sum()}"

)

print(

    f"Highest Risk Activity : "

    f"{activity_analytics_df.iloc[0]['Activity']}"

)

print(

    f"Highest Risk Score : "

    f"{activity_analytics_df.iloc[0]['Risk Score']}"

)

print(

    f"Average Risk Score : "

    f"{round(activity_analytics_df['Risk Score'].mean(), 2)}"

)

print("=" * 80)