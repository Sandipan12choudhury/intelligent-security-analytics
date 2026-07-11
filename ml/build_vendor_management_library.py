"""
=============================================================
Third-Party / Vendor Management Observation Library Builder
=============================================================

Purpose:
--------
Append enterprise-grade Third-Party / Vendor Management
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

DOMAIN = "Third-Party / Vendor Management"
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
# Third-Party / Vendor Management Observations
# ============================================================

OBSERVATIONS = [

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of vendor onboarding records identified that security due diligence was not performed prior to onboarding third-party service providers supporting critical production applications. Absence of security due diligence may expose the organization to unmanaged third-party cyber security risks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of third-party risk assessment reports identified that periodic security risk assessments for critical vendors were not performed in accordance with organizational requirements. Failure to periodically reassess vendor risks may result in emerging security threats remaining unidentified.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of vendor access records identified that privileged access granted to third-party personnel was not periodically reviewed or recertified. Unnecessary third-party privileged access may increase the risk of unauthorized activities within the production environment.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of contractual agreements identified that security responsibilities, incident reporting requirements and information protection obligations were not explicitly defined for critical third-party service providers. Inadequate contractual security clauses may weaken accountability during security incidents.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of third-party compliance records identified that independent security assurance reports such as SOC reports or equivalent assessments were not obtained for vendors hosting or processing sensitive organizational information.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of vendor management records identified that terminated vendors continued to retain active logical access to enterprise systems beyond contract termination dates. Delayed revocation of vendor access may increase the organization's exposure to unauthorized access.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of outsourced service governance identified that critical vendors were not included within the enterprise cyber security monitoring and risk management program. Limited oversight may reduce visibility into vendor-related cyber risks.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of vendor security exception records identified that high-risk third-party security observations remained open beyond approved remediation timelines without documented management approval or compensating controls.",
        "Severity": "High"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of vendor inventory identified that the centralized register of third-party service providers was not periodically reviewed to ensure completeness and accuracy.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of confidentiality agreements identified that Non-Disclosure Agreements (NDAs) were not available for all third-party personnel with access to sensitive organizational information.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of vendor onboarding procedures identified that background verification requirements for vendor personnel were not consistently documented prior to granting system access.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of vendor performance reports identified that security-related Service Level Agreements (SLAs) were not periodically monitored for compliance.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of vendor access management identified that shared accounts were used by third-party support personnel instead of uniquely identifiable user accounts, reducing accountability.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of vendor governance identified that periodic meetings to review cyber security risks associated with critical vendors were not evidenced.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of vendor risk registers identified that identified security risks associated with third-party providers were not periodically reviewed until formal closure.",
        "Severity": "Medium"
    },

        {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of vendor security assessments identified that remediation status of observations reported during previous security assessments was not validated prior to renewal of vendor engagements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of third-party monitoring reports identified that cyber security incidents affecting critical vendors were not periodically reviewed to evaluate potential impact on enterprise applications.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of vendor access records identified that privileged sessions established by third-party administrators were not monitored or logged through centralized privileged session monitoring mechanisms.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of vendor compliance documentation identified that periodic certification of compliance with organizational information security requirements was not obtained from critical third-party service providers.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of third-party governance identified that vendor-owned infrastructure supporting production applications was not periodically reviewed for compliance with enterprise security baseline requirements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of vendor lifecycle management identified that security requirements were not consistently incorporated during renewal or extension of third-party service agreements.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Analysis of vendor performance reports identified recurring non-compliance with agreed security Service Level Agreements (SLAs) without documented corrective action plans or management escalation.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of vendor access governance identified that dormant third-party user accounts were not periodically identified and disabled following prolonged inactivity.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of outsourced service governance identified that security responsibilities between internal teams and external service providers were not formally documented through a RACI matrix or equivalent governance mechanism.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Verification of management reporting identified that periodic dashboards summarizing vendor cyber security posture, open risks and compliance status were not presented to senior management for governance review.",
        "Severity": "Medium"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Assessment of Third-Party Management procedures identified that documented operating procedures had not undergone periodic review and management approval.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of vendor governance documentation identified absence of version-controlled Third-Party Management procedures aligned with current enterprise security practices.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Validation of awareness records identified that personnel responsible for vendor governance were not periodically provided training on third-party cyber risk management requirements.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Inspection of governance records identified that periodic internal quality assurance reviews over Third-Party Management activities were not evidenced.",
        "Severity": "Low"
    },

    {
        "Activity": ACTIVITY,
        "Domain": DOMAIN,
        "Observation":
        "Review of management reporting identified that enterprise Third-Party Risk Management Key Performance Indicators (KPIs) were not periodically reported to senior management for governance oversight.",
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
print("Third-Party / Vendor Management Library Created Successfully")
print("===================================================")

print(f"\nDomain                  : {DOMAIN}")

print(f"Existing Observations   : {existing_count}")

print(f"New Observations        : {len(new_df)}")

print(f"Duplicates Removed      : {duplicates_removed}")

print(f"Final Repository Size   : {len(combined_df)}")

print(f"\nRepository Updated :\n{DATASET_FILE}")