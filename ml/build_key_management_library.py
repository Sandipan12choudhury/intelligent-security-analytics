"""
=============================================================
Cryptographic Key Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Cryptographic Key Management
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

DOMAIN = "Cryptographic Key Management"
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
# Cryptographic Key Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of cryptographic key lifecycle records identified that encryption keys protecting sensitive production data had not been rotated within the intervals prescribed by the Enterprise Cryptographic Key Management Standard. Continued use of long-lived cryptographic keys may increase the likelihood of key compromise and unauthorized disclosure of sensitive information.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Hardware Security Module (HSM) administration identified that master cryptographic keys were generated outside certified HSM infrastructure, contrary to the approved Key Management Standard. Generation of master keys outside secure cryptographic modules increases the risk of key exposure.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of encryption key storage mechanisms identified that application encryption keys were stored in plaintext configuration files instead of approved secure key repositories or Hardware Security Modules. Insecure key storage significantly increases the risk of unauthorized key disclosure.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of cryptographic key access records identified that privileged administrators possessed unrestricted access to production encryption keys without implementation of dual control or split knowledge principles. Inadequate segregation of key custodians may increase the risk of unauthorized cryptographic operations.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of cryptographic key backup procedures identified that backup copies of master encryption keys were maintained without documented encryption or secure storage controls. Inadequate protection of backup keys may compromise the confidentiality of encrypted enterprise information.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of cryptographic key destruction records identified that retired encryption keys were not securely destroyed following completion of their operational lifecycle. Retention of obsolete cryptographic keys may increase the risk of unauthorized data decryption.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of cryptographic key usage identified that identical encryption keys were reused across multiple production applications without documented risk assessment or management approval. Shared cryptographic keys increase the potential impact of key compromise across enterprise systems.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of key management governance identified that cryptographic keys protecting payment-related information were not periodically reviewed for compliance with approved cryptographic standards and regulatory requirements.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of key inventory records identified that the centralized inventory of production cryptographic keys was not periodically reconciled with deployed enterprise applications.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of key custodianship identified that designated key custodians had not formally acknowledged responsibility for management of production cryptographic keys.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of cryptographic key generation records identified that cryptographic key lengths and algorithms were not consistently aligned with the approved Enterprise Cryptographic Standard.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of cryptographic key escrow procedures identified that secure escrow arrangements for critical encryption keys had not been documented or periodically validated.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of key lifecycle documentation identified that ownership, activation, suspension and retirement dates for production cryptographic keys were not consistently maintained.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of cryptographic key monitoring identified that privileged activities involving key generation, export, import and deletion were not continuously monitored through centralized security logging mechanisms.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of cryptographic governance identified that periodic reviews of enterprise cryptographic standards were not performed to incorporate changes in regulatory requirements, industry standards and emerging cryptographic threats.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Hardware Security Module (HSM) administration identified that periodic health checks and integrity validation of HSM appliances were not performed in accordance with the Enterprise Cryptographic Standard. Failure to verify HSM integrity may impact the confidentiality and availability of enterprise cryptographic operations.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of cryptographic key rotation records identified that emergency cryptographic key replacement procedures were not defined for suspected or confirmed key compromise events. Absence of emergency key replacement procedures may delay containment of cryptographic security incidents.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of cryptographic key usage identified that encryption keys were utilized beyond their approved cryptographic validity period without documented risk assessment or management approval.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application secret management identified that API secrets, database credentials and application encryption keys were maintained within application source code repositories instead of approved enterprise secret management solutions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of key distribution procedures identified that cryptographic keys were transmitted between environments without implementation of secure key exchange mechanisms approved under the Enterprise Cryptographic Standard.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of cryptographic key access reviews identified that periodic recertification of personnel authorized to manage production cryptographic keys was not evidenced.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of cryptographic configuration identified that deprecated encryption algorithms and key lengths remained enabled within production environments despite availability of stronger enterprise-approved cryptographic standards.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of cryptographic audit logs identified that privileged cryptographic operations including key export, key recovery and master key activation were not periodically reviewed by independent personnel.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of cryptographic governance identified that third-party service providers responsible for managing enterprise encryption keys were not periodically assessed for compliance with organizational cryptographic security requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that periodic dashboards summarizing cryptographic key lifecycle status, key rotation compliance and cryptographic control effectiveness were not presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Cryptographic Key Management procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Cryptographic Key Management documentation identified absence of version-controlled cryptographic standards aligned with the current enterprise technology landscape and regulatory requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that key custodians and cryptographic administrators were not periodically provided awareness training on enterprise cryptographic key management requirements and secure key handling practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Cryptographic Key Management activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Cryptographic Key Management Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("Cryptographic Key Management Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")