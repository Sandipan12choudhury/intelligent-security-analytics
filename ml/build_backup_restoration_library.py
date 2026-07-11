"""
=============================================================
Backup & Restoration Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Backup & Restoration observations
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

DOMAIN = "Backup & Restoration"
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
# Backup & Restoration Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of backup schedules identified that periodic backups of critical application data were not performed in accordance with the approved backup policy. Failure to perform scheduled backups may result in permanent loss of business-critical information during system failures.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of backup monitoring reports identified multiple failed backup jobs that were not investigated or remediated within defined operational timelines. Unresolved backup failures may impact recovery capability during security incidents.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Examination of restoration testing records identified that periodic backup restoration exercises had not been performed for the application. Absence of restoration testing provides limited assurance regarding recoverability of backed-up data.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of backup encryption controls identified that backup media containing sensitive application data was not encrypted in accordance with enterprise information security requirements. Unencrypted backup media increases the risk of unauthorized disclosure of sensitive information.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of backup retention records identified that backup copies were retained for periods shorter than organizational retention requirements without documented approval. Inadequate retention may limit recovery options following security incidents.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of disaster recovery evidences identified that application backup procedures were not aligned with documented Disaster Recovery objectives and Recovery Point Objectives (RPO). Misalignment may affect business continuity during major disruptions.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Examination of offsite backup arrangements identified that backup copies were not maintained at geographically separate locations. Lack of offsite backups increases the risk of simultaneous loss of production and backup data during site-level incidents.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of backup integrity verification reports identified that cryptographic integrity checks were not performed on backup files following backup completion. Failure to validate backup integrity may result in undetected corruption of backup data.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of backup scheduling identified inconsistencies in backup frequency across production environments supporting critical business applications.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of backup administration procedures identified absence of documented ownership for periodic review of backup success reports.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of backup monitoring identified that automated notifications for backup failures were not configured for all critical backup jobs.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of backup reports identified that incremental and full backup schedules were not periodically reviewed for operational effectiveness.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of restoration procedures identified that documented restoration instructions were not periodically validated against current production configurations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of backup storage identified that backup repositories were not periodically reviewed for available storage capacity and growth trends.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of backup governance identified that backup exceptions were not supported by documented management approval and compensating controls.",
        "Severity": "Medium"
    },
    
        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of backup restoration reports identified that restoration success rates were not periodically measured or reported to application management. Absence of restoration performance metrics limits assurance over recovery readiness.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of backup operations identified that backup jobs associated with newly onboarded production systems were not incorporated into the enterprise backup schedule within defined timelines.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of backup retention configurations identified inconsistent retention periods across backup repositories supporting the same application environment.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Examination of restoration evidences identified that restoration testing was limited to selected application components and did not include end-to-end application recovery validation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of backup administration identified that privileged activities performed on backup infrastructure were not periodically reviewed for unauthorized changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of backup infrastructure identified that immutable backup controls were not implemented for critical application backups. Absence of immutable backups may increase exposure to ransomware attacks and malicious data modification.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of backup monitoring reports identified recurring backup failures affecting the same application components without documented root cause analysis or permanent corrective actions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of backup scheduling identified that backup windows were not periodically reviewed to ensure completion prior to commencement of critical business processing.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of backup governance identified that Recovery Time Objective (RTO) and Recovery Point Objective (RPO) compliance was not periodically validated against actual restoration test results.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of backup administration identified that backup media inventory records were not periodically reconciled with actual backup assets maintained within the backup infrastructure.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of backup procedures identified that documented backup operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of backup governance documentation identified absence of version-controlled backup procedures aligned with current enterprise operational practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of backup awareness records identified that personnel responsible for backup administration were not periodically provided awareness training regarding backup and restoration responsibilities.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of backup reporting identified that periodic management dashboards summarizing backup success rates, restoration testing and backup compliance were not available for review.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of backup governance identified that periodic internal quality assurance reviews over backup and restoration processes were not evidenced.",
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
print("Backup & Restoration Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")

print(f"Existing Observations   : {existing_count}")

print(f"New Observations        : {len(new_df)}")

print(f"Duplicates Removed      : {duplicates_removed}")

print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")