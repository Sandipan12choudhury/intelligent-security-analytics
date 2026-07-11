"""
=============================================================
Network Segmentation & Perimeter Security Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Network Segmentation & Perimeter
Security observations into the central Observation Repository.

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

DOMAIN = "Network Segmentation & Perimeter Security"
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
# Network Segmentation & Perimeter Security Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of network segmentation controls identified that production application servers were accessible from user VLANs without traversing approved security zones, contrary to the Enterprise Network Segmentation Standard. Inadequate logical segregation increases the likelihood of lateral movement following compromise of user endpoints.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of privileged access pathways identified that administrative access to production servers was established directly from user workstations instead of designated jump servers. Direct administrative connectivity increases the risk of unauthorized privileged access and weakens monitoring of administrative activities.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of web application deployment identified that internet-facing applications were published without deployment behind an approved Web Application Firewall (WAF) or reverse proxy architecture. Absence of perimeter protection reduces resilience against application-layer attacks and unauthorized access attempts.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of network zoning identified that database servers were directly reachable from application user networks without implementation of dedicated database security zones. Inadequate isolation of database infrastructure increases the risk of unauthorized access to sensitive information.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of network trust boundaries identified unrestricted communication between development and production environments without documented business justification or approved compensating controls. Weak environment segregation increases the likelihood of unauthorized production access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of remote administration architecture identified that privileged access to critical infrastructure bypassed designated bastion hosts and centralized session monitoring controls. Uncontrolled administrative pathways reduce accountability for privileged activities.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of east-west traffic controls identified unrestricted lateral communication between critical production workloads without implementation of internal segmentation controls. Excessive east-west connectivity increases the potential impact of successful cyber attacks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of perimeter security governance identified that network segmentation exceptions remained active beyond approved review timelines without documented risk acceptance or compensating security controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of VLAN configuration identified that periodic review of VLAN membership and associated security zones was not evidenced for critical production environments.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network trust zones identified that ownership and business justification for inter-zone communication paths were not consistently documented.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of jump server administration identified that privileged administrative sessions established through jump servers were not consistently recorded or retained for audit purposes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of reverse proxy configuration identified that periodic security validation of reverse proxy routing rules was not evidenced for externally accessible production applications.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of internal segmentation identified that periodic verification of network access restrictions between critical security zones was not performed following major infrastructure changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of perimeter monitoring identified that unauthorized attempts to traverse restricted network zones were not periodically analyzed through centralized security monitoring processes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Network Segmentation governance identified that the Enterprise Network Segmentation Standard had not undergone periodic review to incorporate evolving security requirements and architectural changes.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of network segmentation reviews identified that communication paths between critical security zones had not undergone periodic business owner recertification to validate continued operational necessity. Failure to periodically review inter-zone connectivity may result in unnecessary exposure between enterprise network segments.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of internal network architecture identified that shared infrastructure services were accessible from multiple security zones without implementation of dedicated service segmentation controls. Inadequate isolation of shared services may increase the impact of lateral movement during cyber security incidents.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of network isolation controls identified that temporary network segmentation exceptions granted for project activities remained active beyond their approved validity period without documented management approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of privileged access architecture identified that privileged administrative connections traversing multiple security zones were not periodically reviewed to verify compliance with the principle of least privilege.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of DMZ architecture identified that application communication flows between the demilitarized zone (DMZ) and internal production networks were not periodically validated against approved network architecture documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of perimeter security identified that security controls protecting externally accessible services were not periodically assessed following significant infrastructure or application architecture changes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network segmentation governance identified that periodic technical validation of VLAN separation and inter-VLAN routing controls was not evidenced for critical production environments.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of administrative network segregation identified that dedicated management networks supporting infrastructure administration were not periodically assessed for unauthorized connectivity to user network segments.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of network security monitoring identified that attempted policy violations involving restricted network zones were not subjected to periodic trend analysis and Root Cause Analysis (RCA).",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing network segmentation compliance, perimeter security posture, segmentation exceptions and unresolved isolation risks were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Network Segmentation & Perimeter Security procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Network Segmentation & Perimeter Security documentation identified absence of version-controlled network segmentation standards aligned with the current enterprise infrastructure and security architecture.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that network administrators and infrastructure engineers were not periodically provided awareness training on enterprise network segmentation principles, trust zone management and perimeter security requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Network Segmentation & Perimeter Security activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Network Segmentation & Perimeter Security Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("Network Segmentation & Perimeter Security Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")