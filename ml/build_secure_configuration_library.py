"""
=============================================================
Secure Configuration Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Secure Configuration Management
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

DOMAIN = "Secure Configuration Management"
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
# Secure Configuration Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of server hardening records identified that production Linux servers were not configured in accordance with the approved Secure Configuration Standard. Multiple unnecessary services remained enabled, increasing the attack surface and exposure to unauthorized access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of cryptographic protocol configurations identified that deprecated protocols including TLS 1.0 and TLS 1.1 remained enabled on externally accessible application servers. Continued use of obsolete protocols may expose encrypted communications to known cryptographic attacks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of operating system configuration baselines identified that production Windows servers were operating with default security settings instead of the approved enterprise hardening baseline. Inadequate system hardening increases the likelihood of successful exploitation of known weaknesses.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database configuration parameters identified insecure default security settings including unrestricted network access and weak authentication configurations that were inconsistent with the approved Database Hardening Standard.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application server configuration identified that default administrative interfaces remained accessible from untrusted network segments without appropriate access restrictions. Exposure of management interfaces may facilitate unauthorized administrative access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of network device configurations identified insecure management protocols including Telnet and HTTP enabled for administrative access. Use of insecure management protocols may expose administrative credentials to interception.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of configuration compliance reports identified multiple production systems deviating from the approved enterprise security baseline without documented risk assessment or management approval.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of secure configuration reviews identified that critical configuration deviations remained unresolved beyond approved remediation timelines without documented compensating security controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of operating system hardening records identified that password complexity, account lockout and audit policy settings were not consistently configured across production servers.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application configuration reviews identified that unnecessary software components and services remained installed on production servers contrary to the approved server hardening baseline.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of secure configuration assessment reports identified that periodic compliance verification against CIS Benchmarks or equivalent hardening standards was not performed for critical production systems.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of configuration change records identified that modifications to secure configuration baselines were implemented without documented technical justification or security approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of secure configuration governance identified that configuration drift between approved baselines and production systems was not periodically monitored or reported.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of configuration monitoring identified that unauthorized configuration changes were not detected through automated configuration compliance monitoring mechanisms.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of secure configuration governance identified that periodic review of approved hardening baselines was not performed to address newly emerging cyber security threats and industry best practices.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of server configuration reviews identified that local administrator and default service accounts were not disabled or secured in accordance with the approved Secure Configuration Standard. Presence of default privileged accounts may increase the risk of unauthorized administrative access.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of operating system configurations identified that unnecessary startup services and scheduled tasks remained enabled on production servers without documented business justification, resulting in an expanded system attack surface.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of network security configurations identified that unused network ports and services remained enabled on production infrastructure contrary to the approved hardening baseline, increasing the likelihood of unauthorized network access.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of configuration compliance reports identified that secure configuration validation was performed only during initial deployment and not periodically throughout the operational lifecycle of production systems.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of middleware configuration settings identified that default security parameters supplied by the vendor had not been reviewed or hardened before deployment into the production environment.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of secure configuration exceptions identified that approved deviations from enterprise hardening standards did not contain defined review dates, documented compensating controls or formal risk acceptance.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of secure configuration governance identified that configuration baseline documents were not synchronized with infrastructure upgrades, resulting in outdated hardening requirements being referenced during security reviews.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of configuration monitoring reports identified recurring deviations from approved hardening standards without documented Root Cause Analysis (RCA) or permanent corrective actions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise security dashboards identified that secure configuration compliance metrics for critical production assets were not periodically reported to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of secure configuration governance identified that periodic independent validation of hardening compliance was not performed for business-critical production environments.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Secure Configuration Management procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Secure Configuration documentation identified absence of version-controlled hardening standards aligned with the current enterprise technology landscape.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that infrastructure administrators were not periodically trained on secure configuration standards, hardening requirements and baseline compliance expectations.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Secure Configuration Management activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Secure Configuration Management Key Performance Indicators (KPIs) were not periodically presented to senior management for governance oversight.",
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
print("Secure Configuration Management Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")

print(f"Existing Observations   : {existing_count}")

print(f"New Observations        : {len(new_df)}")

print(f"Duplicates Removed      : {duplicates_removed}")

print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")