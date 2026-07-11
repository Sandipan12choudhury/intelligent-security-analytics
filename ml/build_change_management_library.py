"""
=============================================================
Change Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Change Management observations
into the central Observation Repository.

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

DOMAIN = "Change Management"
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
# Change Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of submitted Change Request records identified that production changes were implemented without approved Change Requests. Absence of formal change authorization increases the risk of unauthorized system modifications and service disruption.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of change approval evidences identified that multiple production changes were deployed without documented approval from the designated Change Advisory Board (CAB). Lack of CAB approval weakens governance over production change implementation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Examination of impact assessment documentation identified that business and technical impact analyses were not performed prior to implementation of production changes. Inadequate impact assessment increases the likelihood of unintended service disruption.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of User Acceptance Testing (UAT) evidences identified that production deployments were completed without documented UAT sign-off from business stakeholders. Deployment of unvalidated changes may adversely impact application availability and business operations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of rollback planning documentation identified that rollback procedures were not prepared or tested prior to implementation of production changes. Absence of rollback capability may prolong service outages during unsuccessful deployments.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of emergency change records identified that emergency production changes were implemented without subsequent management review and retrospective approval. Inadequate governance over emergency changes increases operational and security risks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Examination of production deployment evidences identified that the same individual performed change development, testing and production deployment activities. Lack of segregation of duties increases the risk of unauthorized or erroneous system changes.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of change implementation records identified that production changes were deployed outside approved maintenance windows without documented business justification or management approval.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of change documentation identified that supporting implementation procedures were not consistently attached to approved Change Requests.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of risk assessment reports identified that change-related risks were not formally evaluated prior to implementation of production changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of Change Request records identified that change classification as Standard, Normal or Emergency was not consistently documented.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of change schedules identified that production deployment calendars were not periodically reviewed to identify conflicting or overlapping changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of change testing evidences identified that test cases did not adequately cover security-related functionality impacted by the implemented change.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of implementation records identified that actual deployment activities were not consistently reconciled with the approved implementation plan.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of change governance identified that periodic review of pending and overdue Change Requests was not evidenced.",
        "Severity": "Medium"
    },
    
        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Change Advisory Board (CAB) meeting records identified that CAB decisions were not consistently documented for production changes implemented during the review period.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of emergency change documentation identified that root cause analysis was not performed following implementation of emergency production changes. Absence of post-implementation analysis limits continuous process improvement.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of production deployment evidences identified that implementation success criteria were not formally defined prior to deployment of production changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of rollback validation records identified that rollback procedures were documented but had not been periodically tested under representative production conditions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of change implementation records identified that post-implementation validation activities were not consistently performed to confirm successful deployment and expected system behaviour.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of production deployment logs identified that implementation timestamps were not consistently reconciled with approved deployment schedules.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Change Request records identified that dependencies between related production changes were not evaluated prior to implementation, increasing the risk of service interruption.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of implementation evidences identified that infrastructure changes and corresponding application changes were not coordinated through a unified Change Management process.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of production change reports identified that failed deployment statistics and change success rates were not periodically analysed for trend identification and process improvement.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Change Management governance identified that Key Performance Indicators (KPIs) for change success, rollback frequency and emergency changes were not periodically reported to management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of Change Management procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Change Management documentation identified absence of version-controlled procedures aligned with current organizational Change Management practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of awareness records identified that personnel involved in Change Management activities were not periodically provided training on approved change governance requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of Change Management reporting identified that periodic management dashboards summarizing change implementation trends and governance metrics were not available for review.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Change Management governance identified that periodic internal quality assurance reviews over Change Management activities were not evidenced.",
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
print("Change Management Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")

print(f"Existing Observations   : {existing_count}")

print(f"New Observations        : {len(new_df)}")

print(f"Duplicates Removed      : {duplicates_removed}")

print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")