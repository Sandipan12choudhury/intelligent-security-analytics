"""
=============================================================
Patch Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Patch Management observations
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

DOMAIN = "Patch Management"
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
# Patch Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of patch deployment records identified that Critical security patches released by vendors were not deployed within the timelines prescribed by the organization's Patch Management Policy. Delayed deployment of security patches may expose production systems to publicly known vulnerabilities and increase the likelihood of successful cyber attacks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of operating system patch reports identified that multiple production servers were operating on unsupported operating system versions that had reached End-of-Life (EOL). Continued use of unsupported platforms may result in absence of vendor security updates and increased exposure to emerging threats.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of patch compliance reports identified recurring non-compliance with defined patch deployment timelines for internet-facing application servers. Failure to remediate identified security vulnerabilities within approved timelines may significantly increase the organization's external attack surface.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of patch validation records identified that production patches were deployed without documented User Acceptance Testing (UAT) or technical validation. Deployment of unverified patches may adversely impact application availability and business continuity.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of emergency patch implementation records identified that emergency security patches were deployed directly into production without subsequent documentation, management approval or post-implementation review. Inadequate governance over emergency patch deployment increases operational and security risks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of infrastructure patch records identified that firmware and hypervisor security updates for virtualization infrastructure were not periodically reviewed and deployed. Delayed infrastructure patching may expose multiple hosted production systems to common security vulnerabilities.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of third-party software patch records identified that security updates for third-party libraries and application dependencies were not incorporated into the enterprise patch management process. Unpatched third-party components may introduce exploitable security weaknesses into production applications.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of patch governance identified that production servers with critical vulnerabilities remained excluded from scheduled patch deployment activities without documented risk acceptance or compensating security controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of patch management procedures identified that patch deployment schedules were not consistently aligned with application maintenance windows.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of patch inventory identified that deployed security patches were not periodically reconciled against vendor-released security advisories.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of patch testing evidences identified that rollback procedures for failed patch deployments were not documented prior to production implementation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of patch compliance reports identified that periodic patch compliance reviews were not performed for production databases, middleware and application servers.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of patch deployment records identified inconsistencies between approved patch deployment schedules and actual production implementation dates.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of patch governance identified that responsibilities for reviewing vendor security bulletins and vulnerability advisories were not formally assigned.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of production patch reports identified that patch deployment exceptions were not periodically reviewed by Information Security and application owners.",
        "Severity": "Medium"
    },
    
        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of patch deployment reports identified that security patches deployed across clustered production environments were implemented inconsistently, resulting in version mismatch between cluster nodes. Inconsistent patch levels may affect application stability and increase operational risk.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of patch verification records identified that post-deployment validation was not consistently performed to confirm successful installation of security patches across all targeted production systems.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of operating system maintenance records identified that patch deployment activities were repeatedly deferred due to operational constraints without documented risk assessment or management approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of patch lifecycle documentation identified that superseded security patches were not periodically reviewed to ensure appropriate replacement by the latest cumulative security updates.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of application patch records identified that production patch deployment activities were not consistently synchronized with corresponding infrastructure patch implementation schedules.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of patch management governance identified that recurring delays in patch implementation were not subjected to Root Cause Analysis (RCA) to identify underlying process deficiencies.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of patch exception registers identified that approved patch exceptions did not contain defined review periods, expiry dates or documented compensating security controls.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of patch monitoring reports identified that automated alerts for failed patch deployments were not configured for all critical production infrastructure components.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of vendor advisory management identified that newly released security advisories were not periodically assessed to determine applicability to enterprise applications and supporting infrastructure.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of management reporting identified that periodic dashboards summarizing patch compliance, overdue patches and critical vulnerability remediation status were not available for governance review.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of Patch Management procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Patch Management documentation identified absence of version-controlled patch management procedures aligned with current enterprise operational practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of awareness records identified that infrastructure administrators were not periodically provided awareness training regarding enterprise patch management requirements and security update responsibilities.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Patch Management activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Patch Management Key Performance Indicators (KPIs) were not periodically presented to senior management for governance oversight.",
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
print("Patch Management Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")

print(f"Existing Observations   : {existing_count}")

print(f"New Observations        : {len(new_df)}")

print(f"Duplicates Removed      : {duplicates_removed}")

print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")