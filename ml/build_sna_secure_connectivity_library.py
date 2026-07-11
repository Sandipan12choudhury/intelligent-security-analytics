"""
=============================================================
SNA Secure Connectivity & Communication
Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Secure Connectivity &
Communication observations into the central
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

DOMAIN = "Secure Connectivity & Communication"
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
# Secure Connectivity & Communication
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of enterprise communication architecture identified that administrative connectivity to critical infrastructure devices relied upon legacy management protocols without documented migration to encrypted protocols such as Secure Shell (SSH) or equivalent secure management mechanisms, increasing exposure of privileged administrative sessions.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of remote access architecture identified that privileged administrative access to production infrastructure was permitted without traversal through dedicated VPN termination points protected by multi-factor authentication, certificate-based device validation or privileged access management controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application communication architecture identified that server-to-server communication carrying confidential business information was not documented as using mutual Transport Layer Security (mTLS) authentication or equivalent certificate-based trust mechanisms, increasing exposure to unauthorized service impersonation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of enterprise network communication identified that critical application traffic traversing untrusted or shared network segments was not documented as being protected through current cryptographic protocols supporting confidentiality, integrity and authenticity of transmitted information.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of secure communication architecture identified that certificate lifecycle management processes governing issuance, renewal, revocation and retirement of certificates supporting production communication channels were not documented within the enterprise architecture.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of enterprise communication architecture identified that network management protocols supporting monitoring and administration of critical infrastructure were configured using legacy or unauthenticated communication mechanisms rather than secure protocol implementations providing encryption and integrity protection.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of routing architecture identified that dynamic routing communication between enterprise network devices was not documented as employing authenticated routing exchanges or equivalent integrity protection mechanisms to reduce exposure to route manipulation attacks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of remote connectivity identified that third-party administrative access to enterprise infrastructure traversed shared communication paths without dedicated secure access gateways, session isolation or continuous monitoring of privileged remote activities.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of communication security identified that machine-to-machine communication supporting critical enterprise services relied upon shared trust relationships without documented implementation of certificate-based authentication or equivalent cryptographic identity verification.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of secure communication identified that enterprise DNS, directory services or authentication infrastructure communication paths were not documented with associated encryption requirements, integrity controls or authentication mechanisms.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise communication architecture identified that network time synchronization supporting security monitoring, authentication services and forensic investigations was not documented with authenticated time synchronization mechanisms where applicable.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of secure connectivity identified that communication between hybrid infrastructure environments, including on-premises and cloud-hosted services, was not documented with corresponding encryption standards, trust relationships and secure tunnel architecture.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of enterprise communication architecture identified that periodic validation of cryptographic communication controls, certificate trust relationships and secure connectivity configurations was not performed to ensure continued compliance with enterprise security standards.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of secure communication identified that network services supporting centralized authentication, authorization and accounting were not documented with corresponding communication protection controls and resilience requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Secure Connectivity & Communication governance identified that enterprise standards governing encrypted communications, certificate-based trust, remote administrative connectivity, secure routing and cryptographic communication architecture had not undergone periodic review to address evolving cryptographic standards, emerging attack techniques and enterprise infrastructure modernization initiatives.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of enterprise communication architecture identified that application and infrastructure communication channels were not periodically validated to ensure compliance with approved Transport Layer Security (TLS) versions and enterprise cryptographic baseline requirements, increasing the risk of legacy protocol usage.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Public Key Infrastructure (PKI) governance identified that certificate revocation validation mechanisms, including Certificate Revocation Lists (CRLs) or Online Certificate Status Protocol (OCSP), were not documented for production communication channels relying on certificate-based authentication.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application communication architecture identified that certificate pinning or equivalent trust validation mechanisms were not implemented for high-risk machine-to-machine communication channels, increasing exposure to certificate spoofing and man-in-the-middle attacks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of API communication architecture identified that internal and external API traffic carrying sensitive business information was not consistently protected through encrypted transport channels with authenticated endpoints and documented cryptographic trust relationships.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of enterprise communication architecture identified that management plane communication supporting network infrastructure administration traversed shared production communication paths rather than dedicated secure management channels, increasing exposure of privileged administrative traffic.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of secure communication architecture identified that exceptions permitting use of non-standard or legacy communication protocols were not supported by documented risk assessments, compensating security controls, defined review periods or formal management approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of communication security identified that enterprise name resolution services supporting critical business applications were not documented with integrity protection mechanisms, secure resolution architecture or resilience controls appropriate to the business criticality of supported services.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of secure connectivity identified that communication paths supporting centralized logging, security monitoring and Security Information and Event Management (SIEM) platforms were not documented as employing authenticated and encrypted transmission mechanisms to preserve log integrity and confidentiality.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of enterprise architecture identified that communication channels supporting disaster recovery environments, backup infrastructure and secondary data centers were not documented with equivalent cryptographic protection and trust controls as implemented within the primary production environment.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of communication assurance identified that periodic technical validation of secure communication architecture, including certificate trust chains, encrypted transport mechanisms, authenticated routing exchanges and secure remote connectivity, was not evidenced through formal architecture assurance activities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Secure Connectivity & Communication procedures identified that documented operating procedures governing encrypted communications, certificate lifecycle management, secure remote administration and communication protocol standards had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Secure Connectivity & Communication documentation identified absence of version-controlled enterprise standards governing cryptographic communication architecture, certificate trust models, secure routing protocols and protected management plane communications.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that network architects, infrastructure engineers and Information Security personnel were not periodically provided technical awareness training on enterprise cryptographic communication standards, certificate trust management and secure communication architecture principles.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic architecture assurance reviews over Secure Connectivity & Communication controls were not evidenced to validate continued alignment with approved enterprise security architecture standards.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise metrics covering encrypted communication coverage, certificate lifecycle compliance, secure remote access posture, authenticated communication channels and unresolved communication security risks were not periodically reported to senior management for governance oversight.",
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
print("SNA Secure Connectivity & Communication Library Created Successfully")
print("===================================================")

print(f"\nActivity                : {ACTIVITY}")
print(f"Domain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")