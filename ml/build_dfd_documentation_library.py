"""
=============================================================
DFD Data Flow Documentation & Completeness
Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Data Flow Documentation &
Completeness observations into the central Observation
Repository.

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

DOMAIN = "Data Flow Documentation & Completeness"
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
# Data Flow Documentation & Completeness
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of application architecture documentation identified that an approved Data Flow Diagram (DFD) was not available for the application under assessment. Absence of an approved DFD reduces visibility of information movement and limits effective security analysis.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Data Flow Diagram documentation identified that the documented DFD did not accurately represent the current production architecture, resulting in discrepancies between documented and actual application data flows.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application documentation identified that critical application components, processing nodes or supporting services were omitted from the documented Data Flow Diagram, reducing completeness of architectural representation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application interfaces identified that one or more external entities interacting with the application were not represented within the approved Data Flow Diagram, resulting in incomplete documentation of application interactions.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application architecture identified that data stores supporting critical business functions were not represented within the Data Flow Diagram, reducing visibility of information storage locations and associated security considerations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of application documentation identified that major application data flows between business processes, interfaces and supporting infrastructure were incompletely documented within the approved Data Flow Diagram.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of architectural documentation identified that high-risk deficiencies affecting completeness of the Data Flow Diagram remained unresolved beyond approved remediation timelines without documented management approval or compensating controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application documentation identified inconsistencies between system architecture documentation, network diagrams and the approved Data Flow Diagram, reducing confidence in architectural accuracy.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Data Flow Diagram documentation identified that application processes were not consistently labelled using standardized naming conventions, reducing clarity and maintainability of architectural documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application documentation identified that data flows were not consistently labelled to describe the nature of information exchanged between system components and external entities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of Data Flow Diagram documentation identified that obsolete application components remained represented within the DFD despite retirement from the production environment, reducing documentation accuracy.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of architectural documentation identified that supporting batch processes, scheduled jobs or background services were not represented within the approved Data Flow Diagram where applicable.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of application documentation identified that periodic reconciliation between implemented application architecture and the approved Data Flow Diagram was not performed to confirm continued documentation accuracy.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of documentation completeness identified that application dependencies, upstream systems and downstream consuming applications were not comprehensively represented within the approved Data Flow Diagram.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Data Flow Documentation & Completeness governance identified that enterprise standards governing Data Flow Diagram preparation and documentation completeness had not undergone periodic review to address evolving application architecture and enterprise documentation requirements.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Data Flow Diagram reviews identified that documented application data flows had not undergone periodic business owner recertification to ensure continued alignment with the production environment and business processes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of architectural documentation identified that application interfaces introduced through recent system enhancements were not reflected within the approved Data Flow Diagram, resulting in incomplete documentation of production architecture.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of documentation completeness identified that inter-application dependencies supporting critical business services were not consistently represented within the approved Data Flow Diagram, limiting visibility of end-to-end business processes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application documentation identified that manual processing activities influencing application data movement were not represented within the Data Flow Diagram where applicable, reducing completeness of business process documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of architectural documentation identified that application entry points, output destinations and intermediate processing stages were not comprehensively documented within the approved Data Flow Diagram.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of documentation quality identified that Data Flow Diagrams were prepared using inconsistent notation standards, reducing readability, maintainability and consistency across enterprise application documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of documentation governance identified that recurring deficiencies affecting Data Flow Diagram completeness identified during architecture reviews were not subjected to Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of architectural documentation identified that unique identifiers linking Data Flow Diagrams with application architecture documents, interface specifications and asset inventories were not consistently maintained.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of documentation repositories identified that approved Data Flow Diagrams were not consistently maintained within centralized document management repositories accessible to authorized stakeholders.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing Data Flow Diagram completeness, documentation exceptions, pending updates and unresolved architectural documentation risks were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Data Flow Documentation & Completeness procedures identified that documented operating procedures governing preparation and maintenance of Data Flow Diagrams had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Data Flow Documentation & Completeness documentation identified absence of version-controlled enterprise standards governing preparation, review and maintenance of Data Flow Diagrams.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that application owners, solution architects and development teams were not periodically provided awareness training on enterprise Data Flow Diagram standards and documentation requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Data Flow Documentation & Completeness activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Data Flow Documentation & Completeness Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("DFD Data Flow Documentation & Completeness Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")