"""
=============================================================
SNA Infrastructure Resilience & High Availability
Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Infrastructure Resilience &
High Availability observations into the central
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

DOMAIN = "Infrastructure Resilience & High Availability"
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
# Infrastructure Resilience & High Availability
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of enterprise network architecture identified that perimeter firewall infrastructure was deployed as a standalone appliance without stateful high-availability clustering, synchronized failover or equivalent redundancy mechanisms, creating a single point of failure for ingress and egress network traffic.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network resilience identified that production connectivity relied upon a single upstream telecommunications provider without physically diverse carrier paths, redundant edge routing infrastructure or automated failover mechanisms, increasing the likelihood of prolonged service disruption following provider outages.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of disaster recovery architecture identified that network connectivity supporting the secondary data center was not provisioned with equivalent bandwidth, routing resilience and security controls as implemented within the primary production environment, reducing the effectiveness of disaster recovery operations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of infrastructure resilience identified that production network architecture contained single points of failure within core routing, switching or gateway infrastructure without documented redundancy, increasing the probability of enterprise-wide service disruption following component failure.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of high-availability architecture identified that critical application delivery infrastructure, including load balancers or reverse proxy services, lacked redundant deployment with synchronized state information, increasing the risk of session interruption during failover events.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of infrastructure resilience identified that centralized authentication services supporting enterprise administrative access represented a single dependency without redundant authentication infrastructure capable of maintaining service continuity during component failure.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of network architecture identified that redundant communication links between critical infrastructure components were configured without documented path diversity, resulting in exposure to common-mode failures affecting multiple communication paths simultaneously.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of enterprise infrastructure identified that failover architecture supporting critical business services depended upon manual operational intervention rather than automated detection, health monitoring and traffic redirection mechanisms, increasing recovery time objectives during infrastructure failures.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of resilience architecture identified that redundancy mechanisms protecting production infrastructure were not consistently implemented across network, compute and supporting platform services, resulting in uneven resilience capabilities across critical application components.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of network resilience identified that equal-cost multipath routing, link aggregation or equivalent traffic distribution mechanisms were not implemented where appropriate to improve communication path availability and fault tolerance.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise infrastructure identified that redundancy supporting Domain Name System (DNS), Network Time Protocol (NTP) and centralized logging services was not documented, increasing dependency on individual infrastructure components for critical enterprise services.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of resilience controls identified that automated health monitoring, heartbeat validation and failover trigger mechanisms supporting critical network infrastructure were not documented within the approved enterprise architecture.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of infrastructure resilience identified that periodic validation of high-availability mechanisms, redundancy architecture and failover capabilities was not performed through controlled resilience testing to confirm operational effectiveness.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of disaster recovery architecture identified that communication paths supporting backup infrastructure, storage replication and disaster recovery operations were not periodically validated to ensure consistency with production resilience objectives.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Infrastructure Resilience & High Availability governance identified that enterprise standards governing redundancy architecture, high-availability design, disaster recovery connectivity and infrastructure resilience testing had not undergone periodic review to address evolving business continuity requirements and enterprise infrastructure modernization initiatives.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of gateway resilience identified that default gateway redundancy for critical production networks was not implemented using resilient first-hop redundancy mechanisms, increasing the likelihood of network disruption following gateway failure.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of enterprise WAN architecture identified that Software-Defined Wide Area Network (SD-WAN), Multiprotocol Label Switching (MPLS) or equivalent WAN resiliency mechanisms were not configured to provide automatic traffic failover between geographically diverse communication paths supporting critical business services.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application delivery architecture identified that Global Server Load Balancing (GSLB) or equivalent geographic traffic distribution mechanisms were not implemented for Internet-facing business services requiring continuous availability across multiple data center locations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of infrastructure resilience identified that control-plane services supporting routing, switching and network management lacked redundant deployment and synchronization mechanisms, increasing the likelihood of network instability following infrastructure component failures.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of enterprise architecture identified that high-availability clusters supporting critical infrastructure components were not periodically validated for state synchronization, failover consistency and service continuity under production-equivalent operating conditions.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of resilience architecture identified that exceptions permitting deployment of single-instance infrastructure supporting critical business services were not supported by documented business impact assessments, compensating controls, recovery objectives or formal management approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of capacity engineering identified that resilience planning did not consider infrastructure capacity requirements following failover scenarios, creating the risk that surviving infrastructure components may be unable to sustain production workloads during component outages.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of disaster recovery resilience identified that Recovery Time Objectives (RTOs) and Recovery Point Objectives (RPOs) established for critical business services were not periodically validated against implemented infrastructure capabilities and failover architecture.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise resilience architecture identified that automated dependency mapping between network infrastructure, application platforms and shared enterprise services was not maintained, limiting visibility of cascading failures during infrastructure disruptions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of infrastructure assurance identified that periodic resilience exercises simulating network device failures, communication path outages and data center failover scenarios were not evidenced to validate operational readiness of the enterprise infrastructure.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Infrastructure Resilience & High Availability procedures identified that documented operating procedures governing redundancy architecture, failover operations, disaster recovery connectivity and resilience testing had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Infrastructure Resilience & High Availability documentation identified absence of version-controlled enterprise standards governing high-availability architecture, gateway redundancy, resilient WAN connectivity, disaster recovery networking and automated failover validation.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that network architects, infrastructure engineers, platform administrators and Information Security personnel were not periodically provided technical awareness training on high-availability design principles, resilience engineering practices and enterprise disaster recovery architecture.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic architecture assurance reviews evaluating compliance of implemented resilience mechanisms against approved enterprise high-availability standards were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise resilience metrics covering single points of failure, high-availability coverage, failover validation results, disaster recovery readiness and unresolved infrastructure resilience risks were not periodically reported to senior management for governance oversight.",
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
    [existing_df, new_df], ignore_index=True
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
print("SNA Infrastructure Resilience & High Availability Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")