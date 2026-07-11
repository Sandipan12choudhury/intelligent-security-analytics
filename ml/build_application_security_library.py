"""
=============================================================
Application Security Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Application Security Management
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

DOMAIN = "Application Security Management"
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
# Application Security Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Secure Software Development Life Cycle (SSDLC) practices identified that security requirements were not formally incorporated into application design and development activities. Absence of security-by-design principles increases the likelihood of introducing exploitable vulnerabilities into production applications.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application authentication controls identified that privileged application accounts were not protected using Multi-Factor Authentication (MFA), contrary to the Enterprise Application Security Standard. Weak authentication mechanisms increase the risk of unauthorized access to critical business functions.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application secret management identified that database credentials, encryption keys and API secrets were embedded within application configuration files instead of approved enterprise secret management solutions. Insecure storage of application secrets increases the likelihood of credential compromise.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of secure coding practices identified that mandatory secure code reviews were not performed prior to deployment of production application releases. Absence of secure code review increases the probability of introducing security vulnerabilities into production environments.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application security testing identified that periodic Dynamic Application Security Testing (DAST) and Static Application Security Testing (SAST) were not performed before production deployment. Failure to identify application vulnerabilities prior to release may expose critical business applications to cyber attacks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of session management controls identified that application sessions remained active beyond the approved inactivity timeout defined within the Enterprise Application Security Standard. Excessive session duration increases the risk of unauthorized session hijacking.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application input validation identified that server-side validation controls were not consistently implemented for user-supplied input parameters. Insufficient input validation increases exposure to injection attacks and application compromise.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application governance identified that critical application security exceptions remained active beyond approved review timelines without documented risk acceptance or compensating security controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of application hardening identified that unnecessary application modules and services remained enabled within the production environment without documented business justification.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application authentication identified that password complexity and account lockout controls configured within the application were not periodically validated against enterprise security standards.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application session management identified that secure cookie attributes including HttpOnly and Secure flags were not consistently configured for authenticated application sessions.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application security testing identified that identified vulnerabilities from previous security assessments were not consistently revalidated following remediation activities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of application logging identified that security-relevant application events including authentication failures and privilege changes were not consistently generated for centralized monitoring.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application dependency management identified that third-party software libraries and frameworks used within production applications were not periodically reviewed for publicly disclosed security vulnerabilities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of Application Security governance identified that the Enterprise Application Security Standard had not undergone periodic review to incorporate evolving regulatory requirements, secure development practices and emerging cyber threats.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of secure software development governance identified that threat modeling exercises were not performed during the design phase for newly developed or significantly modified enterprise applications. Absence of structured threat modeling may result in security weaknesses remaining unidentified before implementation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application authentication identified that inactive application user sessions were not automatically invalidated following password changes or account disablement, increasing the risk of unauthorized session reuse.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application authorization controls identified that role-based access permissions were not periodically reviewed to validate alignment with current business responsibilities and the principle of least privilege.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application deployment identified that debug interfaces, verbose error messages and diagnostic functions remained enabled within production environments without documented business justification. Exposure of diagnostic information may assist attackers in identifying application weaknesses.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of application configuration identified that Cross-Origin Resource Sharing (CORS) policies were not periodically reviewed to ensure that access was restricted to authorized domains only. Overly permissive CORS configurations may expose sensitive application resources to unauthorized origins.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of application security testing identified that remediation of vulnerabilities detected during penetration testing was not consistently verified through independent retesting prior to production deployment.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of application dependency management identified that open-source software components were not continuously monitored for newly disclosed Common Vulnerabilities and Exposures (CVEs), increasing the likelihood of vulnerable components remaining in production.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of application monitoring identified that repeated application security events including authentication failures, privilege escalations and access violations were not subjected to periodic trend analysis and Root Cause Analysis (RCA).",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of application documentation identified that ownership information for production application security controls was not consistently maintained, reducing accountability for periodic security reviews and remediation activities.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that dashboards summarizing application security posture, unresolved vulnerabilities, secure code review status and security testing coverage were not periodically presented to Information Security management.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of Application Security Management procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Application Security Management documentation identified absence of version-controlled application security standards aligned with the current enterprise application landscape and regulatory requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of awareness records identified that software developers, application administrators and quality assurance personnel were not periodically provided awareness training on secure coding practices, OWASP guidance and enterprise application security requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Application Security Management activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Application Security Management Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("Application Security Management Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")
print(f"Existing Observations   : {existing_count}")
print(f"New Observations        : {len(new_df)}")
print(f"Duplicates Removed      : {duplicates_removed}")
print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")