"""
=============================================================
DFD Sensitive Data Flow Protection
Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Sensitive Data Flow Protection
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

DOMAIN = "Sensitive Data Flow Protection"
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
# Sensitive Data Flow Protection
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of application architecture identified that data flows involving Personally Identifiable Information (PII) were not clearly identified within the approved Data Flow Diagram, reducing visibility of privacy-sensitive information processing activities.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of sensitive data protection identified that encryption mechanisms protecting confidential information during transmission between application components were not documented within the approved architectural diagrams.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application architecture identified that authentication credentials, cryptographic secrets or security tokens transmitted between integrated systems were not represented as protected data flows within the approved Data Flow Diagram.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application architecture identified that financial transaction data exchanged between application components was not classified or distinguished from non-sensitive business information within the approved Data Flow Diagram.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application security architecture identified that sensitive customer information traversing internal and external application interfaces was not documented as being protected through approved cryptographic controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of application architecture identified that data masking, tokenization or equivalent protection mechanisms applicable to sensitive information were not represented within the approved Data Flow Diagram where required.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of sensitive data governance identified that high-risk deficiencies affecting protection of confidential information remained unresolved beyond approved remediation timelines without documented management approval or compensating controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application architecture identified that confidential business information exchanged with third-party service providers was not clearly identified or classified within the approved Data Flow Diagram.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of sensitive data documentation identified that enterprise data classification labels were not consistently applied to sensitive information flows represented within the approved Data Flow Diagram.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of secure communication identified that protocols protecting transmission of confidential information between application components were not documented within the approved architectural documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application architecture identified that sensitive data transmitted through batch interfaces, scheduled jobs or file transfer mechanisms was not explicitly identified within the approved Data Flow Diagram.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application security identified that storage or transmission of authentication credentials, API keys or cryptographic material within application data flows was not documented with associated protection controls.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of sensitive data protection identified that periodic verification of sensitive data flows against implemented production architecture was not performed to ensure continued protection of confidential information.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of privacy protection identified that application data flows had not been reviewed to verify implementation of data minimization principles and avoidance of unnecessary transmission of sensitive information.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Sensitive Data Flow Protection governance identified that enterprise standards governing identification, classification and protection of sensitive information within application data flows had not undergone periodic review to address evolving regulatory obligations, privacy requirements and enterprise security expectations.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of sensitive data protection reviews identified that documented sensitive data flows had not undergone periodic business owner recertification to ensure continued alignment with application architecture, business processes and regulatory requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application architecture identified that newly introduced sensitive information flows resulting from application enhancements or business process changes were not reflected within the approved Data Flow Diagram, reducing visibility of confidential data processing activities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of data protection identified that application data flows involving confidential information were not consistently documented with associated encryption standards, cryptographic protocols or protection mechanisms within the approved architecture.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application architecture identified that sensitive information exchanged between production environments and external third-party service providers was not documented with associated confidentiality and privacy protection controls.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application security architecture identified that cross-border or cross-jurisdictional transmission of sensitive information was not documented within the approved Data Flow Diagram where applicable, reducing visibility of regulatory compliance obligations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of sensitive data protection identified that exceptions permitting transmission of unmasked or unencrypted sensitive information were not supported by documented business justification, risk assessment or management approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of governance identified that recurring deficiencies affecting sensitive data flow protection identified during architecture reviews were not subjected to Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application architecture identified that ownership and accountability for sensitive data flows exchanged between integrated systems were not consistently documented within the approved architectural documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of documentation repositories identified that approved sensitive data flow diagrams, data classification records and privacy impact documentation were not consistently maintained within centralized document management repositories accessible to authorized stakeholders.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing sensitive data flow coverage, encryption compliance, data classification exceptions and unresolved privacy risks were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Sensitive Data Flow Protection procedures identified that documented operating procedures governing identification, classification and protection of sensitive information within application data flows had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Sensitive Data Flow Protection documentation identified absence of version-controlled enterprise standards governing sensitive data identification, privacy classification, encryption requirements and secure data flow architecture.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that application owners, solution architects, developers and Information Security personnel were not periodically provided awareness training on sensitive data protection requirements, privacy regulations and enterprise data classification standards.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Sensitive Data Flow Protection activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Sensitive Data Flow Protection Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("DFD Sensitive Data Flow Protection Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")