"""
=============================================================
Password Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Password Management observations
into the central Observation Repository.

Repository:
dataset/observation_library.xlsx

This script DOES NOT overwrite the repository.

It performs:

1. Load existing repository
2. Generate Password Management observations
3. Append new observations
4. Remove duplicates
5. Save updated repository

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

DOMAIN = "Password Management"
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
# Load Existing Repository
# ============================================================

existing_df = pd.read_excel(DATASET_FILE)

existing_count = len(existing_df)


# ============================================================
# Password Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application password policy configurations identified that the minimum password length configured for user accounts was below the organization's approved security standard. Weak password length requirements increase susceptibility to brute-force attacks and unauthorized account compromise.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password complexity settings indicated that application passwords were not enforced to contain uppercase characters, lowercase characters, numeric values and special characters in accordance with organizational password management requirements. Weak complexity controls significantly reduce password strength.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password history configuration identified that previously used passwords could be reused immediately after password change. Absence of password history enforcement increases the likelihood of credential reuse and unauthorized account access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of administrative account password controls identified that privileged accounts were not subjected to enhanced password management requirements as defined within the enterprise security policy. Weak privileged credential protection increases the risk of administrative account compromise.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of service account credential management identified that passwords assigned to service accounts were configured as non-expiring without documented business justification or compensating security controls. Long-lived credentials increase exposure to unauthorized access if compromised.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password storage mechanisms identified that user credentials were protected using cryptographic algorithms that do not comply with current enterprise password protection standards. Weak credential storage mechanisms increase the risk of credential disclosure.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of authentication configurations identified that vendor-supplied default passwords associated with system accounts had not been changed following deployment. Retention of default credentials may allow unauthorized access using publicly known authentication information.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password transmission mechanisms identified that user credentials were transmitted without adequate cryptographic protection across application interfaces. Exposure of authentication credentials during transmission increases the likelihood of interception by malicious actors.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password expiry configurations identified that password validity periods exceeded the organization's approved password lifecycle requirements. Extended password lifetimes increase the window of opportunity for misuse of compromised credentials.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of account lockout configurations identified that repeated failed authentication attempts did not trigger automated account lockout controls. Absence of lockout mechanisms increases susceptibility to password guessing and brute-force attacks.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password reset procedures identified that temporary passwords generated during account recovery were not configured to expire after first successful authentication. Persistent temporary credentials weaken authentication security.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password policy implementation identified that application password parameters were not consistently aligned with enterprise information security standards across all user categories.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password reset approval records identified that password reset requests were processed without documented user identity verification procedures. Weak password reset controls increase the likelihood of unauthorized account takeover.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password synchronization controls identified that inconsistent password policies existed across integrated application environments, resulting in non-uniform authentication security.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of user authentication configurations identified that password expiry notification mechanisms were not implemented prior to credential expiration, increasing operational dependency on manual password reset requests.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password management procedures identified that password complexity requirements were not periodically reviewed to ensure alignment with evolving enterprise security standards.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password governance reports identified absence of periodic management review over password policy compliance across the application environment. Lack of governance oversight may result in ineffective enforcement of password security controls.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application configuration identified inconsistent enforcement of password policies across different user groups. Inconsistent implementation of password controls may weaken overall authentication security.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password exception records identified password policy exemptions granted without documented management approval or periodic reassessment. Uncontrolled exceptions may increase authentication-related security risks.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password administration procedures identified absence of documented monitoring over inactive password reset requests. Lack of monitoring may affect timely closure of authentication-related activities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password audit reports identified that password policy compliance was not periodically verified through independent security reviews. Lack of independent validation may reduce assurance over password control effectiveness.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of user authentication documentation identified absence of documented password management standards for application support accounts. Undefined standards may result in inconsistent password administration practices.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password lifecycle management identified that password change events were not consistently logged for security monitoring purposes. Incomplete audit trails may affect investigation of authentication-related incidents.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application password configuration identified that password expiry reminders were not periodically reviewed for operational effectiveness. Ineffective notification mechanisms may increase password reset requests.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password governance documentation identified that responsibilities for periodic password policy review were not formally assigned to designated personnel.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password management procedures identified that password policy documents were not periodically reviewed and approved in accordance with organizational governance requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password administration documentation identified that password configuration standards were not centrally maintained. Absence of centralized documentation may affect consistency of password management activities.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password governance records identified that password-related operational metrics were not periodically reported to application management. Lack of reporting may reduce management visibility over password security controls.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password policy documentation identified absence of version control and periodic review records. Lack of document governance may result in outdated password management practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of password awareness documentation identified that periodic communication of password management requirements to application users was not evidenced. Lack of user awareness may affect compliance with organizational password policies.",
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
print("Password Management Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")

print(f"Existing Observations   : {existing_count}")

print(f"New Observations        : {len(new_df)}")

print(f"Duplicates Removed      : {duplicates_removed}")

print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")