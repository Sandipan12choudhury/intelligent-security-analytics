"""
=============================================================
Database Encryption & Data Protection Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Database Encryption & Data Protection
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

DOMAIN = "Database Encryption & Data Protection"
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
# Database Encryption & Data Protection Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database encryption controls identified that sensitive production data was stored without implementation of approved encryption at rest controls in accordance with the Enterprise Database Security Standard. Absence of encryption increases the risk of unauthorized disclosure following storage compromise.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database communication security identified that client connections to production database instances were established without enforcement of encrypted communication protocols. Unencrypted database communications increase the risk of interception of sensitive business information during transmission.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database key management identified that encryption keys protecting production databases were not periodically rotated in accordance with enterprise cryptographic standards. Failure to rotate encryption keys increases the potential impact of long-term key compromise.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database encryption implementation identified that highly sensitive business tables containing confidential information were not protected using approved database encryption mechanisms. Lack of encryption increases exposure of sensitive data during unauthorized access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database certificate management identified that expired or weak cryptographic certificates were used to secure encrypted database communications, increasing the risk of insecure client-server connections.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database data protection controls identified that non-production databases containing production data were not protected through approved data masking or anonymization techniques. Exposure of production data within non-production environments increases confidentiality risks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database encryption governance identified that database encryption exceptions remained active beyond approved review timelines without documented risk acceptance or compensating security controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database encryption identified that encryption algorithms configured for database protection had not been periodically reviewed to ensure continued compliance with approved enterprise cryptographic standards.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database encryption implementation identified that encryption coverage for newly created database objects was not periodically validated following application deployments or schema changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of encrypted database communications identified that secure communication protocols were not consistently enforced across all database client connections within the enterprise environment.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database key protection identified that access to database encryption keys was not periodically reviewed to validate compliance with the principle of least privilege.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of sensitive data protection identified that database columns containing regulated information were not periodically reviewed to validate appropriate encryption or masking controls.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database encryption monitoring identified that failures associated with database encryption mechanisms were not consistently monitored and escalated through centralized security monitoring processes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database cryptographic controls identified that encryption configurations were not periodically validated following database software upgrades or infrastructure changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Database Encryption & Data Protection governance identified that enterprise database encryption standards had not undergone periodic review to address evolving regulatory requirements, emerging cryptographic risks and changes in database technologies.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of database encryption reviews identified that encryption controls protecting sensitive production databases had not undergone periodic business owner recertification to validate continued compliance with enterprise data protection requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database encryption identified that database encryption keys protecting archived and historical data were not periodically reviewed to ensure continued cryptographic protection throughout the data retention lifecycle.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database communication security identified that mutual authentication for encrypted database client-server communications had not been consistently implemented across critical production environments.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database data protection identified that encrypted database backups were not periodically validated to confirm encryption integrity and successful recovery of protected information.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of database encryption implementation identified that deprecated cryptographic protocols and cipher suites remained enabled for database communications without documented business justification or risk assessment.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of database key management identified that database encryption keys were not segregated according to production, test and development environments, increasing the potential impact of key compromise across multiple environments.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of database data protection governance identified that exceptions related to encrypted storage of sensitive database objects were not subjected to periodic Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of database encryption monitoring identified that repeated failures of database encryption operations and certificate validation events were not periodically analysed to identify recurring security issues.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of database documentation identified that encryption architecture diagrams, key usage documentation and database data classification records were not consistently maintained within centralized governance repositories.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing database encryption coverage, protected sensitive data, certificate status, encryption exceptions and unresolved data protection risks were not periodically presented to Database Administration and Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Database Encryption & Data Protection procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Database Encryption & Data Protection documentation identified absence of version-controlled database encryption standards aligned with the current enterprise database infrastructure, regulatory obligations and organizational data classification requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that database administrators and application support teams were not periodically provided awareness training on database encryption technologies, secure key usage practices and sensitive data protection requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Database Encryption & Data Protection activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Database Encryption & Data Protection Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("Database Encryption & Data Protection Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")