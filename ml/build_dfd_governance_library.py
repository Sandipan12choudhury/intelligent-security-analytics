"""
=============================================================
DFD Governance & Change Management
Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade DFD Governance &
Change Management observations into the central
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

DOMAIN = "DFD Governance & Change Management"
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
# DFD Governance & Change Management
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of architecture governance identified that ownership of approved Data Flow Diagrams was not formally assigned to accountable application or business owners, reducing accountability for maintaining accurate architectural documentation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of architecture change management identified that modifications to application architecture were implemented without corresponding updates to approved Data Flow Diagrams, resulting in outdated security documentation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of governance identified that periodic reviews of approved Data Flow Diagrams were not performed to ensure continued alignment with production architecture, regulatory expectations and enterprise security standards.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of architecture governance identified that formal approval workflows for creation, modification and retirement of Data Flow Diagrams were not consistently implemented across enterprise applications.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of architecture governance identified that application enhancement projects introducing significant architectural changes were completed without mandatory review and approval of associated Data Flow Diagrams.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of architecture governance identified that version history for approved Data Flow Diagrams was not consistently maintained, reducing traceability of architectural changes over time.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of governance identified that high-risk deficiencies affecting Data Flow Diagram governance remained unresolved beyond approved remediation timelines without documented management approval or compensating controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of architecture documentation identified that application decommissioning activities were completed without formal review or retirement of associated Data Flow Diagrams, resulting in obsolete architectural documentation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of governance identified that architecture owners were not periodically required to recertify the accuracy and completeness of approved Data Flow Diagrams.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of change management identified that approved Data Flow Diagrams were not consistently linked with enterprise Change Management records, reducing traceability between production changes and architectural documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance identified that architecture review board approvals for significant application design changes were not consistently evidenced within Data Flow Diagram documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of architecture governance identified that periodic quality assurance reviews assessing completeness, consistency and compliance of approved Data Flow Diagrams were not performed.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of governance identified that architecture exceptions permitting deviations from approved Data Flow Diagram standards were not supported by documented risk assessments and management approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of documentation governance identified that approved Data Flow Diagrams were not consistently maintained within centralized repositories supporting version control, access management and document lifecycle management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of DFD Governance & Change Management identified that enterprise governance standards governing ownership, review, approval, version management and lifecycle maintenance of Data Flow Diagrams had not undergone periodic review to address evolving enterprise architecture and regulatory requirements.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of governance reviews identified that approved Data Flow Diagrams had not undergone periodic business owner recertification to confirm continued alignment with production architecture, business processes and regulatory obligations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of architecture governance identified that newly implemented application modules, interfaces and infrastructure components introduced through approved change requests were not consistently reflected within the approved Data Flow Diagrams following implementation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of change management identified that emergency changes affecting application architecture were implemented without subsequent validation and update of the associated Data Flow Diagrams, resulting in outdated architectural documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance identified that historical versions of approved Data Flow Diagrams were not retained to support auditability, forensic review and traceability of architectural evolution.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of architecture governance identified that documented ownership transfers resulting from organizational restructuring or application ownership changes were not consistently reflected within Data Flow Diagram governance records.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of governance identified that deviations from enterprise Data Flow Diagram standards were not periodically reviewed to determine whether approved exceptions remained valid and justified.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of governance identified that recurring deficiencies affecting Data Flow Diagram governance identified during architecture reviews were not subjected to Root Cause Analysis (RCA) or tracked through formal corrective action plans.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of architecture governance identified that Data Flow Diagram repositories were not periodically reconciled against the enterprise application inventory to identify missing, obsolete or duplicate architectural documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance documentation identified that architecture review decisions, management approvals and supporting evidence associated with Data Flow Diagram updates were not consistently retained within centralized governance repositories.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing Data Flow Diagram review status, overdue architectural updates, governance exceptions and unresolved documentation risks were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of DFD Governance & Change Management procedures identified that documented operating procedures governing ownership, review, approval and lifecycle management of Data Flow Diagrams had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of DFD Governance & Change Management documentation identified absence of version-controlled enterprise standards governing Data Flow Diagram governance, change control, ownership responsibilities and documentation lifecycle management.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that application owners, enterprise architects, solution architects and Information Security personnel were not periodically provided awareness training on Data Flow Diagram governance, review responsibilities and change management requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over DFD Governance & Change Management activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise DFD Governance & Change Management Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("DFD Governance & Change Management Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")