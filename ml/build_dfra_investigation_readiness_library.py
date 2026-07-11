"""
=============================================================
DFRA Forensic Investigation Readiness Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade DFRA Forensic Investigation Readiness
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

DOMAIN = "Forensic Investigation Readiness"
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
# DFRA Forensic Investigation Readiness Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of forensic investigation readiness identified that documented forensic investigation procedures were not established for major cyber security incidents. Absence of standardized investigation procedures increases the likelihood of inconsistent evidence handling and delayed incident response.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of forensic capability identified that enterprise forensic tools used for digital evidence acquisition and analysis had not undergone periodic validation to confirm operational accuracy and evidentiary reliability.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of forensic readiness identified that periodic forensic investigation exercises simulating cyber security incidents were not conducted to evaluate organizational preparedness, evidence handling procedures and investigation effectiveness.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of forensic governance identified that defined roles and responsibilities for digital forensic investigations were not formally documented, approved or communicated across relevant organizational functions.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of investigation procedures identified that standardized playbooks for malware infections, ransomware incidents, insider threats and data breach investigations were not established to support consistent forensic response activities.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of forensic evidence acquisition identified that documented procedures governing live system acquisition, memory capture and forensic disk imaging were not consistently implemented during security investigations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of forensic readiness governance identified that high-risk deficiencies affecting forensic investigation capabilities remained unresolved beyond approved remediation timelines without documented risk acceptance or compensating controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of third-party forensic support identified that arrangements governing engagement of external forensic specialists were not formally documented, increasing the risk of delayed investigation response during major security incidents.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of forensic procedures identified that investigation methodologies were not periodically reviewed to incorporate emerging cyber threat techniques, technology changes and evolving forensic best practices.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of forensic tools identified that inventories documenting approved forensic software, hardware and supporting licenses were not consistently maintained.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of investigation documentation identified that forensic case files were not consistently maintained to document investigation scope, evidence reviewed, analytical procedures performed and investigation conclusions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of forensic readiness identified that post-investigation lessons learned were not formally documented and incorporated into forensic procedures, investigation playbooks and organizational security improvements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of forensic capability identified that periodic competency assessments for personnel responsible for forensic investigations were not performed to validate required technical skills and investigative expertise.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of investigation readiness identified that escalation procedures governing transition from incident response activities to formal forensic investigations were not clearly defined and periodically validated.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Forensic Investigation Readiness governance identified that enterprise forensic investigation standards had not undergone periodic review to address evolving legal requirements, cyber threats, investigation methodologies and regulatory expectations.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of forensic investigation readiness reviews identified that enterprise forensic investigation procedures had not undergone periodic business owner recertification to ensure continued alignment with regulatory obligations, legal requirements and organizational investigation objectives.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of forensic investigation exercises identified that findings from tabletop exercises and simulated cyber security incidents were not consistently tracked to closure through documented corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of forensic tool management identified that integrity verification of forensic software, acquisition tools and supporting utilities was not periodically performed to validate operational reliability prior to investigative use.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of forensic evidence acquisition identified that standardized procedures governing acquisition of cloud-hosted digital evidence were not formally established, reducing organizational readiness to investigate cloud security incidents.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of forensic investigation readiness identified that communication procedures governing coordination between Information Security, Legal, Human Resources and business stakeholders during forensic investigations were not formally documented.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of forensic readiness identified that periodic testing of investigation escalation procedures was not performed to validate timely engagement of forensic responders during major cyber security incidents.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of forensic governance identified that recurring deficiencies affecting forensic investigation readiness identified during internal assessments were not subjected to Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of investigation documentation identified that centralized repositories containing forensic investigation reports, lessons learned and supporting investigation artifacts were not consistently maintained to support future investigations and knowledge sharing.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of forensic documentation identified that investigation playbooks, evidence acquisition procedures, escalation workflows and forensic response responsibilities were not consistently maintained within centralized governance repositories.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing forensic investigation readiness, investigation exercise results, forensic capability gaps and unresolved readiness risks were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Forensic Investigation Readiness procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Forensic Investigation Readiness documentation identified absence of version-controlled enterprise standards governing forensic investigations, evidence acquisition procedures and investigation lifecycle management.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that forensic investigators, security operations personnel and incident response teams were not periodically provided awareness training on forensic investigation methodologies, legal considerations and evidence acquisition procedures.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Forensic Investigation Readiness activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Forensic Investigation Readiness Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("DFRA Forensic Investigation Readiness Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")