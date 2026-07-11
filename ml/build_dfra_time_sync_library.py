"""
=============================================================
DFRA Time Synchronization & Log Integrity Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade DFRA Time Synchronization &
Log Integrity observations into the central Observation Repository.

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

DOMAIN = "Time Synchronization & Log Integrity"
ACTIVITY = "DFRA"

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
# DFRA Time Synchronization & Log Integrity Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of enterprise time synchronization identified that critical production systems were not consistently synchronized with approved enterprise time sources. Unsynchronized system clocks reduce the reliability of forensic event timelines and cross-system incident correlation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of log integrity identified that security logs were not protected using integrity verification mechanisms capable of detecting unauthorized modification. Lack of integrity validation compromises the evidentiary value of retained log records.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of forensic readiness identified that periodic verification of timestamp consistency across critical infrastructure, applications and databases was not performed. Inconsistent timestamps increase the likelihood of inaccurate incident reconstruction during forensic investigations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise time services identified that Network Time Protocol (NTP) configurations were not consistently implemented across production infrastructure, resulting in inconsistent system timestamps used for forensic analysis.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of log integrity controls identified that privileged administrators were able to modify or overwrite retained security logs without implementation of independent integrity verification mechanisms.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of forensic logging identified that timestamp information associated with security events was not preserved in its original format throughout the evidence lifecycle, reducing confidence in forensic timelines.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of enterprise time governance identified that failures affecting centralized time synchronization services were not monitored or escalated, increasing the likelihood of undetected timestamp inconsistencies across enterprise systems.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of evidence integrity governance identified that high-risk deficiencies affecting log integrity validation remained unresolved beyond approved remediation timelines without documented risk acceptance or compensating controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of time synchronization identified that systems operating across multiple geographical regions were not configured with standardized time synchronization and timezone management practices to support enterprise forensic investigations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of timestamp management identified that periodic reviews of clock drift across critical production systems were not performed, increasing the possibility of inaccurate event sequencing during forensic analysis.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of log integrity identified that cryptographic hash verification of archived security logs was not periodically performed to validate continued integrity of retained forensic evidence.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of enterprise logging identified that timestamp formats generated by critical systems were not standardized, reducing the efficiency of automated forensic event correlation across heterogeneous technology platforms.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of forensic readiness identified that integrity verification procedures for security logs had not been periodically tested to confirm timely detection of unauthorized log modification.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of evidence integrity identified that changes affecting enterprise time synchronization infrastructure were not periodically reviewed to evaluate potential impact on forensic evidence reliability.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Time Synchronization & Log Integrity governance identified that enterprise standards governing timestamp consistency and forensic log integrity had not undergone periodic review to address evolving technology platforms, regulatory obligations and digital forensic best practices.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of enterprise time synchronization reviews identified that approved time synchronization configurations had not undergone periodic business owner recertification to ensure continued alignment with forensic investigation requirements and regulatory expectations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of trusted time sources identified that redundancy of enterprise time synchronization servers had not been periodically validated, increasing the risk of inaccurate timestamps during primary time source failures.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of forensic timestamp management identified that event timestamps generated by virtualized infrastructure were not periodically verified against approved enterprise time sources to ensure chronological consistency.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of log integrity controls identified that integrity validation results for archived forensic logs were not periodically reviewed to detect unauthorized modification or corruption of retained evidence.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of enterprise logging identified that timestamp normalization across operating systems, databases, applications and network devices was not consistently implemented, reducing the effectiveness of cross-platform forensic correlation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of forensic evidence identified that automated alerts for failures affecting enterprise time synchronization services had not been implemented, delaying detection of timestamp inconsistencies impacting forensic investigations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of evidence integrity governance identified that recurring deficiencies affecting timestamp accuracy and log integrity identified during forensic readiness assessments were not subjected to Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of enterprise log integrity identified that verification records demonstrating successful integrity validation of retained security logs were not consistently maintained for future forensic reference.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of forensic documentation identified that enterprise time synchronization architecture, approved time sources and integrity verification procedures were not consistently maintained within centralized governance repositories.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing enterprise time synchronization status, clock drift exceptions, log integrity validation results and unresolved forensic evidence risks were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Time Synchronization & Log Integrity procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Time Synchronization & Log Integrity documentation identified absence of version-controlled enterprise standards governing trusted time synchronization, timestamp consistency and forensic log integrity validation.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that infrastructure administrators, security operations personnel and forensic responders were not periodically provided awareness training on enterprise time synchronization requirements and forensic evidence integrity principles.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Time Synchronization & Log Integrity activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Time Synchronization & Log Integrity Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("DFRA Time Synchronization & Log Integrity Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")