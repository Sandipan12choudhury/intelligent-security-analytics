"""
==============================================================================
Department Analytics Dataset Builder

Purpose
-------
Builds the Enterprise Department Analytics Dataset.

This builder aggregates the Application Analytics Dataset into
department-level analytics for:

    • Enterprise Dashboard
    • Department Dashboard
    • Executive Reporting
    • AI Intelligence Engine
    • Machine Learning Engine

Input
-----
application_analytics_dataset.xlsx

Output
------
department_analytics_dataset.xlsx

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

APPLICATION_ANALYTICS_DATASET_PATH = (

    DATASET_DIR /

    "application_analytics_dataset.xlsx"

)

DEPARTMENT_ANALYTICS_DATASET_PATH = (

    DATASET_DIR /

    "department_analytics_dataset.xlsx"

)

os.makedirs(

    DATASET_DIR,

    exist_ok=True

)

# =============================================================================
# Load Application Analytics Dataset
# =============================================================================

print("=" * 80)
print("Loading Application Analytics Dataset...")
print("=" * 80)

application_df = pd.read_excel(

    APPLICATION_ANALYTICS_DATASET_PATH

)

print(

    f"Loaded {len(application_df)} applications."

)

print()

print("=" * 80)
print("Building Enterprise Department Analytics Dataset...")
print("=" * 80)

# =============================================================================
# Enterprise Risk Thresholds
# =============================================================================

LOW_RISK_THRESHOLD = 63

HIGH_RISK_THRESHOLD = 77

# =============================================================================
# Build Department Analytics
# =============================================================================

print()

print("=" * 80)
print("Computing Department Analytics...")
print("=" * 80)

department_records = []

# =============================================================================
# Process Each Department
# =============================================================================

for department in sorted(application_df["Department"].unique()):

    department_df = (

        application_df[

            application_df["Department"] == department

        ]

        .copy()

        .reset_index(drop=True)

    )

    # -------------------------------------------------------------------------
    # Coverage
    # -------------------------------------------------------------------------

    application_count = len(

        department_df

    )

    total_observations = int(

        department_df["Total Observations"]

        .sum()

    )

    # -------------------------------------------------------------------------
    # Severity Counts
    # -------------------------------------------------------------------------

    high_count = int(

        department_df["High Count"]

        .sum()

    )

    medium_count = int(

        department_df["Medium Count"]

        .sum()

    )

    low_count = int(

        department_df["Low Count"]

        .sum()

    )

    # -------------------------------------------------------------------------
    # Severity Percentages
    # -------------------------------------------------------------------------

    if total_observations == 0:

        high_percentage = 0

        medium_percentage = 0

        low_percentage = 0

    else:

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

    # -------------------------------------------------------------------------
    # Activity Counts
    # -------------------------------------------------------------------------

    itgc_count = int(

        department_df["ITGC Count"]

        .sum()

    )

    database_count = int(

        department_df["Database Count"]

        .sum()

    )

    dfra_count = int(

        department_df["DFRA Count"]

        .sum()

    )

    dfa_count = int(

        department_df["DFA Count"]

        .sum()

    )

    sna_count = int(

        department_df["SNA Count"]

        .sum()

    )

    # -------------------------------------------------------------------------
    # Activity Percentages
    # -------------------------------------------------------------------------

    if total_observations == 0:

        itgc_percentage = 0

        database_percentage = 0

        dfra_percentage = 0

        dfa_percentage = 0

        sna_percentage = 0

    else:

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

    # -------------------------------------------------------------------------
    # Risk Analytics
    # -------------------------------------------------------------------------

    average_risk_score = round(

        department_df["Risk Score"]

        .mean(),

        2

    )

    highest_risk_score = round(

        department_df["Risk Score"]

        .max(),

        2

    )

    lowest_risk_score = round(

        department_df["Risk Score"]

        .min(),

        2

    )

    # -------------------------------------------------------------------------
    # Compliance Analytics
    # -------------------------------------------------------------------------

    average_compliance = round(

        department_df["Compliance %"]

        .mean(),

        2

    )

    # -------------------------------------------------------------------------
    # Compliance Grade
    # -------------------------------------------------------------------------

    if average_compliance >= 90:

        compliance_grade = "A"

    elif average_compliance >= 80:

        compliance_grade = "B"

    elif average_compliance >= 70:

        compliance_grade = "C"

    elif average_compliance >= 60:

        compliance_grade = "D"

    else:

        compliance_grade = "F"

    # -------------------------------------------------------------------------
    # Department Risk Category
    # -------------------------------------------------------------------------

    if average_risk_score < LOW_RISK_THRESHOLD:

        department_risk_category = "Low"

    elif average_risk_score < HIGH_RISK_THRESHOLD:

        department_risk_category = "Medium"

    else:

        department_risk_category = "High"

    # -------------------------------------------------------------------------
    # Executive Priority
    # -------------------------------------------------------------------------

    if average_risk_score >= 85:

        executive_priority = "Critical"

    elif average_risk_score >= 70:

        executive_priority = "High"

    elif average_risk_score >= 40:

        executive_priority = "Medium"

    else:

        executive_priority = "Low"

    # -------------------------------------------------------------------------
    # Highest & Lowest Risk Applications
    # -------------------------------------------------------------------------

    highest_application = (

        department_df

        .sort_values(

            "Risk Score",

            ascending=False

        )

        .iloc[0]

    )

    lowest_application = (

        department_df

        .sort_values(

            "Risk Score",

            ascending=True

        )

        .iloc[0]

    )

    # -------------------------------------------------------------------------
    # Top 3 Risk Applications
    # -------------------------------------------------------------------------

    top_three = (

        department_df

        .sort_values(

            "Risk Score",

            ascending=False

        )

        .head(3)

        .reset_index(drop=True)

    )

    # -------------------------------------------------------------------------
    # Ensure Three Records Always Exist
    # -------------------------------------------------------------------------

    while len(top_three) < 3:

        top_three.loc[len(top_three)] = top_three.iloc[-1]

    # -------------------------------------------------------------------------
    # Dominant Severity
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

    # -------------------------------------------------------------------------
    # Top Activity
    # -------------------------------------------------------------------------

    activity_dictionary = {
        "ITGC": itgc_percentage,
        "Database": database_percentage,
        "DFRA": dfra_percentage,
        "DFA": dfa_percentage,
        "SNA": sna_percentage
    }
    
    top_activity = max(
        activity_dictionary,
        key=activity_dictionary.get
    )
    
    top_activity_percentage = round(
        activity_dictionary[top_activity],
        2
    )

    # -------------------------------------------------------------------------
    # Store Department Analytics
    # -------------------------------------------------------------------------

    department_records.append({

        # Identity

        "Department": department,

        # Coverage

        "Applications": application_count,

        "Total Observations": total_observations,

        # Severity Counts

        "High Count": high_count,

        "Medium Count": medium_count,

        "Low Count": low_count,

        # Severity %

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

        # Risk

        "Average Risk Score": average_risk_score,

        "Highest Risk Score": highest_risk_score,

        "Lowest Risk Score": lowest_risk_score,

        "Risk Category": department_risk_category,

        # Compliance

        "Average Compliance %": average_compliance,

        "Compliance Grade": compliance_grade,

        # Executive

        "Executive Priority": executive_priority,

        # Highest Risk Application

        "Highest Risk Application ID":

            highest_application["Application ID"],

        "Highest Risk Application Name":

            highest_application["Application Name"],

        # Lowest Risk Application

        "Lowest Risk Application ID":

            lowest_application["Application ID"],

        "Lowest Risk Application Name":

            lowest_application["Application Name"],

        # Top 3 Applications

        "Top 1 Application ID":

            top_three.iloc[0]["Application ID"],

        "Top 1 Application Name":

            top_three.iloc[0]["Application Name"],

        "Top 2 Application ID":

            top_three.iloc[1]["Application ID"],

        "Top 2 Application Name":

            top_three.iloc[1]["Application Name"],

        "Top 3 Application ID":

            top_three.iloc[2]["Application ID"],

        "Top 3 Application Name":

            top_three.iloc[2]["Application Name"],

        # Analytics Metadata

        "Top Activity": top_activity,
        "Top Activity %": top_activity_percentage,
        "Dominant Severity": dominant_severity,
        "Dominant Severity %": dominant_severity_percentage


    })

print()

print(

    f"Generated {len(department_records)} department analytics records."

)

# =============================================================================
# Create Department Analytics DataFrame
# =============================================================================

department_analytics_df = pd.DataFrame(

    department_records

)

# =============================================================================
# Enterprise Department Ranking
# =============================================================================

print()

print("=" * 80)
print("Computing Enterprise Department Rankings...")
print("=" * 80)

department_analytics_df = (

    department_analytics_df

    .sort_values(

        by="Average Risk Score",

        ascending=False

    )

    .reset_index(drop=True)

)

department_analytics_df.insert(

    0,

    "Department Rank",

    range(

        1,

        len(department_analytics_df) + 1

    )

)

print(

    "Enterprise Department Ranking completed."

)

# =============================================================================
# Validate Department Analytics Dataset
# =============================================================================

print()

print("=" * 80)
print("Validating Department Analytics Dataset...")
print("=" * 80)

# -------------------------------------------------------------------------
# Validate Record Count
# -------------------------------------------------------------------------

assert (

    len(department_analytics_df)

    ==

    application_df["Department"].nunique()

), (

    "Department count mismatch."

)

# -------------------------------------------------------------------------
# Validate Unique Departments
# -------------------------------------------------------------------------

assert (

    department_analytics_df["Department"].is_unique

), (

    "Duplicate departments detected."

)

# -------------------------------------------------------------------------
# Validate Missing Values
# -------------------------------------------------------------------------

assert (

    department_analytics_df.isnull().sum().sum()

    ==

    0

), (

    "Missing values detected."

)

# -------------------------------------------------------------------------
# Validate Observation Aggregation
# -------------------------------------------------------------------------

assert (

    department_analytics_df["Total Observations"]

    .sum()

    ==

    application_df["Total Observations"]

    .sum()

), (

    "Observation aggregation mismatch."

)

print(

    "Department Analytics Dataset validation completed successfully."

)

# =============================================================================
# Export Department Analytics Dataset
# =============================================================================

department_analytics_df.to_excel(

    DEPARTMENT_ANALYTICS_DATASET_PATH,

    index=False

)

print()

print(

    "Department Analytics Dataset exported successfully."

)

# =============================================================================
# Build Summary
# =============================================================================

print()

print("=" * 80)
print("BUILD SUMMARY")
print("=" * 80)

print(

    f"Departments Processed : {len(department_analytics_df)}"

)

print(

    f"Applications Aggregated : "

    f"{department_analytics_df['Applications'].sum()}"

)

print(

    f"Observations Aggregated : "

    f"{department_analytics_df['Total Observations'].sum()}"

)

print(

    f"Highest Risk Department : "

    f"{department_analytics_df.iloc[0]['Department']}"

)

print(

    f"Highest Department Risk : "

    f"{department_analytics_df['Average Risk Score'].max()}"

)

print(

    f"Average Department Risk : "

    f"{round(department_analytics_df['Average Risk Score'].mean(),2)}"

)

print("=" * 80)