"""
=============================================================
Certificate Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Certificate Management observations
into the central Observation Repository.

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

DOMAIN = "Certificate Management"
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
# Certificate Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of certificate inventory records identified that digital certificates deployed across production environments were not maintained within a centralized certificate inventory. Absence of centralized certificate tracking increases the likelihood of expired or unmanaged certificates remaining undetected.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of TLS certificate lifecycle identified that multiple externally exposed application certificates were renewed after expiration, contrary to the Enterprise PKI Standard requiring certificate renewal prior to expiry. Delayed certificate renewal may result in service disruption and weakened trust relationships.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of certificate issuance procedures identified that digital certificate requests were approved without independent verification of requester authorization. Inadequate validation during certificate issuance increases the risk of unauthorized certificate generation.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of certificate deployment identified that self-signed certificates were used within production applications instead of certificates issued by approved Certification Authorities (CAs). Use of self-signed certificates may weaken trust validation and expose communications to impersonation risks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of certificate revocation procedures identified that revoked certificates were not periodically validated using Certificate Revocation Lists (CRL) or Online Certificate Status Protocol (OCSP). Failure to validate certificate revocation status may allow continued use of compromised certificates.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of certificate administration identified that private keys associated with production TLS certificates were stored outside approved secure cryptographic repositories, contrary to the Enterprise Certificate Management Standard. Inadequate private key protection increases the risk of certificate compromise.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Public Key Infrastructure (PKI) governance identified that subordinate Certification Authority (CA) certificates had not undergone periodic security review to validate continued operational necessity and trust relationships.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of certificate lifecycle management identified that expired digital certificates remained deployed within production environments without documented risk acceptance or timely replacement, increasing the likelihood of application service disruption.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of certificate inventory identified that ownership information for production certificates was not consistently maintained within the centralized certificate repository.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of certificate renewal procedures identified that automated notification mechanisms for impending certificate expiry were not configured for critical production certificates.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of certificate lifecycle records identified that certificate validity periods exceeded the organization's approved Certificate Management Standard without documented risk assessment.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of certificate issuance logs identified that certificate requests and approvals were not consistently retained for audit trail and forensic purposes.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of enterprise PKI governance identified that periodic reconciliation between deployed certificates and the approved certificate inventory was not performed.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of certificate monitoring identified that unauthorized certificate installation within production servers was not detected through centralized security monitoring mechanisms.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Certificate Management governance identified that periodic review of enterprise PKI standards was not performed to incorporate evolving cryptographic recommendations and regulatory requirements.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of certificate lifecycle records identified that certificate renewal activities were not completed sufficiently in advance of certificate expiry, contrary to the Enterprise Certificate Management Standard. Delayed renewal activities increase the likelihood of unexpected production service interruptions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of certificate deployment identified that wildcard certificates were extensively deployed across unrelated production applications without documented risk assessment or management approval. Excessive reliance on wildcard certificates may increase the impact of certificate compromise.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of certificate configuration identified that deprecated signature algorithms were used for production digital certificates despite availability of stronger enterprise-approved cryptographic algorithms. Continued use of obsolete algorithms may weaken certificate trust and cryptographic assurance.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of certificate administration identified that certificate private keys associated with retired certificates were retained beyond the approved retention period without documented business justification.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of certificate request procedures identified that certificate requests submitted by application administrators were not independently verified prior to approval, reducing segregation of duties within the certificate issuance process.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of enterprise PKI operations identified that Certificate Revocation Lists (CRLs) were not periodically validated for successful publication across all production environments.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Online Certificate Status Protocol (OCSP) configuration identified that certificate status validation was not enabled for externally accessible production applications, reducing the effectiveness of certificate revocation verification.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of certificate governance identified that certificate exceptions approved for legacy applications were not periodically reviewed to determine continued business necessity or migration planning.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of certificate monitoring reports identified that unauthorized certificate modifications and replacements were not continuously monitored through centralized security monitoring mechanisms.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise dashboards summarizing certificate expiry status, renewal compliance and PKI health were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Certificate Management procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Certificate Management documentation identified absence of version-controlled Enterprise PKI standards aligned with the current technology landscape and regulatory requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that PKI administrators and certificate custodians were not periodically provided awareness training on enterprise certificate lifecycle management requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Certificate Management activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Certificate Management Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("Certificate Management Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")