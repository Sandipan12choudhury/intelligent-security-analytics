"""
=============================================================
DFD Interface & Integration Security
Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Interface & Integration Security
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

DOMAIN = "Interface & Integration Security"
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
# Interface & Integration Security
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of application architecture identified that APIs facilitating communication between internal applications and external service providers were not comprehensively represented within the approved Data Flow Diagram, reducing visibility of application integration points.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of interface security identified that authentication mechanisms protecting application interfaces were not documented within the approved Data Flow Diagram, limiting visibility of access control enforcement across integrated systems.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application integration identified that middleware components responsible for routing business transactions between enterprise applications were not represented within the approved architectural documentation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application interfaces identified that third-party service integrations supporting critical business processes were not documented within the approved Data Flow Diagram, resulting in incomplete architectural visibility.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of interface security identified that communication channels supporting application integrations were not documented as being protected through approved encryption mechanisms, increasing the risk of unauthorized disclosure during data exchange.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of application architecture identified that file transfer interfaces supporting critical business operations were not represented within the approved Data Flow Diagram, reducing visibility of batch data exchange mechanisms.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of integration architecture identified that high-risk deficiencies affecting interface documentation remained unresolved beyond approved remediation timelines without documented management approval or compensating controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application integration identified that direct system-to-system communication paths bypassing approved integration gateways or middleware were not documented or supported by documented business justification.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of interface documentation identified that APIs were not consistently classified as internal, external or third-party interfaces within the approved Data Flow Diagram, reducing architectural clarity.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of secure integration identified that protocols used for application-to-application communication including REST, SOAP, message queues or file transfer mechanisms were not documented within the approved architectural diagrams.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application architecture identified that asynchronous communication mechanisms including message queues, event brokers or publish-subscribe services were not represented where applicable within the approved Data Flow Diagram.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of interface security identified that application integrations requiring service accounts or machine identities were not documented with associated authentication mechanisms within the approved Data Flow Diagram.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of application architecture identified that periodic verification of documented interfaces against implemented production integrations was not performed to ensure continued architectural accuracy.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of interface monitoring identified that logging and monitoring points supporting critical application integrations were not represented within the approved Data Flow Diagram where applicable.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Interface & Integration Security governance identified that enterprise standards governing secure application integrations, interface documentation and communication architecture had not undergone periodic review to address evolving integration technologies and enterprise security requirements.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of interface security reviews identified that documented application interfaces and integration points had not undergone periodic business owner recertification to ensure continued alignment with the production architecture and business requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application integration identified that newly implemented APIs, web services or third-party integrations introduced through system enhancements were not reflected within the approved Data Flow Diagram, resulting in incomplete architectural documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of interface security identified that input validation, output validation and error handling controls applicable to application interfaces were not documented within the approved architecture, reducing visibility of interface security controls.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application architecture identified that scheduled batch interfaces and automated background integrations exchanging business data were not consistently represented within the approved Data Flow Diagram.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of integration security identified that certificate management, mutual authentication or secure key exchange requirements protecting application integrations were not documented where applicable.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of interface architecture identified that application integrations bypassing approved authentication mechanisms were not supported by documented business justification, risk assessment or management approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of integration governance identified that recurring deficiencies affecting interface and integration security identified during architecture reviews were not subjected to Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application integration identified that dependencies on external APIs, cloud services and shared enterprise services were not consistently documented with associated interface ownership and accountability.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of documentation repositories identified that approved interface specifications, API documentation and integration architecture diagrams were not consistently maintained within centralized document management repositories accessible to authorized stakeholders.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing application integration coverage, undocumented interfaces, interface security exceptions and unresolved integration risks were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Interface & Integration Security procedures identified that documented operating procedures governing secure application interfaces and system integrations had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Interface & Integration Security documentation identified absence of version-controlled enterprise standards governing API security, middleware integrations, third-party interfaces and secure communication architecture.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that application owners, integration developers and solution architects were not periodically provided awareness training on secure interface design principles and enterprise integration standards.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Interface & Integration Security activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Interface & Integration Security Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("DFD Interface & Integration Security Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")