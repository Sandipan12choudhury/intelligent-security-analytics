"""
=============================================================
Database User & Access Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Database User & Access Management
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

DOMAIN = "Database User & Access Management"
ACTIVITY = "Database"

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
# Database User & Access Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database user administration identified that privileged database accounts were assigned directly to individual users without implementation of centralized identity management controls. Decentralized user administration increases the risk of inconsistent access governance and unauthorized privileged access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database authentication identified that privileged database accounts authenticated using locally managed passwords instead of enterprise-approved centralized authentication mechanisms. Weak authentication controls increase the risk of unauthorized database access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database access governance identified that periodic recertification of privileged database users had not been performed in accordance with the Enterprise Database Access Management Standard. Failure to periodically review privileged access increases the likelihood of excessive database privileges remaining active.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database service account management identified that service accounts were configured with interactive login privileges without documented business justification. Interactive service account usage increases the risk of unauthorized database access and privilege misuse.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged database accounts identified shared administrative database accounts used by multiple personnel without implementation of individual accountability or session attribution controls. Shared privileged accounts reduce accountability and hinder forensic investigations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database role management identified that privileged roles granting unrestricted database administration capabilities were assigned without documented business approval or role-based access justification. Excessive privilege assignment increases the likelihood of unauthorized database modifications.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database account lifecycle management identified that database accounts belonging to transferred or separated personnel remained active beyond approved de-provisioning timelines. Delayed account removal increases the risk of unauthorized database access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database governance identified that high-risk database access exceptions remained active beyond approved review timelines without documented risk acceptance or compensating security controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database user inventory identified that ownership information for privileged database accounts was not consistently maintained within the centralized database access inventory.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database account management identified that dormant database accounts were not periodically identified and disabled in accordance with the Enterprise Database Access Management Standard.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database access reviews identified that business owners were not consistently involved in periodic validation of privileged database access rights.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database authentication identified that failed database authentication attempts were not periodically analyzed to identify potential brute-force attacks or unauthorized access attempts.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database privilege management identified that database roles and privileges were not periodically reviewed to verify compliance with the principle of least privilege.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of service account governance identified that passwords associated with database service accounts were not periodically rotated in accordance with enterprise password management requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Database User & Access Management governance identified that the Enterprise Database Access Management Standard had not undergone periodic review to address evolving database technologies, regulatory expectations and emerging security threats.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database access reviews identified that privileged database accounts assigned to third-party vendors had not undergone periodic recertification following completion of contracted activities. Failure to review vendor database access increases the risk of unauthorized privileged access remaining active.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database authentication identified that password policies enforced for database accounts were not consistently aligned with the organization's Enterprise Password Management Standard, resulting in inconsistent authentication controls across database platforms.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database account governance identified that orphaned database accounts with no identifiable business owner remained active within production database instances. Orphan accounts reduce accountability and increase the likelihood of unauthorized database access.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of privileged database administration identified that emergency database administrator access was not periodically reviewed to validate appropriate usage and timely revocation following completion of emergency activities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database role management identified that custom database roles accumulated privileges over time without periodic rationalization, increasing the risk of excessive database permissions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database service account management identified that service account ownership was not periodically reviewed to confirm continued business necessity and accountable ownership.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database user provisioning identified that newly created privileged database accounts were not independently verified following account creation to ensure assigned privileges matched approved access requests.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database access governance identified that segregation of duties conflicts involving privileged database roles were not periodically identified or assessed through formal access governance reviews.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database user documentation identified that database account ownership, purpose and associated business applications were not consistently maintained within the centralized database access repository.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing privileged database users, dormant accounts, access recertification status and unresolved database access risks were not periodically presented to Database Administration and Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Database User & Access Management procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Database User & Access Management documentation identified absence of version-controlled database access standards aligned with the current enterprise database landscape and regulatory requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that database administrators and database custodians were not periodically provided awareness training on enterprise database access governance, privileged account management and least privilege principles.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Database User & Access Management activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Database User & Access Management Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("Database User & Access Management Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")