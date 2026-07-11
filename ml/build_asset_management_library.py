"""
=============================================================
Asset Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Asset Management observations
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

DOMAIN = "Asset Management"
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
# Asset Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of the centralized asset inventory identified that newly commissioned production servers supporting the application were not incorporated into the approved asset inventory. Absence of complete asset records may result in unmanaged technology assets remaining outside the scope of security governance and monitoring.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application asset inventory identified that ownership was not formally assigned for multiple critical infrastructure assets. Lack of defined asset ownership may result in ineffective accountability for implementation of security controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of asset classification records identified that information assets supporting the application were not classified in accordance with the enterprise Information Classification Standard. Inappropriate classification may result in inadequate protection of sensitive information assets.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of asset criticality assessment records identified that business criticality had not been assigned for application servers and supporting infrastructure components. Absence of criticality assessment may impact risk prioritization and incident response activities.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of software asset records identified installation of software components that were not reflected within the approved software asset inventory. Unauthorized software may introduce unassessed security risks within the production environment.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of hardware asset management procedures identified that periodic physical verification of production hardware assets was not performed. Failure to validate physical assets may result in inaccurate asset inventory and ineffective asset governance.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of asset disposal records identified that retired storage media containing sensitive application information were disposed of without documented sanitization or destruction evidence. Inadequate media disposal increases the risk of unauthorized information disclosure.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of asset lifecycle management identified that obsolete production assets remained active beyond their approved operational lifecycle without documented business justification or risk assessment.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of asset inventory records identified that periodic reconciliation between the centralized asset inventory and deployed production assets was not evidenced.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of asset governance identified that application asset inventories were not periodically reviewed and approved by designated asset owners.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of software asset management identified that software version information was not consistently maintained within the approved software inventory.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of hardware asset records identified inconsistencies between serial numbers recorded in the centralized asset inventory and production infrastructure records.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of asset onboarding procedures identified that newly deployed application assets were not incorporated into the centralized asset inventory within defined operational timelines.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of asset ownership records identified that responsibility for review and maintenance of shared infrastructure assets was not formally documented.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of asset management governance identified that periodic review of dormant and inactive technology assets was not evidenced.",
        "Severity": "Medium"
    },
    
        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of asset lifecycle records identified that decommissioned application assets were not removed from the centralized asset inventory within the defined decommissioning timelines.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of asset inventory reports identified that asset location information was incomplete for multiple production infrastructure components, limiting effective asset traceability.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of asset governance identified that periodic validation of asset ownership following organizational restructuring was not evidenced, increasing the likelihood of orphaned technology assets.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of software asset records identified that unsupported software products remained deployed within the production environment without documented migration or replacement plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of hardware lifecycle records identified that End-of-Life (EOL) infrastructure assets continued to support production services without documented risk assessment or management approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of asset reconciliation reports identified discrepancies between infrastructure monitoring tools and the centralized asset inventory which were not investigated.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of asset review procedures identified that periodic asset inventory certification by application owners was not performed in accordance with organizational requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of software asset governance identified that software license utilization was not periodically reviewed to identify unauthorized or unused software installations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of infrastructure asset governance identified that virtual infrastructure assets were not consistently tracked within the centralized asset inventory.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of asset management reporting identified that periodic management dashboards summarizing asset inventory completeness and asset compliance metrics were not available for review.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of asset management procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of asset governance documentation identified absence of version-controlled Asset Management procedures aligned with current organizational practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of awareness records identified that personnel responsible for maintaining the asset inventory were not periodically provided awareness training regarding enterprise asset management requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of management reporting identified that periodic asset management metrics and compliance reports were not submitted to senior management for governance review.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of Asset Management governance identified that periodic internal quality assurance reviews over Asset Management processes were not evidenced.",
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
print("Asset Management Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")

print(f"Existing Observations   : {existing_count}")

print(f"New Observations        : {len(new_df)}")

print(f"Duplicates Removed      : {duplicates_removed}")

print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")