"""
=============================================================
Incident Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Incident Management observations
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

DOMAIN = "Incident Management"
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
# Incident Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of security incident records identified that High Severity security incidents were not escalated to the Information Security team within the timelines prescribed by the Incident Response Standard. Delayed escalation may adversely impact timely containment and recovery activities.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of incident response evidences identified that security incidents affecting production systems were closed without documented Root Cause Analysis (RCA). Absence of RCA limits identification of underlying control deficiencies and increases the likelihood of recurring incidents.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of incident investigation records identified that digital evidence collected during security incidents was not preserved in accordance with approved evidence handling procedures. Improper evidence preservation may affect forensic investigations and legal admissibility.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of incident management records identified that multiple security incidents were not formally classified based on severity and business impact prior to initiation of response activities. Inconsistent classification may result in ineffective prioritization of incident response efforts.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of incident response procedures identified that documented containment procedures were not available for critical cybersecurity incidents affecting production environments. Absence of predefined containment procedures may prolong incident impact and business disruption.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of incident notification records identified that key business stakeholders were not informed within the timelines defined by the Incident Management Policy following occurrence of critical security incidents.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of security incident registers identified recurring security incidents impacting the same application components without evidence of permanent corrective actions or preventive controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of post-incident activities identified that corrective actions arising from previous security incidents remained open beyond approved remediation timelines without documented management approval.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of incident reporting records identified that incident response timelines were not consistently documented for all reported security incidents.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of incident management procedures identified that security incidents were not consistently categorized according to the organization's approved incident classification framework.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of incident response records identified that evidence of technical investigation activities was not consistently maintained for security incidents affecting production applications.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of incident closure records identified that incident closure approvals from designated incident owners were not consistently documented.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of incident escalation procedures identified that escalation matrices were not periodically reviewed to ensure alignment with the current organizational structure.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of incident response testing identified that periodic tabletop exercises and incident response simulations were not conducted for critical application environments.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of incident governance identified that periodic review of open security incidents by application management was not evidenced.",
        "Severity": "Medium"
    },
    
        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of incident review records identified that lessons learned from major security incidents were not documented or communicated to relevant technology teams. Failure to institutionalize lessons learned may result in recurrence of similar security incidents.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of incident management reports identified that recurring security incidents were not subjected to trend analysis to identify systemic control weaknesses requiring remediation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of incident documentation identified that supporting evidences including system logs, screenshots and investigation artefacts were not consistently maintained within the incident records.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of incident response procedures identified that responsibilities of incident responders were not clearly defined for all phases of the incident response lifecycle.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of incident handling records identified that containment, eradication and recovery activities were not consistently documented for closed security incidents.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of management review records identified that periodic review of incident response effectiveness by senior management was not evidenced.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of incident metrics identified that Mean Time to Detect (MTTD) and Mean Time to Respond (MTTR) were not periodically monitored for security incidents affecting critical applications.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of incident governance identified that dependencies between security incidents and associated problem management activities were not formally tracked.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of incident response coordination identified that third-party service providers were not formally integrated into incident escalation and response procedures for outsourced services.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of incident reporting identified that periodic management dashboards summarizing incident trends, severity distribution and remediation performance were not available for review.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of Incident Management procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Incident Management documentation identified absence of version-controlled Incident Response procedures aligned with current organizational security practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of awareness records identified that personnel responsible for incident handling were not periodically provided training on the organization's Incident Management framework.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Incident Management activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that periodic governance reports covering security incident performance indicators were not presented to senior management.",
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
print("Incident Management Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")

print(f"Existing Observations   : {existing_count}")

print(f"New Observations        : {len(new_df)}")

print(f"Duplicates Removed      : {duplicates_removed}")

print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")