"""
=============================================================
Privileged Access Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Privileged Access Management (PAM)
observations into the central Observation Repository.

Repository:
dataset/observation_library.xlsx

This script DOES NOT overwrite the repository.

It performs:

1. Load existing repository
2. Generate PAM observations
3. Append new observations
4. Remove duplicates
5. Save updated repository

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

DOMAIN = "Privileged Access Management"
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
# Load Existing Repository
# ============================================================

existing_df = pd.read_excel(DATASET_FILE)

existing_count = len(existing_df)


# ============================================================
# PAM Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account inventory identified that a comprehensive inventory of administrative accounts was not maintained for the application environment. Absence of a complete privileged account inventory increases the risk of unmanaged administrative access remaining undetected.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access review records identified that periodic recertification of administrative accounts was not performed in accordance with organizational access governance requirements. Lack of periodic review may result in excessive privileged access remaining active.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access approval records identified that privileged accounts were provisioned without documented management approval and business justification. Unauthorized assignment of administrative privileges increases the likelihood of privilege misuse.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account management identified that shared administrative accounts were utilized for operational activities instead of individually assigned privileged identities. Shared privileged credentials reduce user accountability and hinder forensic investigations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of emergency privileged access procedures identified that break-glass administrative accounts were not periodically reviewed and monitored. Inadequate governance over emergency accounts increases the risk of unauthorized privileged activities.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged credential management identified that privileged account passwords were not stored within an approved privileged access management solution. Unprotected privileged credentials increase exposure to unauthorized disclosure.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged session monitoring identified that activities performed using administrative accounts were not recorded or monitored. Absence of privileged session monitoring limits accountability and security investigation capability.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account lifecycle management identified that privileged access assigned to transferred or terminated personnel was not revoked within defined timelines. Delayed de-provisioning increases the risk of unauthorized administrative access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged role assignments identified that administrative privileges exceeded business requirements for several privileged users. Excessive privileges violate the principle of least privilege and increase operational risk.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access governance identified that documented ownership of privileged accounts was not formally assigned for all administrative identities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access procedures identified that periodic validation of privileged account necessity was not performed for application support personnel.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account configuration identified that privileged access was granted through permanent assignments instead of time-bound privileged elevation mechanisms.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access governance identified absence of documented approval for privileged access extensions beyond approved validity periods.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account monitoring identified that unsuccessful privileged authentication attempts were not periodically reviewed for suspicious activity.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account administration identified that generic privileged IDs continued to exist within the production environment without documented business justification.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account review records identified that privileged access granted to third-party support personnel was not periodically validated against approved business requirements. Lack of periodic review may result in unnecessary privileged access remaining active.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged credential rotation procedures identified that passwords associated with administrative accounts were not rotated in accordance with organizational password management requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access request records identified that emergency privileged access requests were not supported by documented post-access management review and approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged session monitoring identified that privileged administrative commands executed within the production environment were not retained for independent security review.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access governance identified that privileged account owners were not required to periodically certify continued business necessity for elevated access.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account administration identified that dormant privileged accounts remained enabled beyond the organization's approved inactivity threshold.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access monitoring identified that privileged account activities were not integrated with centralized security monitoring mechanisms for continuous oversight.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account governance identified that administrative role assignments were not periodically compared against current job responsibilities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account administration identified that segregation between privileged administrative accounts and standard user accounts was not consistently implemented for all administrators.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access procedures identified that privileged account creation and deletion activities were not independently reviewed by application management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access governance documentation identified that periodic reporting of privileged account metrics to senior management was not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account procedures identified that documented operational guidelines for privileged account administration were not periodically reviewed and approved.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access documentation identified absence of version-controlled privileged access management procedures aligned with organizational security standards.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged account awareness activities identified that administrators were not periodically provided awareness training regarding privileged access management responsibilities.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of privileged access governance identified that periodic management reporting over privileged account compliance trends was not available for review.",
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
print("Privileged Access Management Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")

print(f"Existing Observations   : {existing_count}")

print(f"New Observations        : {len(new_df)}")

print(f"Duplicates Removed      : {duplicates_removed}")

print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")