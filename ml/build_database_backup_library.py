"""
=============================================================
Database Backup, Recovery & Availability Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Database Backup, Recovery &
Availability observations into the central Observation Repository.

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

DOMAIN = "Database Backup, Recovery & Availability"
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
# Database Backup, Recovery & Availability Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database backup controls identified that production database backups were not encrypted using approved enterprise encryption mechanisms. Unencrypted backups increase the risk of unauthorized disclosure of sensitive business information if backup media is compromised.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database recovery identified that periodic restoration testing of production database backups was not performed to validate recoverability and backup integrity. Failure to verify database restoration increases the likelihood of unsuccessful recovery during operational disruptions.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database availability controls identified that high availability and replication mechanisms supporting critical production databases were not periodically tested to validate successful failover capabilities and recovery objectives.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database backup operations identified that backup jobs for critical production databases experienced repeated failures without timely investigation, remediation or documented management escalation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database backup governance identified that backup retention periods for production databases were not aligned with approved enterprise retention policies and applicable regulatory requirements.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database recovery planning identified that Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO) for critical production databases had not been formally defined, approved or periodically validated.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database backup security identified that access to production database backup repositories was not restricted according to the principle of least privilege, increasing the risk of unauthorized access or backup tampering.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database backup governance identified that high-risk backup and recovery exceptions remained active beyond approved review timelines without documented risk acceptance or compensating security controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of backup scheduling identified that production database backup schedules were not periodically reviewed to ensure alignment with evolving business continuity and operational requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of backup integrity identified that periodic verification of backup file integrity using approved validation mechanisms was not consistently performed for production database backups.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database replication identified that replication status and synchronization health for high availability database environments were not periodically monitored to identify replication failures.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database recovery procedures identified that recovery runbooks were not periodically updated to reflect infrastructure, application or database architecture changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database backup monitoring identified that alerts associated with failed backup jobs, storage capacity thresholds and backup infrastructure issues were not consistently integrated with centralized enterprise monitoring solutions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of backup storage identified that production database backups were not periodically reviewed to validate secure storage, media lifecycle management and protection against unauthorized modification.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Database Backup, Recovery & Availability governance identified that enterprise database backup and recovery standards had not undergone periodic review to address evolving business continuity requirements, technology changes and regulatory expectations.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database backup reviews identified that production database backup strategies had not undergone periodic business owner recertification to ensure continued alignment with business continuity requirements and recovery objectives.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database recovery identified that restoration testing was performed using limited datasets rather than complete production-equivalent database backups, reducing confidence in full-scale recovery capabilities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database backup security identified that backup copies stored at offsite locations were not periodically reviewed to verify encryption status, physical security controls and continued availability.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database availability identified that automatic failover mechanisms supporting high availability database environments were not periodically tested to validate successful service continuity during infrastructure failures.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database backup operations identified that obsolete database backup files exceeding approved retention periods were not consistently removed from backup repositories, increasing unnecessary storage utilization and information exposure.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database recovery identified that recovery procedures for database corruption scenarios had not been periodically exercised to validate operational readiness and recovery effectiveness.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database replication identified that replication lag and synchronization failures affecting production database replicas were not periodically analysed to identify recurring operational issues.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database backup governance identified that repeated backup failures and unsuccessful recovery activities were not subjected to Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database documentation identified that backup architecture diagrams, recovery procedures, replication topology and backup storage inventories were not consistently maintained within centralized governance repositories.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing backup success rates, restore testing status, replication health, recovery readiness and unresolved backup risks were not periodically presented to Database Administration and Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Database Backup, Recovery & Availability procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Database Backup, Recovery & Availability documentation identified absence of version-controlled database backup and recovery standards aligned with the current enterprise database infrastructure and business continuity requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that database administrators and backup operations personnel were not periodically provided awareness training on secure backup handling, database recovery procedures and high availability operations.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Database Backup, Recovery & Availability activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Database Backup, Recovery & Availability Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("Database Backup, Recovery & Availability Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")