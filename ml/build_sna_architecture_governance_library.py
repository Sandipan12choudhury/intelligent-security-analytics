"""
=============================================================
SNA Architecture Governance & Change Management
Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Architecture Governance &
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

DOMAIN = "Architecture Governance & Change Management"
ACTIVITY = "SNA"

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
# Architecture Governance & Change Management
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of enterprise architecture governance identified that ownership of the approved network architecture baseline was not formally assigned to accountable infrastructure or enterprise architecture teams, reducing accountability for maintaining secure architectural standards throughout the infrastructure lifecycle.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of architecture governance identified that significant modifications to enterprise network architecture were implemented without formal review by an Architecture Review Board (ARB), Technical Design Authority (TDA) or equivalent enterprise design governance function.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise architecture lifecycle identified that production network infrastructure had diverged from the approved reference architecture without documented architecture exception records, technical risk acceptance or approved remediation plans, resulting in architecture drift.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of technology lifecycle governance identified that critical routing, switching, security or communication infrastructure approaching End-of-Life (EOL) or End-of-Support (EOS) status remained deployed within production environments without approved technology modernization or replacement strategies.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of architecture governance identified that enterprise network architecture standards were not consistently enforced across newly deployed infrastructure, resulting in deviations from approved design principles and inconsistent implementation of enterprise security architecture.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of infrastructure governance identified that architectural decisions introducing new network technologies or communication platforms were implemented without documented impact assessments evaluating interoperability, security implications and long-term operational sustainability.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise architecture identified that recurring deviations from approved network design standards were not consolidated within a formal architecture exception register or technical debt register to support enterprise infrastructure modernization initiatives.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of architecture assurance identified that periodic technical assessments validating compliance of implemented infrastructure against approved enterprise reference architectures were not performed, reducing assurance over architectural consistency across production environments.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of architecture governance identified that enterprise network architecture roadmaps defining current-state, transitional and target-state architectures were not maintained to guide infrastructure modernization and strategic technology adoption.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of change governance identified that architecture impact assessments performed during major infrastructure changes did not consistently evaluate dependencies across network, security, compute and application platforms prior to implementation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise governance identified that infrastructure modernization initiatives were not prioritized using documented technical risk, architecture maturity or technology lifecycle assessments, reducing effectiveness of long-term infrastructure planning.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of architecture governance identified that periodic reviews of enterprise reference architectures were not performed to incorporate evolving cybersecurity threats, emerging infrastructure technologies and revised enterprise design standards.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of enterprise architecture identified that architecture principles governing network segmentation, resilience, secure communication and infrastructure standardization were not consistently referenced during infrastructure procurement and solution design activities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of architecture maturity identified that objective metrics measuring architecture compliance, technology obsolescence, technical debt and infrastructure standardization were not established to support continuous improvement of enterprise network architecture.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Architecture Governance & Change Management identified that enterprise governance standards governing architecture lifecycle management, technology refresh planning, architecture assurance, design authority responsibilities and infrastructure modernization had not undergone periodic review to ensure continued alignment with evolving business objectives, regulatory expectations and enterprise technology strategy.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of architecture compliance identified that implemented network infrastructure was not periodically assessed against approved enterprise reference architectures to identify deviations, unauthorized design modifications and emerging architecture risks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of architecture lifecycle governance identified that completed infrastructure change requests were not subjected to post-implementation architecture validation to confirm continued alignment with approved enterprise network design principles.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise architecture governance identified that recurring architecture exceptions remained active beyond approved review periods without documented reassessment of business justification, technical risk or modernization plans.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of technical debt management identified that infrastructure modernization backlogs were not prioritized using risk-based criteria considering technology obsolescence, architecture complexity, operational resilience and cybersecurity exposure.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of architecture assurance identified that enterprise network architecture principles were not consistently validated during procurement, solution design and infrastructure onboarding activities, increasing the risk of introducing non-standard technologies into production environments.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of architecture governance identified that approved deviations from enterprise architecture standards were not supported by documented sunset plans, measurable remediation milestones or defined target-state transition objectives.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of enterprise architecture identified that periodic architecture maturity assessments evaluating infrastructure standardization, technology lifecycle alignment, resilience capabilities and security architecture compliance were not performed.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of architecture governance identified that architecture review outcomes, technical design decisions and approval records were not consistently retained within centralized repositories to support auditability, traceability and enterprise knowledge management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of enterprise governance identified that architecture performance indicators measuring design compliance, infrastructure standardization, modernization progress and technical debt reduction were not periodically reviewed to support continuous architecture improvement.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of architecture assurance identified that independent architecture assessments evaluating compliance with enterprise design principles, cybersecurity architecture standards and approved target-state architectures were not periodically performed.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Architecture Governance & Change Management procedures identified that documented operating procedures governing enterprise architecture lifecycle management, design authority reviews, architecture compliance validation and technical debt management had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Architecture Governance & Change Management documentation identified absence of version-controlled enterprise standards governing architecture governance, reference architecture management, technology lifecycle planning and architecture assurance activities.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that enterprise architects, network architects, infrastructure engineers and Information Security personnel were not periodically provided technical awareness training on enterprise architecture governance, design authority responsibilities and infrastructure modernization practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic architecture assurance reviews evaluating effectiveness of enterprise architecture governance, technical debt remediation activities and compliance with approved design standards were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise architecture dashboards presenting architecture compliance, technology lifecycle status, technical debt, modernization progress, architecture exception trends and governance risks were not periodically reported to senior management and architecture governance forums for strategic oversight.",
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
print("SNA Architecture Governance & Change Management Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")