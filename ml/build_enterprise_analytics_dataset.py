"""
==============================================================================
Enterprise Analytics Dataset Builder

Purpose
-------
Builds the Enterprise Analytics Dataset.

This builder aggregates the Department Analytics Dataset into a
single enterprise-wide analytics record.

The dataset powers:

    • Executive Dashboard
    • Enterprise Dashboard
    • AI Intelligence Engine
    • Executive Reporting
    • Machine Learning Engine

Input
-----
department_analytics_dataset.xlsx

Output
------
enterprise_analytics_dataset.xlsx

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

DEPARTMENT_ANALYTICS_DATASET_PATH = (

    DATASET_DIR /

    "department_analytics_dataset.xlsx"

)

ENTERPRISE_ANALYTICS_DATASET_PATH = (

    DATASET_DIR /

    "enterprise_analytics_dataset.xlsx"

)

os.makedirs(

    DATASET_DIR,

    exist_ok=True

)

# =============================================================================
# Enterprise Configuration
# =============================================================================

ENTERPRISE_NAME = "State Bank of India"

LOW_RISK_THRESHOLD = 63

HIGH_RISK_THRESHOLD = 77

# =============================================================================
# Load Department Analytics Dataset
# =============================================================================

print("=" * 80)
print("Loading Department Analytics Dataset...")
print("=" * 80)

department_df = pd.read_excel(

    DEPARTMENT_ANALYTICS_DATASET_PATH

)

print(

    f"Loaded {len(department_df)} departments."

)

print()

print("=" * 80)
print("Building Enterprise Analytics Dataset...")
print("=" * 80)


# =============================================================================
# Compute Enterprise Analytics
# =============================================================================

print()

print("=" * 80)
print("Computing Enterprise Analytics...")
print("=" * 80)

# =============================================================================
# Enterprise Coverage
# =============================================================================

department_count = len(

    department_df

)

application_count = int(

    department_df["Applications"]

    .sum()

)

total_observations = int(

    department_df["Total Observations"]

    .sum()

)

# =============================================================================
# Severity Counts
# =============================================================================

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

# =============================================================================
# Severity Percentages
# =============================================================================

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

# =============================================================================
# Activity Counts
# =============================================================================

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

# =============================================================================
# Activity Percentages
# =============================================================================

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

# =============================================================================
# Enterprise Risk Analytics
# =============================================================================

average_risk_score = round(

    department_df["Average Risk Score"]

    .mean(),

    2

)

highest_risk_score = round(

    department_df["Average Risk Score"]

    .max(),

    2

)

lowest_risk_score = round(

    department_df["Average Risk Score"]

    .min(),

    2

)

# =============================================================================
# Enterprise Compliance
# =============================================================================

average_compliance = round(

    department_df["Average Compliance %"]

    .mean(),

    2

)

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

# =============================================================================
# Enterprise Risk Category
# =============================================================================

if average_risk_score < LOW_RISK_THRESHOLD:

    enterprise_risk_category = "Low"

elif average_risk_score < HIGH_RISK_THRESHOLD:

    enterprise_risk_category = "Medium"

else:

    enterprise_risk_category = "High"


# =============================================================================
# Executive Analytics
# =============================================================================

print()

print("=" * 80)
print("Computing Executive Analytics...")
print("=" * 80)

# -----------------------------------------------------------------------------
# Highest & Lowest Risk Departments
# -----------------------------------------------------------------------------

highest_department = (

    department_df

    .sort_values(

        "Average Risk Score",

        ascending=False

    )

    .iloc[0]

)

lowest_department = (

    department_df

    .sort_values(

        "Average Risk Score",

        ascending=True

    )

    .iloc[0]

)

# -----------------------------------------------------------------------------
# Top 3 Risk Departments
# -----------------------------------------------------------------------------

top_three_departments = (

    department_df

    .sort_values(

        "Average Risk Score",

        ascending=False

    )

    .head(3)

    .reset_index(drop=True)

)

while len(top_three_departments) < 3:

    top_three_departments.loc[

        len(top_three_departments)

    ] = top_three_departments.iloc[-1]

# -----------------------------------------------------------------------------
# Top Activity
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# Dominant Severity
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# Executive Priority
# -----------------------------------------------------------------------------

if average_risk_score >= 85:

    executive_priority = "Critical"

elif average_risk_score >= 70:

    executive_priority = "High"

elif average_risk_score >= 40:

    executive_priority = "Medium"

else:

    executive_priority = "Low"

# =============================================================================
# Create Enterprise Analytics Dataset
# =============================================================================

enterprise_analytics_df = pd.DataFrame([{

    # Identity

    "Enterprise Name": ENTERPRISE_NAME,

    # Coverage

    "Departments": department_count,

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

    # Enterprise Risk

    "Average Risk Score": average_risk_score,

    "Highest Department Risk": highest_risk_score,

    "Lowest Department Risk": lowest_risk_score,

    "Risk Category": enterprise_risk_category,

    # Compliance

    "Average Compliance %": average_compliance,

    "Compliance Grade": compliance_grade,

    # Executive Analytics

    "Highest Risk Department":

        highest_department["Department"],

    "Highest Risk Department Rank":

        highest_department["Department Rank"],

    "Lowest Risk Department":

        lowest_department["Department"],

    "Lowest Risk Department Rank":

        lowest_department["Department Rank"],

    "Top 1 Department":

        top_three_departments.iloc[0]["Department"],

    "Top 2 Department":

        top_three_departments.iloc[1]["Department"],

    "Top 3 Department":

        top_three_departments.iloc[2]["Department"],

    "Executive Priority":

        executive_priority,

    # Metadata

    "Top Activity":

        top_activity,

    "Top Activity %":

        top_activity_percentage,

    "Dominant Severity":

        dominant_severity,

    "Dominant Severity %":

        dominant_severity_percentage

}])

print(

    "Enterprise Analytics Record created successfully."

)

# =============================================================================
# Validate Enterprise Analytics Dataset
# =============================================================================

print()

print("=" * 80)
print("Validating Enterprise Analytics Dataset...")
print("=" * 80)

assert len(enterprise_analytics_df) == 1, (

    "Enterprise record count mismatch."

)

assert enterprise_analytics_df.isnull().sum().sum() == 0, (

    "Missing values detected."

)

assert (

    enterprise_analytics_df["Applications"].iloc[0]

    ==

    department_df["Applications"].sum()

), (

    "Application aggregation mismatch."

)

assert (

    enterprise_analytics_df["Total Observations"].iloc[0]

    ==

    department_df["Total Observations"].sum()

), (

    "Observation aggregation mismatch."

)

print(

    "Enterprise Analytics Dataset validation completed successfully."

)

# =============================================================================
# Export Enterprise Analytics Dataset
# =============================================================================

enterprise_analytics_df.to_excel(

    ENTERPRISE_ANALYTICS_DATASET_PATH,

    index=False

)

print()

print(

    "Enterprise Analytics Dataset exported successfully."

)

# =============================================================================
# Build Summary
# =============================================================================

print()

print("=" * 80)
print("BUILD SUMMARY")
print("=" * 80)

print(

    f"Departments Aggregated : {department_count}"

)

print(

    f"Applications Aggregated : {application_count}"

)

print(

    f"Observations Aggregated : {total_observations}"

)

print(

    f"Enterprise Risk Score : {average_risk_score}"

)

print(

    f"Enterprise Compliance : {average_compliance}%"

)

print(

    f"Highest Risk Department : "

    f"{highest_department['Department']}"

)

print("=" * 80)