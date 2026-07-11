"""
=============================================================
Business Continuity & Disaster Recovery Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Business Continuity & Disaster Recovery
observations into the central Observation Repository.

Repository:
dataset/observation_library.xlsx

Author:
B.Tech Major Project
Intelligent Security Analytics
=============================================================
"""

import pandas as pd
from pathlib import Path


# ============================================================
# Configuration
# ============================================================

DOMAIN = "Business Continuity & Disaster Recovery"
ACTIVITY = "ITGC"

ROOT_DIR = Path(__file__).resolve().parent.parent

DATASET_FILE = ROOT_DIR / "dataset" / "observation_library.xlsx"


# ============================================================
# Repository Validation
# ============================================================

if not DATASET_FILE.exists():

    raise FileNotFoundError(

        "\nObservation Repository not found.\n\n"
        "Please execute:\n"
        "build_user_management_library.py\n"
        "before running this script."

    )


# ============================================================
# Load Repository
# ============================================================

existing_df = pd.read_excel(DATASET_FILE)

existing_count = len(existing_df)


# ============================================================
# Business Continuity & Disaster Recovery Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Business Continuity Plan (BCP) documentation identified that the approved BCP had not undergone periodic review and update following significant changes to the application architecture and supporting infrastructure. Outdated continuity plans may adversely impact recovery during disruptive events.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Disaster Recovery (DR) testing records identified that annual Disaster Recovery exercises were not performed for critical production applications as required under the approved Business Continuity framework. Absence of periodic DR testing reduces assurance over organizational recovery capability.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Business Impact Analysis (BIA) documentation identified that Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) had not been formally reviewed following implementation of major production changes. Outdated recovery objectives may result in ineffective disaster recovery planning.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of Disaster Recovery infrastructure identified that critical production servers were not replicated to the designated Disaster Recovery site in accordance with the approved Disaster Recovery strategy. Failure to maintain synchronized recovery infrastructure may delay restoration of critical business services.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of Disaster Recovery failover records identified that failover procedures for critical applications had not been validated through end-to-end recovery testing. Unvalidated failover procedures may increase recovery time during an actual disaster scenario.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of Disaster Recovery governance identified that production databases were not consistently replicated to the Disaster Recovery environment, increasing the risk of data loss during major service disruptions.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of crisis management procedures identified that responsibilities of Business Continuity and Disaster Recovery response teams were not clearly defined or periodically communicated. Lack of clearly assigned responsibilities may delay coordinated response during business disruptions.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Disaster Recovery exception records identified that unresolved deficiencies observed during previous DR drills remained open beyond approved remediation timelines without documented risk acceptance or management approval.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Business Impact Analysis records identified that critical business processes supporting the application were not periodically reassessed to validate business criticality.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Disaster Recovery documentation identified that application dependency mapping required for recovery planning was incomplete for multiple production services.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of Disaster Recovery test reports identified that recovery validation focused only on infrastructure restoration without verification of complete business functionality.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of Business Continuity governance identified that alternate communication procedures for business disruption scenarios were not periodically validated.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of Disaster Recovery readiness identified that recovery procedures for newly deployed production applications were not incorporated into the approved Disaster Recovery documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Disaster Recovery infrastructure identified that periodic health verification of standby infrastructure supporting Disaster Recovery operations was not evidenced.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Business Continuity governance identified that periodic management review of Business Continuity risks and recovery readiness was not evidenced.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Disaster Recovery testing records identified that Recovery Time Objectives (RTOs) achieved during Disaster Recovery drills were not compared against approved business recovery targets to validate recovery readiness.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Recovery Point Objective (RPO) validation identified that data synchronization between the primary and Disaster Recovery environments was not periodically verified to ensure compliance with approved recovery objectives.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Disaster Recovery exercise reports identified that critical application dependencies on external service providers were not included within Disaster Recovery testing scenarios, reducing confidence in end-to-end recovery capability.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of Business Continuity governance identified that periodic awareness and simulation exercises for business users were not conducted to familiarize personnel with continuity procedures during disruptive events.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of Disaster Recovery failback procedures identified that restoration of production services following Disaster Recovery activation had not been periodically tested and documented.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of Business Continuity documentation identified that contact information for crisis management teams, application owners and external stakeholders was not periodically reviewed for accuracy.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Disaster Recovery governance identified that findings observed during Disaster Recovery exercises were not subjected to Root Cause Analysis (RCA) and formal corrective action tracking.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Business Continuity monitoring identified that Key Risk Indicators (KRIs) relating to recovery readiness and continuity capability were not periodically monitored or reported.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of Disaster Recovery readiness identified that supporting infrastructure including DNS, authentication services and network connectivity required for recovery operations was not validated during Disaster Recovery exercises.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that periodic dashboards summarizing Business Continuity and Disaster Recovery readiness, testing outcomes and open remediation items were not presented to senior management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Business Continuity & Disaster Recovery procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Business Continuity documentation identified absence of version-controlled Business Continuity and Disaster Recovery plans aligned with the current enterprise application landscape.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that personnel assigned Business Continuity and Disaster Recovery responsibilities were not periodically provided awareness training and recovery simulation exercises.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Business Continuity and Disaster Recovery activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Business Continuity and Disaster Recovery Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
        "Severity": "Low"
    }

]

# ============================================================
# CREATE DATAFRAME
# ============================================================

new_df = pd.DataFrame(OBSERVATIONS)

# ============================================================
# APPEND TO EXISTING REPOSITORY
# ============================================================

combined_df = pd.concat(
    [existing_df, new_df],
    ignore_index=True
)

before_dedup = len(combined_df)

combined_df = combined_df.drop_duplicates(
    subset=[
        "Activity",
        "Domain",
        "Observation"
    ],
    keep="first"
)

duplicates_removed = before_dedup - len(combined_df)

combined_df = combined_df.sort_values(
    by=[
        "Activity",
        "Domain"
    ]
).reset_index(drop=True)

# ============================================================
# SAVE UPDATED REPOSITORY
# ============================================================

combined_df.to_excel(
    DATASET_FILE,
    index=False
)

# ============================================================
# EXECUTION SUMMARY
# ============================================================

print("\n===================================================")
print("Business Continuity & Disaster Recovery Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")