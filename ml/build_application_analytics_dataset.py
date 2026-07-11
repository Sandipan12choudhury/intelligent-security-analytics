"""
==============================================================================
Application Analytics Dataset Builder

Purpose
-------
Builds the Enterprise Application Analytics Dataset.

This builder converts the operational application dataset into
analytics-ready metrics for:

    • Enterprise Dashboard
    • Department Dashboard
    • Application Dashboard
    • Executive Reporting
    • AI Intelligence Engine
    • Machine Learning Engine

Input
-----
application_dataset.xlsx

Output
------
application_analytics_dataset.xlsx

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

APPLICATION_DATASET_PATH = (

    DATASET_DIR /

    "application_dataset.xlsx"

)

APPLICATION_ANALYTICS_DATASET_PATH = (

    DATASET_DIR /

    "application_analytics_dataset.xlsx"

)

os.makedirs(

    DATASET_DIR,

    exist_ok=True

)

# =============================================================================
# Load Application Dataset
# =============================================================================

print("=" * 80)
print("Loading Application Dataset...")
print("=" * 80)

application_df = pd.read_excel(

    APPLICATION_DATASET_PATH

)

print(

    f"Loaded {len(application_df)} applications."

)

print()

print("=" * 80)
print("Building Enterprise Application Analytics Dataset...")
print("=" * 80)

# =============================================================================
# Enterprise Risk Thresholds
# =============================================================================

LOW_RISK_THRESHOLD = 63

HIGH_RISK_THRESHOLD = 77

# =============================================================================
# Build Enterprise Analytics
# =============================================================================

print()

print("=" * 80)
print("Computing Enterprise Analytics...")
print("=" * 80)

analytics_records = []

for _, application in application_df.iterrows():

    # -------------------------------------------------------------------------
    # Identity
    # -------------------------------------------------------------------------

    application_id = application["Application ID"]

    application_name = application["Application Name"]

    department = application["Department"]

    # -------------------------------------------------------------------------
    # Observation Metrics
    # -------------------------------------------------------------------------

    total_observations = application["Total Observations"]

    high_count = application["High Count"]

    medium_count = application["Medium Count"]

    low_count = application["Low Count"]

    # -------------------------------------------------------------------------
    # Activity Counts
    # -------------------------------------------------------------------------

    itgc_count = application["ITGC Count"]

    database_count = application["Database Review Count"]

    dfra_count = application["DFRA Count"]

    dfa_count = application["DFA Count"]

    sna_count = application["SNA Count"]

    # -------------------------------------------------------------------------
    # Handle Divide-by-Zero
    # -------------------------------------------------------------------------

    if total_observations == 0:

        high_percentage = 0

        medium_percentage = 0

        low_percentage = 0

        itgc_percentage = 0

        database_percentage = 0

        dfra_percentage = 0

        dfa_percentage = 0

        sna_percentage = 0

        severity_index = 0

        risk_score = 0

    else:

        # ---------------------------------------------------------------------
        # Severity Analytics
        # ---------------------------------------------------------------------

        high_percentage = round(

            (high_count / total_observations) * 100,

            2

        )

        medium_percentage = round(

            (medium_count / total_observations) * 100,

            2

        )

        low_percentage = round(

            (low_count / total_observations) * 100,

            2

        )

        # ---------------------------------------------------------------------
        # Activity Analytics
        # ---------------------------------------------------------------------

        itgc_percentage = round(

            (itgc_count / total_observations) * 100,

            2

        )

        database_percentage = round(

            (database_count / total_observations) * 100,

            2

        )

        dfra_percentage = round(

            (dfra_count / total_observations) * 100,

            2

        )

        dfa_percentage = round(

            (dfa_count / total_observations) * 100,

            2

        )

        sna_percentage = round(

            (sna_count / total_observations) * 100,

            2

        )

        

        # ---------------------------------------------------------------------
        # Risk Score (0-100)
        # ---------------------------------------------------------------------

        severity_index = (
            (high_count * 3)
                +
            (medium_count * 2)
                +
            (low_count * 1)

        )
        maximum_possible_score = total_observations * 3
        risk_score = round(
            (severity_index / maximum_possible_score) * 100,
            2
        )

    # -------------------------------------------------------------------------
    # Risk Category
    # -------------------------------------------------------------------------

    if risk_score < LOW_RISK_THRESHOLD:

        risk_category = "Low"

    elif risk_score < HIGH_RISK_THRESHOLD :

        risk_category = "Medium"

    else:

        risk_category = "High"

    # -------------------------------------------------------------------------
    # Compliance Analytics
    # -------------------------------------------------------------------------

    compliance_percentage = round(

        100 - risk_score,

        2

    )

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
    # Explainable Risk Contribution
    # -------------------------------------------------------------------------

    if severity_index == 0:

        high_contribution = 0

        medium_contribution = 0

        low_contribution = 0

    else:

        high_contribution = round(

            ((high_count * 3) / severity_index) * 100,

            2

        )

        medium_contribution = round(

            ((medium_count * 2) / severity_index) * 100,

            2

        )

        low_contribution = round(

            ((low_count * 1) / severity_index) * 100,

            2

        )

    analytics_records.append({

        # Identity

        "Application ID": application_id,

        "Application Name": application_name,

        "Department": department,

        # Observation Metrics

        "Total Observations": total_observations,

        "High Count": high_count,

        "Medium Count": medium_count,

        "Low Count": low_count,

        # Observation %

        "High %": high_percentage,

        "Medium %": medium_percentage,

        "Low %": low_percentage,

        # Activity Counts

        "ITGC Count": itgc_count,

        "Database Count": database_count,

        "DFRA Count": dfra_count,

        "DFA Count": dfa_count,

        "SNA Count": sna_count,

        # Activity %

        "ITGC %": itgc_percentage,

        "Database %": database_percentage,

        "DFRA %": dfra_percentage,

        "DFA %": dfa_percentage,

        "SNA %": sna_percentage,

        # Risk Analytics

        "Severity Index": severity_index,

        "Risk Score": risk_score,

        "Risk Category": risk_category,

        # Compliance

        "Compliance %": compliance_percentage,

        "Compliance Grade": compliance_grade,

        # Executive

        "Executive Priority": executive_priority,

        # Explainable AI

        "High Risk Contribution %": high_contribution,

        "Medium Risk Contribution %": medium_contribution,

        "Low Risk Contribution %": low_contribution

    })

analytics_df = pd.DataFrame(

    analytics_records

)

print(

    f"Generated {len(analytics_df)} analytics records."

)

# =============================================================================
# Enterprise Risk Ranking
# =============================================================================

print()

print("=" * 80)
print("Computing Enterprise Risk Rankings...")
print("=" * 80)

analytics_df = (

    analytics_df

    .sort_values(

        by=[

            "Risk Score",

            "Severity Index",

            "High Count"

        ],

        ascending=False

    )

    .reset_index(drop=True)

)

analytics_df.insert(

    analytics_df.columns.get_loc(

        "Risk Score"

    ) + 2,

    "Risk Rank",

    range(

        1,

        len(analytics_df) + 1

    )

)

print(

    "Enterprise Risk Ranking completed."

)

# =============================================================================
# Dataset Validation
# =============================================================================

print()

print("=" * 80)
print("Validating Analytics Dataset...")
print("=" * 80)

# -------------------------------------------------------------------------
# Application Count
# -------------------------------------------------------------------------

assert (

    len(analytics_df)

    ==

    len(application_df)

), (

    "Application count mismatch."

)

# -------------------------------------------------------------------------
# Unique Application IDs
# -------------------------------------------------------------------------

assert (

    analytics_df["Application ID"].is_unique

), (

    "Duplicate Application IDs detected."

)

# -------------------------------------------------------------------------
# Missing Values
# -------------------------------------------------------------------------

assert (

    analytics_df.isnull().sum().sum()

    ==

    0

), (

    "Missing values detected."

)

# -------------------------------------------------------------------------
# Risk Score Validation
# -------------------------------------------------------------------------

assert (

    analytics_df["Risk Score"]

    .between(

        0,

        100

    )

    .all()

), (

    "Risk Score out of range."

)

# -------------------------------------------------------------------------
# Compliance Validation
# -------------------------------------------------------------------------

assert (

    analytics_df["Compliance %"]

    .between(

        0,

        100

    )

    .all()

), (

    "Compliance Percentage out of range."

)

# -------------------------------------------------------------------------
# Risk Rank Validation
# -------------------------------------------------------------------------

assert (

    analytics_df["Risk Rank"]

    .nunique()

    ==

    len(analytics_df)

), (

    "Duplicate Risk Ranks detected."

)

print(

    "Analytics Dataset validation completed successfully."

)

# =============================================================================
# Export Analytics Dataset
# =============================================================================

analytics_df.to_excel(

    APPLICATION_ANALYTICS_DATASET_PATH,

    index=False

)

print()

print(

    "Application Analytics Dataset exported successfully."

)

# =============================================================================
# Build Summary
# =============================================================================

print()

print("=" * 80)
print("BUILD SUMMARY")
print("=" * 80)

print(

    f"Applications Processed : {len(analytics_df)}"

)

print(

    f"High Risk Applications : "

    f"{(analytics_df['Risk Category'] == 'High').sum()}"

)

print(

    f"Medium Risk Applications : "

    f"{(analytics_df['Risk Category'] == 'Medium').sum()}"

)

print(

    f"Low Risk Applications : "

    f"{(analytics_df['Risk Category'] == 'Low').sum()}"

)

print()

print(

    f"Highest Risk Score : "

    f"{analytics_df['Risk Score'].max()}"

)

print(

    f"Average Risk Score : "

    f"{round(analytics_df['Risk Score'].mean(),2)}"

)

print(

    f"Average Compliance : "

    f"{round(analytics_df['Compliance %'].mean(),2)}%"

)

print("=" * 80)