"""
=============================================================
Database Auditing & Monitoring Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Database Auditing & Monitoring
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

DOMAIN = "Database Auditing & Monitoring"
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
# Database Auditing & Monitoring Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database auditing identified that privileged database activities including user administration, privilege modifications and schema changes were not consistently captured within database audit logs. Incomplete audit coverage reduces the organization's ability to detect unauthorized administrative activities.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Database Activity Monitoring (DAM) identified that production database instances were not integrated with the approved database activity monitoring solution, limiting continuous monitoring of privileged SQL execution and anomalous database behaviour.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database audit trail configuration identified that audit logging for Data Definition Language (DDL) operations including CREATE, ALTER and DROP statements was not consistently enabled across production databases. Inadequate DDL auditing may result in unauthorized structural changes remaining undetected.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database monitoring identified that privileged database administrator sessions were not continuously monitored for execution of high-risk SQL statements affecting sensitive business data.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database audit governance identified that audit logs containing privileged database activities were accessible for modification by database administrators without implementation of independent integrity protection controls. Inadequate protection of audit records weakens forensic investigations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database security monitoring identified that failed database authentication attempts were not automatically correlated with enterprise security monitoring platforms for timely detection of brute-force attacks and credential misuse.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database auditing identified that access to tables containing sensitive business information was not consistently recorded within database audit trails. Absence of object-level auditing reduces visibility into unauthorized data access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database governance identified that high-risk database audit exceptions remained active beyond approved review timelines without documented management approval or formal risk acceptance.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database audit configuration identified that audit policies were not periodically reviewed following application deployments or database upgrades to ensure continued monitoring coverage.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database monitoring identified that repeated failed login attempts against privileged database accounts were not periodically analysed to identify emerging attack patterns.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database auditing identified that execution of privileged Data Control Language (DCL) statements including GRANT and REVOKE operations was not consistently captured within audit logs.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database activity monitoring identified that anomalous SQL execution patterns involving privileged accounts were not periodically analysed to identify suspicious database behaviour.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database audit retention identified that database audit logs were not retained in accordance with approved enterprise log retention requirements and regulatory obligations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of SIEM integration identified that database audit events generated by production database platforms were not consistently forwarded to the centralized Security Information and Event Management (SIEM) solution.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Database Auditing & Monitoring governance identified that enterprise database audit standards had not undergone periodic review to incorporate evolving regulatory requirements, emerging database threats and audit best practices.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database audit reviews identified that privileged audit configurations had not undergone periodic business owner recertification to ensure continued alignment with enterprise monitoring requirements and regulatory obligations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database activity monitoring identified that monitoring rules for privileged SQL execution had not been periodically tuned to address newly identified attack techniques and evolving database threats.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database auditing identified that execution of Data Manipulation Language (DML) operations affecting highly sensitive business tables was not consistently audited in accordance with enterprise data protection requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database monitoring identified that database administrator activities performed during approved maintenance windows were not periodically reviewed by personnel independent of database administration teams.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database audit configuration identified that modifications to database audit policies were not themselves captured within immutable audit logs, reducing accountability for audit configuration changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database monitoring identified that alerts generated for unauthorized privilege escalation and abnormal database administration activities were not periodically tested to verify effective detection and notification.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database audit governance identified that audit log integrity verification mechanisms were not periodically validated to ensure protection against unauthorized alteration or deletion of audit records.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database monitoring identified that repeated access attempts to sensitive database objects were not subjected to periodic trend analysis and Root Cause Analysis (RCA) to identify emerging insider threats or attack patterns.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database documentation identified that database audit policies, monitored event categories and audit configuration baselines were not consistently maintained within centralized governance repositories.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing database audit coverage, privileged activity monitoring, DAM alerts, audit exceptions and unresolved monitoring risks were not periodically presented to Database Administration and Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Database Auditing & Monitoring procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Database Auditing & Monitoring documentation identified absence of version-controlled database audit standards aligned with the current enterprise database infrastructure and regulatory requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that database administrators and security monitoring personnel were not periodically provided awareness training on database auditing requirements, Database Activity Monitoring (DAM) capabilities and forensic readiness practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Database Auditing & Monitoring activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Database Auditing & Monitoring Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("Database Auditing & Monitoring Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")