"""
=============================================================
SNA Network Segmentation & Perimeter Security
Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Network Segmentation &
Perimeter Security observations into the central
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

DOMAIN = "Network Segmentation & Perimeter Security"
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
# Network Segmentation & Perimeter Security
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of enterprise network architecture identified that production application servers, middleware infrastructure and database servers were deployed within a common security zone without documented justification for the absence of tier-based network segmentation, increasing the potential impact of lateral movement following host compromise.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network segmentation identified that application workloads supporting distinct business functions were deployed within the same Layer-2 broadcast domain without logical separation through VLANs, Virtual Routing and Forwarding (VRF) instances or equivalent network isolation mechanisms.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of inter-zone routing identified unrestricted Layer-3 communication between user, application and database security zones without documented access control policies, stateful inspection controls or business justification, increasing exposure to unauthorized east-west network movement.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of perimeter architecture identified that Internet-facing application components communicated directly with internal production workloads without an appropriately segmented Demilitarized Zone (DMZ) or equivalent security buffer separating external and internal network segments.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of enterprise network architecture identified that administrative management interfaces for network infrastructure devices were accessible from end-user workstation networks rather than through a dedicated management network or privileged administration segment.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of perimeter security identified that inbound communication from external networks was permitted to internal application environments without documented security enforcement points such as reverse proxy infrastructure, Web Application Firewalls (WAFs) or equivalent application-layer inspection controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of network segmentation identified that third-party vendor connectivity terminated directly within production network segments without dedicated partner security zones, restricted routing policies or controlled inspection points.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of internal network architecture identified unrestricted east-west communication between production server segments without implementation of internal segmentation firewalls, micro-segmentation policies or equivalent network isolation controls to restrict lateral movement.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of network zoning identified that environments supporting Development, User Acceptance Testing (UAT) and Production workloads were interconnected through shared network segments without documented isolation controls or formally approved communication paths.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of segmentation architecture identified that inter-VLAN routing policies permitting communication between security zones were not consistently documented with associated business justification and least-privilege access requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of network architecture identified that network access control mechanisms governing endpoint connectivity to critical infrastructure segments were not documented within the approved enterprise network architecture where applicable.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of security architecture identified that dedicated security zones protecting authentication infrastructure, directory services or identity management platforms were not represented within the approved network architecture documentation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of network segmentation identified that communication paths between branch networks, remote office locations and central data center environments were not documented with associated trust boundaries, routing controls and security inspection points.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of perimeter architecture identified that ingress and egress traffic inspection points were not comprehensively documented to demonstrate how traffic entering or leaving enterprise security zones is monitored, filtered and controlled.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Network Segmentation & Perimeter Security governance identified that enterprise segmentation standards governing security zones, Layer-2 and Layer-3 isolation, perimeter protection architecture and east-west traffic control had not undergone periodic review to address evolving threat landscapes and enterprise infrastructure changes.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of enterprise network architecture identified that privileged administrative access to production infrastructure was not routed through dedicated bastion hosts or hardened jump servers, increasing exposure of administrative interfaces to compromise originating from user-accessible network segments.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Zero Trust architecture identified that implicit trust relationships existed between internal network segments, permitting unrestricted communication between authenticated workloads without continuous verification of identity, device posture or business context.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of micro-segmentation controls identified that security policies governing workload-to-workload communication within production environments were not implemented, allowing unrestricted east-west traffic between application components with differing security classifications.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of network security architecture identified that internal Access Control Lists (ACLs) governing communication between critical infrastructure segments were not periodically reviewed to verify alignment with least-privilege access principles and current business requirements.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of perimeter architecture identified that inbound connectivity from partner networks and external service providers terminated within shared enterprise network zones without dedicated inspection gateways, restricted routing domains or policy-based segmentation controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of segmentation architecture identified that exceptions permitting communication across isolated security zones were not supported by documented risk assessments, business justification, defined expiry periods or formal management approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network security identified that east-west traffic traversing internal security zones was not consistently subjected to inspection through internal segmentation firewalls, intrusion detection mechanisms or equivalent security monitoring controls.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of enterprise architecture identified that network segmentation supporting container platforms, virtualization clusters or software-defined infrastructure environments was not documented with corresponding isolation boundaries and communication restrictions where applicable.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of segmentation architecture identified that management plane, control plane and data plane communication paths were not logically separated within the enterprise network architecture, increasing the potential impact of compromise affecting critical infrastructure management functions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of network architecture identified that periodic validation of implemented segmentation controls through network architecture reviews, configuration verification or segmentation testing was not evidenced to confirm continued effectiveness of isolation mechanisms.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Network Segmentation & Perimeter Security procedures identified that documented operating procedures governing network zoning, segmentation standards, perimeter security architecture and inter-zone communication controls had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Network Segmentation & Perimeter Security documentation identified absence of version-controlled enterprise standards governing security zone design, Zero Trust segmentation, internal firewall placement and micro-segmentation architecture.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that network architects, infrastructure engineers and Information Security personnel were not periodically provided technical awareness training on enterprise network segmentation principles, Zero Trust architecture and secure perimeter design practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic architecture assurance reviews evaluating compliance of implemented network segmentation against approved enterprise security architecture standards were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise metrics covering segmentation compliance, inter-zone communication exceptions, Zero Trust adoption, micro-segmentation coverage and unresolved network architecture risks were not periodically reported to senior management for governance oversight.",
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
print("SNA Network Segmentation & Perimeter Security Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")