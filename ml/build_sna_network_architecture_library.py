"""
=============================================================
SNA Network Architecture & Documentation
Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Network Architecture &
Documentation observations into the central
Observation Repository.

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

DOMAIN = "Network Architecture & Documentation"
ACTIVITY = "SNA"

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
# Network Architecture & Documentation
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of enterprise network documentation identified that an approved network architecture diagram was not available for the application environment under assessment. Absence of an approved architecture diagram reduces visibility of infrastructure components and communication paths.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network architecture identified that the documented network topology did not accurately represent the current production environment, resulting in inconsistencies between implemented infrastructure and approved documentation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of infrastructure documentation identified that critical network devices including routers, switches, firewalls or load balancers were omitted from the approved network architecture documentation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise network architecture identified that connectivity between application servers, databases and supporting infrastructure components was not comprehensively documented within the approved network topology.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of infrastructure documentation identified that network diagrams did not accurately represent production VLANs, network segments or communication paths supporting business-critical applications.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of network documentation identified that Internet connectivity, WAN links or third-party communication paths supporting enterprise applications were not represented within the approved network architecture.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network governance identified that high-risk deficiencies affecting network architecture documentation remained unresolved beyond approved remediation timelines without documented management approval or compensating controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of enterprise architecture identified inconsistencies between approved network diagrams, infrastructure inventories and configuration management records, reducing confidence in documentation accuracy.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of network documentation identified that network devices were not consistently labelled using standardized enterprise naming conventions, reducing clarity and maintainability of architectural documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of infrastructure documentation identified that IP addressing schemes and subnet allocations were not comprehensively represented within the approved network architecture documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of network architecture identified that obsolete infrastructure components remained represented within approved network diagrams despite retirement from the production environment.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of infrastructure documentation identified that network dependencies supporting application availability and inter-system communication were not comprehensively documented within the approved architecture.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of network documentation identified that periodic reconciliation between implemented infrastructure and approved network diagrams was not performed to ensure continued architectural accuracy.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of documentation completeness identified that network architecture diagrams did not include supporting infrastructure such as DNS servers, proxy servers, authentication services or monitoring systems where applicable.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Network Architecture & Documentation governance identified that enterprise standards governing preparation, maintenance and lifecycle management of network architecture documentation had not undergone periodic review to address evolving infrastructure technologies and enterprise architecture requirements.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of network architecture reviews identified that approved network diagrams had not undergone periodic infrastructure owner recertification to ensure continued alignment with the production environment and enterprise architecture standards.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network documentation identified that newly deployed network devices, communication links and supporting infrastructure introduced through approved change requests were not reflected within the approved network architecture documentation following implementation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of enterprise infrastructure identified that inter-data center connectivity supporting production and disaster recovery environments was not comprehensively documented within the approved network architecture.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of network documentation identified that administrative management networks supporting infrastructure devices were not distinguished from production communication networks within the approved architecture diagrams.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of network architecture identified that wireless infrastructure, remote office connectivity and enterprise branch communication paths were not represented within the approved network documentation where applicable.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of infrastructure documentation identified that temporary network configurations, legacy communication paths or transitional architectures remained represented within approved network diagrams despite retirement from the production environment.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network governance identified that recurring deficiencies affecting network architecture documentation identified during infrastructure reviews were not subjected to Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of network documentation identified that ownership and accountability for critical network devices, communication links and supporting infrastructure components were not consistently documented within the approved architecture.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of documentation repositories identified that approved network architecture diagrams, infrastructure topology documents and supporting design records were not consistently maintained within centralized document management repositories accessible to authorized stakeholders.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing network documentation completeness, outdated architecture diagrams, unresolved documentation exceptions and infrastructure documentation risks were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Network Architecture & Documentation procedures identified that documented operating procedures governing preparation, maintenance and lifecycle management of network architecture documentation had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Network Architecture & Documentation identified absence of version-controlled enterprise standards governing network topology documentation, infrastructure diagram preparation and architecture documentation lifecycle management.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that network administrators, infrastructure engineers, enterprise architects and Information Security personnel were not periodically provided awareness training on enterprise network documentation standards and architecture management requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Network Architecture & Documentation activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Network Architecture & Documentation Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("SNA Network Architecture & Documentation Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")