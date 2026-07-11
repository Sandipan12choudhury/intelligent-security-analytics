"""
=============================================================
Network Security Architecture Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Network Security Architecture
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

DOMAIN = "Network Security Architecture"
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
# Network Security Architecture Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of enterprise network architecture identified that the approved network architecture diagram had not been updated to reflect recently deployed production infrastructure and inter-network connectivity. Outdated architecture documentation may adversely impact security assessments, incident response and change management activities.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network segmentation architecture identified that critical production servers were directly accessible from user network segments without appropriate network isolation controls. Inadequate network segmentation increases the likelihood of lateral movement following compromise of user endpoints.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of enterprise network topology identified multiple single points of failure within the core network infrastructure without documented redundancy or failover capability. Network design deficiencies may result in prolonged service disruption during infrastructure failures.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of DMZ architecture identified that externally accessible application servers communicated directly with internal production databases contrary to the approved enterprise network security architecture. Inadequate network zoning may increase exposure of critical internal systems.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of network infrastructure design identified that management interfaces for critical network devices were accessible from production user networks instead of dedicated administrative management networks. Exposure of management interfaces increases the risk of unauthorized administrative access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of high availability architecture identified that redundant network paths had not been periodically tested to validate automatic failover capability during network outages. Untested failover mechanisms may impact business continuity during infrastructure failures.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network routing architecture identified unauthorized routing paths between development and production environments without documented business justification or security approval. Inadequate environment isolation increases the risk of unauthorized access to production systems.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of network architecture governance identified that critical infrastructure components supporting internet-facing services were deployed without documented security architecture review and approval. Failure to perform security architecture assessments may introduce unmanaged cyber security risks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of enterprise network documentation identified that logical network diagrams were not periodically reviewed and approved by designated network architecture owners.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network connectivity identified that communication flows between production applications and supporting infrastructure were not formally documented within the approved network architecture.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of network redundancy identified that periodic validation of redundant WAN connectivity was not evidenced for critical business applications.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of network architecture standards identified that infrastructure design reviews were not consistently performed before onboarding new enterprise applications into the production environment.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of network dependency documentation identified that dependencies between network devices, application servers and shared infrastructure services were not comprehensively documented.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network monitoring architecture identified that critical network links were not continuously monitored for availability and performance through centralized monitoring solutions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of enterprise network governance identified that periodic review of the approved Network Security Architecture Standard was not performed to incorporate emerging security requirements and technology changes.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of network architecture reviews identified that network paths supporting critical applications were not periodically assessed to ensure continued compliance with the approved Enterprise Network Architecture Standard.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of production network design identified that legacy network segments remained connected to critical production environments without documented migration plans or risk acceptance. Continued use of legacy network segments may increase operational and cyber security risks.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of network resilience testing identified that network failover scenarios involving redundant routers, switches and WAN links were not periodically exercised to validate recovery capability.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise network architecture identified that network trust boundaries separating internal, partner and external connectivity zones were not formally documented or periodically reviewed.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of infrastructure architecture identified that load balancer redundancy supporting critical production applications had not been periodically validated through failover testing.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of network governance identified that exceptions to the approved enterprise network architecture were not periodically reviewed for continued business justification or compensating security controls.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of infrastructure connectivity identified that administrative management networks were not logically segregated from production application traffic, contrary to the Enterprise Network Security Architecture Standard.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of network documentation identified that physical network topology diagrams were not synchronized with logical network architecture documentation following infrastructure changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of network governance identified that periodic capacity planning and scalability assessments for core network infrastructure were not documented for critical production environments.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise dashboards summarizing network architecture compliance, high availability status and unresolved architecture risks were not periodically presented to senior management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Network Security Architecture procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Network Security Architecture documentation identified absence of version-controlled enterprise network architecture standards aligned with the current infrastructure landscape.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that network administrators and infrastructure architects were not periodically provided awareness training on enterprise network architecture standards and secure design principles.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Network Security Architecture activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Network Security Architecture Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("Network Security Architecture Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")