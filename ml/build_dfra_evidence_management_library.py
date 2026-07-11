"""
=============================================================
DFRA Digital Evidence Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade DFRA Digital Evidence Management
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

DOMAIN = "Digital Evidence Management"
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
# DFRA Digital Evidence Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of digital evidence management identified that formal chain of custody documentation was not consistently maintained for digital evidence collected during security investigations. Incomplete custody records reduce the evidentiary value and legal defensibility of collected evidence.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of evidence storage identified that digital forensic evidence repositories were not protected through appropriate physical and logical access controls. Inadequate protection increases the risk of unauthorized access, modification or loss of digital evidence.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of evidence inventory identified that centralized inventories documenting collected forensic evidence, evidence custodians and preservation status were not consistently maintained, reducing traceability throughout the evidence lifecycle.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of evidence collection procedures identified that standardized procedures governing identification, acquisition and handling of digital evidence were not consistently implemented across security investigations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of evidence handling identified that transfers of digital evidence between custodians were not formally documented and acknowledged, increasing the likelihood of chain of custody gaps during forensic investigations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of evidence preservation identified that legal hold procedures for digital evidence associated with ongoing investigations were not formally established, increasing the risk of inadvertent evidence disposal.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of evidence governance identified that high-risk deficiencies affecting digital evidence management remained unresolved beyond approved remediation timelines without documented risk acceptance or compensating security controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of evidence repositories identified that digital evidence was stored alongside operational business data without logical segregation, increasing the risk of unauthorized access or accidental modification.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of evidence inventory identified that metadata describing evidence source, acquisition date, custodian and case reference was not consistently maintained for collected digital evidence.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of evidence access management identified that periodic reviews of user access to digital evidence repositories were not performed to validate continued business necessity and least privilege.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of evidence handling identified that integrity verification of digital evidence following transfer between repositories or custodians was not consistently performed and documented.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of evidence documentation identified that forensic case records were not consistently linked with associated evidence inventories and chain of custody documentation, reducing investigation traceability.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of evidence lifecycle management identified that periodic reviews of retained digital evidence were not performed to confirm continued preservation requirements and authorized retention periods.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of evidence storage identified that environmental and operational controls protecting digital evidence repositories had not been periodically reviewed to ensure continued availability and protection of stored evidence.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Digital Evidence Management governance identified that enterprise digital evidence management standards had not undergone periodic review to address evolving forensic practices, legal requirements and enterprise technology changes.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of digital evidence management reviews identified that enterprise digital evidence handling procedures had not undergone periodic business owner recertification to ensure continued alignment with forensic investigation objectives and regulatory obligations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of chain of custody identified that periodic validation of custody records was not performed to verify completeness, continuity and accuracy of evidence ownership throughout the investigation lifecycle.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of evidence repositories identified that backup copies of digital evidence repositories were not periodically validated to ensure successful recovery of preserved forensic evidence following storage failures.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of evidence handling identified that digital evidence transferred to external investigators or third-party service providers was not consistently accompanied by documented transfer authorization and custody records.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of evidence lifecycle management identified that secure disposal of digital evidence upon completion of approved retention periods was not consistently documented and approved by authorized personnel.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of evidence access controls identified that privileged activities performed within digital evidence repositories were not periodically reviewed to identify unauthorized access or inappropriate evidence handling.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of evidence governance identified that recurring deficiencies affecting digital evidence handling identified during forensic readiness assessments were not subjected to Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of digital evidence identified that integrity verification records associated with collected forensic evidence were not consistently maintained to demonstrate continued authenticity throughout the evidence lifecycle.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of forensic documentation identified that digital evidence handling procedures, evidence classification guidelines and repository management responsibilities were not consistently maintained within centralized governance repositories.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing digital evidence inventory status, chain of custody exceptions, repository access reviews and unresolved evidence management risks were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Digital Evidence Management procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Digital Evidence Management documentation identified absence of version-controlled enterprise standards governing evidence acquisition, custody management, secure storage and evidence disposal activities.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that forensic responders, system administrators and security operations personnel were not periodically provided awareness training on digital evidence handling, chain of custody requirements and evidence preservation practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Digital Evidence Management activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Digital Evidence Management Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("DFRA Digital Evidence Management Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")