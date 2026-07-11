"""
=============================================================
Database Configuration & Hardening Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Database Configuration & Hardening
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

DOMAIN = "Database Configuration & Hardening"
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
# Database Configuration & Hardening Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of production database configurations identified that database instances were not configured in accordance with the approved Enterprise Database Hardening Standard. Deviations from secure configuration baselines increase exposure to known database security weaknesses and unauthorized system modifications.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database configuration identified that default database accounts and sample schemas remained enabled within production database instances without documented business justification. Default components increase the attack surface and may be exploited by unauthorized users.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database configuration parameters identified that authentication, password and account lockout settings were not consistently configured in accordance with approved enterprise security standards across production database instances.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database services identified that unnecessary database features, optional services and legacy components remained enabled within production environments without documented business requirements. Unused services increase the overall database attack surface.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database network configuration identified that database listener configurations permitted connections from unauthorized network locations contrary to the approved Enterprise Database Security Standard. Inadequate listener restrictions increase the risk of unauthorized database access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database hardening identified that production database instances contained insecure configuration parameters inherited from default software installations without formal security review or approval.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database configuration governance identified that deviations from approved database hardening baselines remained unresolved beyond approved remediation timelines without documented risk acceptance or compensating security controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database configuration management identified that periodic validation of production database configurations against approved security baselines was not performed, resulting in undetected configuration drift.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database parameter management identified that critical database initialization parameters were not periodically reviewed following major database upgrades or configuration changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database configuration identified that production database instances were not periodically scanned to identify insecure configuration settings introduced through manual administrative activities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database hardening reviews identified that compliance with enterprise database hardening checklists was not independently verified prior to production deployment of newly provisioned database servers.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database software identified that unsupported optional database components remained installed despite not being utilized by business applications, increasing unnecessary security exposure.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database configuration governance identified that approved secure configuration baselines were not version-controlled or periodically updated to address emerging security threats and vendor recommendations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database infrastructure identified that configuration consistency across clustered and replicated database environments was not periodically verified, increasing the likelihood of inconsistent security controls.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Database Configuration & Hardening governance identified that enterprise database hardening standards had not undergone periodic review to align with evolving database technologies, security best practices and regulatory expectations.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database configuration reviews identified that production database configuration baselines had not undergone periodic recertification to ensure continued alignment with approved enterprise security standards and operational requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database hardening identified that database initialization parameters associated with remote administration and network connectivity had not been periodically reviewed to validate secure configuration settings.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database configuration management identified that configuration changes implemented directly within production database instances were not periodically reconciled against approved baseline configurations, increasing the likelihood of unauthorized configuration drift.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database software identified that deprecated configuration parameters remained enabled following database upgrades without documented technical justification or security assessment.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database network security identified that secure communication parameters governing database listener services were not periodically validated to ensure compliance with enterprise network security standards.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database hardening identified that automated compliance verification against approved database hardening baselines had not been implemented for production database environments, reducing the ability to identify configuration deviations in a timely manner.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database configuration governance identified that security deviations identified during database hardening reviews were not subjected to Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database platform administration identified that secure configuration templates were not consistently utilized while provisioning new production database instances, resulting in inconsistent security configurations across environments.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database documentation identified that approved secure configuration baselines, implementation procedures and configuration exception records were not consistently maintained within centralized configuration repositories.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing database hardening compliance, configuration drift, baseline deviations and unresolved configuration risks were not periodically presented to Database Administration and Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Database Configuration & Hardening procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Database Configuration & Hardening documentation identified absence of version-controlled database hardening standards aligned with the current enterprise database infrastructure and security requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that database administrators were not periodically provided awareness training on enterprise database hardening standards, secure configuration practices and configuration baseline management.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Database Configuration & Hardening activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Database Configuration & Hardening Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("Database Configuration & Hardening Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")