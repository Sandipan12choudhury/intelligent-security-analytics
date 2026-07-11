"""
=============================================================
DFD Trust Boundaries & Data Flow Security
Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Trust Boundaries &
Data Flow Security observations into the central
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

DOMAIN = "Trust Boundaries & Data Flow Security"
ACTIVITY = "DFA / DFD"

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
# Trust Boundaries & Data Flow Security
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of application architecture identified that trust boundaries separating internal application components from external entities were not represented within the approved Data Flow Diagram, reducing visibility of security control enforcement points.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of secure data flows identified that information traversing trust boundaries was not documented as being protected through approved encryption mechanisms, increasing the risk of unauthorized disclosure during transmission.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application architecture identified that security gateways responsible for protecting communication between external users and internal application components were not represented within the approved Data Flow Diagram.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application architecture identified that trust boundaries between production environments and external third-party service providers were not clearly documented within the approved Data Flow Diagram.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application security architecture identified that security controls governing data movement across trust boundaries were not documented within the approved Data Flow Diagram, reducing assurance over secure information exchange.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of application architecture identified that authentication and authorization checkpoints protecting boundary-crossing data flows were not represented within the approved Data Flow Diagram.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of architectural security identified that high-risk deficiencies affecting trust boundary documentation remained unresolved beyond approved remediation timelines without documented management approval or compensating controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application architecture identified that network security zones including internal networks, DMZ segments and external connectivity zones were not consistently represented within the approved Data Flow Diagram.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of trust boundary documentation identified that application trust boundaries were not consistently labelled using standardized architectural conventions, reducing clarity of security documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of secure communications identified that protocols used for data transmission across trust boundaries were not documented within the approved Data Flow Diagram.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application architecture identified that security inspection points including reverse proxies, Web Application Firewalls (WAFs) or API gateways were not represented where applicable within the approved Data Flow Diagram.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of trust boundary documentation identified that application interfaces crossing organizational or business unit boundaries were not clearly distinguished within the approved Data Flow Diagram.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of architectural security identified that periodic verification of trust boundaries against the implemented production architecture was not performed to ensure continued documentation accuracy.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of boundary security identified that documentation describing security controls protecting data entering and leaving cloud-hosted environments was not incorporated within the approved Data Flow Diagram where applicable.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Trust Boundaries & Data Flow Security governance identified that enterprise standards governing trust boundary identification and secure data flow representation had not undergone periodic review to address evolving application architectures, cloud adoption and enterprise security requirements.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of trust boundary reviews identified that documented trust boundaries had not undergone periodic business owner recertification to ensure continued alignment with application architecture and evolving business processes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application security architecture identified that newly implemented trust boundaries introduced through application enhancements were not reflected within the approved Data Flow Diagram, resulting in outdated architectural security documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of boundary protection identified that data flows crossing multiple trust zones were not consistently documented with associated security validation controls including input validation, session management and request inspection mechanisms.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of architectural documentation identified that administrative interfaces crossing trust boundaries were not distinguished from business user interfaces within the approved Data Flow Diagram, reducing visibility of privileged access paths.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of secure communication architecture identified that mutual authentication requirements for inter-system communication across trust boundaries were not documented where applicable.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of trust boundary documentation identified that exceptions permitting direct communication across security zones were not supported by documented business justification, risk assessment or management approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of architectural governance identified that recurring deficiencies affecting trust boundary representation identified during architecture reviews were not subjected to Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of security architecture identified that boundary-crossing data flows involving privileged administration, monitoring or management traffic were not explicitly represented within the approved Data Flow Diagram.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of documentation repositories identified that approved architectural diagrams illustrating trust boundaries and security zones were not consistently maintained within centralized document management repositories accessible to authorized stakeholders.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing trust boundary compliance, undocumented security zones, architectural exceptions and unresolved secure architecture risks were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Trust Boundaries & Data Flow Security procedures identified that documented operating procedures governing trust boundary identification and secure data flow representation had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Trust Boundaries & Data Flow Security documentation identified absence of version-controlled enterprise standards governing trust boundary modelling, security zone representation and secure communication architecture.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that solution architects, application owners and security architects were not periodically provided awareness training on enterprise trust boundary modelling standards and secure architecture principles.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Trust Boundaries & Data Flow Security activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Trust Boundaries & Data Flow Security Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("DFD Trust Boundaries & Data Flow Security Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")