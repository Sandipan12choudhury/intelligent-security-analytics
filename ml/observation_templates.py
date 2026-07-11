"""
============================================================
Observation Template Engine
============================================================

Purpose:
Store standardized observation-writing templates derived
from real security review observations.

These templates are used for generating enterprise-grade
synthetic observations across:

1. ITGC
2. DB
3. DFRA
4. DFA
5. SNA

Observation Quality Benchmark:

Tier 1:
Evidence + Validation + Gap + Risk

Tier 2:
Evidence + Gap + Limited Risk

Tier 3:
Gap + Minimal Explanation
============================================================
"""

# ============================================================
# ITGC Templates
# ============================================================

ITGC_TEMPLATES = {

    "tier1": [
        "Review of {evidence} indicates that {gap}. Absence of {control} increases the risk of {risk}.",

        "During the review of {evidence}, it was observed that {gap}. This may result in {risk}.",

        "Validation of {evidence} identified that {gap}. Lack of {control} may expose the application to {risk}.",

        "Review of submitted evidences indicates that {gap}. Failure to implement {control} may increase the likelihood of {risk}."
    ],

    "tier2": [
        "During review of {evidence}, it was observed that {gap}.",

        "Review of {evidence} indicates that {gap}, which may result in control weaknesses.",

        "The submitted evidences indicate that {gap}.",

        "It was observed that {gap} during review of {evidence}."
    ],

    "tier3": [
        "{gap}.",

        "{control} was not evidenced during review.",

        "Required evidences for {control} were not made available.",

        "{gap} was observed."
    ]
}

# ============================================================
# DATABASE REVIEW TEMPLATES
# ============================================================

DB_TEMPLATES = {

    "tier1": [
        "Review of {configuration} indicates that {gap}. This may result in {risk}.",

        "Analysis of database parameter settings identified that {gap}. Lack of proper configuration may increase the risk of {risk}.",

        "Review of database security configuration shows that {gap}. This may expose the database to {risk}.",

        "Validation of database controls indicates that {gap}. Failure to implement appropriate safeguards may result in {risk}."
    ],

    "tier2": [
        "Review of database configuration indicates that {gap}.",

        "During review of database controls, it was observed that {gap}.",

        "Database review evidences indicate that {gap}.",

        "The reviewed configuration shows that {gap}."
    ],

    "tier3": [
        "{gap}.",

        "Database security evidences were not available for review.",

        "{control} was not evidenced during database review."
    ]
}

# ============================================================
# DFRA TEMPLATES
# ============================================================

DFRA_TEMPLATES = {

    "tier1": [
        "Review of {log_source} indicates that {gap}. Absence of {control} may limit forensic investigation and incident reconstruction.",

        "Analysis of audit records identified that {gap}. This may impact the organization's forensic readiness capability.",

        "Review of logging evidences indicates that {gap}. Lack of complete audit trails may hinder security investigations."
    ],

    "tier2": [
        "Review of audit logs indicates that {gap}.",

        "During review of logging controls, it was observed that {gap}.",

        "Log review evidences indicate that {gap}."
    ],

    "tier3": [
        "{gap}.",

        "Required logging evidences were not available.",

        "{control} was not evidenced."
    ]
}

# ============================================================
# DFA TEMPLATES
# ============================================================

DFA_TEMPLATES = {

    "tier1": [
        "The reviewed data flow diagram depicts {component}; however, {gap}. This limits the ability to validate security controls governing data movement.",

        "Review of the data flow diagram indicates that {gap}. Absence of this information restricts assessment of data flow security.",

        "The reviewed architecture illustrates {component}; however, {gap}, limiting validation of secure data handling practices."
    ],

    "tier2": [
        "Review of the data flow diagram indicates that {gap}.",

        "The DFD does not clearly depict {control}.",

        "During review of the DFD, it was observed that {gap}."
    ],

    "tier3": [
        "{gap}.",

        "Required data flow information was not evidenced.",

        "{control} is not represented in the reviewed DFD."
    ]
}

# ============================================================
# SNA TEMPLATES
# ============================================================

SNA_TEMPLATES = {

    "tier1": [
        "The reviewed network architecture indicates that {gap}. Absence of {control} may increase the attack surface and facilitate unauthorized lateral movement.",

        "Review of the network architecture diagram identified that {gap}. This may expose critical systems to security threats.",

        "The submitted network architecture evidences indicate that {gap}. Lack of appropriate network security controls may result in {risk}."
    ],

    "tier2": [
        "Review of network architecture indicates that {gap}.",

        "The reviewed architecture does not clearly depict {control}.",

        "During network security review, it was observed that {gap}."
    ],

    "tier3": [
        "{gap}.",

        "{control} was not evidenced in the architecture diagram.",

        "Required network security controls were not clearly depicted."
    ]
}

# ============================================================
# Template Registry
# ============================================================

TEMPLATE_REGISTRY = {
    "ITGC": ITGC_TEMPLATES,
    "DB": DB_TEMPLATES,
    "DFRA": DFRA_TEMPLATES,
    "DFA": DFA_TEMPLATES,
    "SNA": SNA_TEMPLATES
}

# ============================================================
# ITGC - USER MANAGEMENT KNOWLEDGE BASE
# ============================================================

USER_MANAGEMENT_KNOWLEDGE_BASE = {

    "evidence": [

        "user access review records",
        "quarterly access recertification records",
        "privileged user review evidences",
        "user provisioning records",
        "user de-provisioning records",
        "access control matrices",
        "role assignment records",
        "joiner-mover-leaver records",
        "identity management reports",
        "user entitlement reports",
        "access governance reports",
        "administrative account inventories"

    ],

    "controls": [

        "periodic user access reviews",
        "privileged account recertification",
        "timely user de-provisioning",
        "role-based access control",
        "access governance controls",
        "user lifecycle management",
        "least privilege principles",
        "segregation of duties controls",
        "user entitlement validation",
        "administrative account monitoring"

    ],

    "gaps": [

        "periodic access reviews are not performed",
        "privileged accounts are not periodically recertified",
        "dormant user accounts remain active",
        "terminated user accounts are not disabled promptly",
        "user entitlement reviews are not evidenced",
        "role assignments are not formally approved",
        "access requests are implemented without documented authorization",
        "administrative accounts are not periodically reviewed",
        "user access matrices are outdated",
        "privileged access inventories are incomplete",
        "duplicate user accounts exist within the environment",
        "inactive accounts remain enabled beyond acceptable timelines",
        "user access ownership has not been formally assigned",
        "generic user accounts are being utilized",
        "shared administrative accounts are in use",
        "temporary access is not revoked after expiry",
        "joiner-mover-leaver procedures are not consistently followed",
        "user access reviews exclude privileged accounts",
        "evidence of user recertification could not be provided",
        "orphaned accounts were identified during review"

    ],

    "risks": [

        "unauthorized access remaining undetected",
        "privilege misuse by internal users",
        "unauthorized transactions",
        "fraudulent activities",
        "data confidentiality breaches",
        "violation of least privilege principles",
        "excessive access accumulation",
        "regulatory non-compliance",
        "unauthorized system modifications",
        "elevated insider threat exposure",
        "segregation of duties conflicts",
        "security incidents caused by excessive privileges"

    ]
}
# ============================================================
# USER MANAGEMENT SEVERITY MAPPING
# ============================================================

USER_MANAGEMENT_SEVERITY = {

    "High": [
        "privileged accounts are not periodically recertified",
        "terminated user accounts are not disabled promptly",
        "shared administrative accounts are in use",
        "generic user accounts are being utilized",
        "user access reviews exclude privileged accounts",
        "orphaned accounts were identified during review"
    ],

    "Medium": [
        "periodic access reviews are not performed",
        "user entitlement reviews are not evidenced",
        "administrative accounts are not periodically reviewed",
        "privileged access inventories are incomplete",
        "inactive accounts remain enabled beyond acceptable timelines",
        "temporary access is not revoked after expiry",
        "joiner-mover-leaver procedures are not consistently followed"
    ],

    "Low": [
        "user access matrices are outdated",
        "user access ownership has not been formally assigned",
        "evidence of user recertification could not be provided",
        "role assignments are not formally approved"
    ]
}
# ============================================================
# USER MANAGEMENT OBSERVATION SCENARIOS
# ============================================================

USER_MANAGEMENT_SCENARIOS = [

    {
        "evidence":
            "quarterly privileged access review records",

        "gap":
            "privileged accounts are not periodically recertified",

        "control":
            "periodic privileged access reviews",

        "risk":
            "unauthorized privileged access remaining undetected",

        "severity":
            "High"
    },

    {
        "evidence":
            "user de-provisioning records",

        "gap":
            "terminated user accounts are not disabled promptly",

        "control":
            "timely user de-provisioning",

        "risk":
            "unauthorized access by former employees",

        "severity":
            "High"
    },

    {
        "evidence":
            "administrative account inventories",

        "gap":
            "shared administrative accounts are in use",

        "control":
            "individual accountability controls",

        "risk":
            "inability to attribute privileged activities",

        "severity":
            "High"
    },

    {
        "evidence":
            "access governance reports",

        "gap":
            "user access reviews exclude privileged accounts",

        "control":
            "comprehensive access recertification",

        "risk":
            "excessive privileges remaining undetected",

        "severity":
            "High"
    },

    {
        "evidence":
            "identity management reports",

        "gap":
            "orphaned accounts were identified during review",

        "control":
            "user lifecycle management",

        "risk":
            "unauthorized system access",

        "severity":
            "High"
    },

    {
        "evidence":
            "user access review records",

        "gap":
            "periodic access reviews are not performed",

        "control":
            "user access recertification",

        "risk":
            "excessive access accumulation",

        "severity":
            "Medium"
    },

    {
        "evidence":
            "user entitlement reports",

        "gap":
            "user entitlement reviews are not evidenced",

        "control":
            "access governance controls",

        "risk":
            "inappropriate access assignments",

        "severity":
            "Medium"
    },

    {
        "evidence":
            "administrative account inventories",

        "gap":
            "administrative accounts are not periodically reviewed",

        "control":
            "privileged access governance",

        "risk":
            "privilege misuse",

        "severity":
            "Medium"
    },

    {
        "evidence":
            "privileged user review evidences",

        "gap":
            "privileged access inventories are incomplete",

        "control":
            "privileged account management",

        "risk":
            "untracked privileged access",

        "severity":
            "Medium"
    },

    {
        "evidence":
            "joiner-mover-leaver records",

        "gap":
            "temporary access is not revoked after expiry",

        "control":
            "temporary access management",

        "risk":
            "continued unauthorized access",

        "severity":
            "Medium"
    },

    {
        "evidence":
            "access control matrices",

        "gap":
            "user access matrices are outdated",

        "control":
            "access matrix maintenance",

        "risk":
            "inaccurate access governance records",

        "severity":
            "Low"
    },

    {
        "evidence":
            "role assignment records",

        "gap":
            "role assignments are not formally approved",

        "control":
            "role approval workflow",

        "risk":
            "inappropriate role assignment",

        "severity":
            "Low"
    },

    {
        "evidence":
            "quarterly access recertification records",

        "gap":
            "evidence of user recertification could not be provided",

        "control":
            "access recertification process",

        "risk":
            "control effectiveness cannot be validated",

        "severity":
            "Low"
    }
]

USER_MANAGEMENT_ADVANCED_SCENARIOS = [

    {
        "review":
            "quarterly privileged access review records",

        "scope":
            "for production support administrators",

        "gap":
            "could not be provided during review",

        "impact":
            "which may result in excessive privileged access remaining undetected",

        "severity":
            "High"
    },

    {
        "review":
            "user de-provisioning evidences",

        "scope":
            "for terminated employees",

        "gap":
            "indicate that user accounts remain active beyond defined timelines",

        "impact":
            "which may result in unauthorized access by former employees",

        "severity":
            "High"
    },

    {
        "review":
            "administrative account inventories",

        "scope":
            "for critical production systems",

        "gap":
            "indicate usage of shared administrative IDs",

        "impact":
            "which may impact accountability and audit traceability",

        "severity":
            "High"
    },

    {
        "review":
            "access governance reports",

        "scope":
            "for privileged accounts",

        "gap":
            "indicate that periodic access recertification is not performed",

        "impact":
            "which may result in accumulation of excessive privileges",

        "severity":
            "High"
    },

    {
        "review":
            "identity management reports",

        "scope":
            "for active users",

        "gap":
            "identified orphan accounts without valid ownership",

        "impact":
            "which may expose the application to unauthorized access",

        "severity":
            "High"
    },

    {
        "review":
            "user entitlement reports",

        "scope":
            "for business users",

        "gap":
            "indicate that entitlement reviews are not evidenced",

        "impact":
            "which may result in inappropriate access assignments",

        "severity":
            "Medium"
    },

    {
        "review":
            "role assignment records",

        "scope":
            "for application administrators",

        "gap":
            "indicate absence of formal approval workflow",

        "impact":
            "which may impact access governance effectiveness",

        "severity":
            "Medium"
    },

    {
        "review":
            "temporary access management records",

        "scope":
            "for vendor users",

        "gap":
            "indicate that temporary access remains active beyond expiry",

        "impact":
            "which may result in continued unauthorized access",

        "severity":
            "Medium"
    },

    {
        "review":
            "user access matrices",

        "scope":
            "for application support teams",

        "gap":
            "were found to be outdated",

        "impact":
            "which may impact accuracy of access governance records",

        "severity":
            "Low"
    },

    {
        "review":
            "access recertification evidences",

        "scope":
            "for administrative users",

        "gap":
            "could not be provided during review",

        "impact":
            "which may limit validation of access governance controls",

        "severity":
            "Low"
    },

    {
    "review": "user access review records",
    "scope": "for dormant user accounts",
    "gap": "identified dormant accounts remaining active beyond approved timelines",
    "impact": "which may result in unauthorized access through unused accounts",
    "severity": "High"
     },

     {
    "review": "identity management reports",
    "scope": "for privileged users",
    "gap": "identified duplicate user IDs assigned to the same individual",
    "impact": "which may weaken accountability and access traceability",
    "severity": "High"
    },

    {
    "review": "access governance reports",
    "scope": "for application administrators",
    "gap": "identified excessive privileges assigned beyond business requirements",
    "impact": "which may increase insider threat exposure",
    "severity": "High"
    },

    {
    "review": "user provisioning records",
    "scope": "for newly onboarded users",
    "gap": "indicate that user access is provisioned without documented approval",
    "impact": "which may result in unauthorized access assignments",
    "severity": "High"
    },
 
    {
    "review": "service account inventories",
    "scope": "for production environments",
    "gap": "identified service accounts without designated ownership",
    "impact": "which may result in unauthorized activities remaining undetected",
    "severity": "High"
    },

    {
    "review": "vendor access records",
    "scope": "for third-party support personnel",
    "gap": "identified active vendor accounts without periodic review",
    "impact": "which may increase exposure to external threats",
    "severity": "High"
    },

    {
    "review": "privileged account inventories",
    "scope": "for database administrators",
    "gap": "identified privileged accounts not mapped to approved personnel",
    "impact": "which may result in unauthorized privileged access",
    "severity": "High"
    },

    {
    "review": "joiner-mover-leaver records",
    "scope": "for transferred employees",
    "gap": "indicate that previous access rights remain active after role changes",
    "impact": "which may lead to excessive privilege accumulation",
    "severity": "High"
    },

    {
    "review": "user entitlement reports",
    "scope": "for business users",
    "gap": "identified segregation of duties conflicts across critical functions",
    "impact": "which may increase the risk of fraudulent activities",
    "severity": "High"
    },

    {
    "review": "emergency access management records",
    "scope": "for break-glass accounts",
    "gap": "indicate that emergency access usage is not periodically reviewed",
    "impact": "which may result in misuse of privileged access",
    "severity": "High"
    },

    {
    "review": "user access review records",
    "scope": "for application support users",
    "gap": "indicate that periodic access certification is not consistently performed",
    "impact": "which may result in inappropriate access remaining undetected",
    "severity": "Medium"
    },

    {
    "review": "role assignment records",
    "scope": "for operational users",
    "gap": "identified role assignments without supporting business justification",
    "impact": "which may impact effectiveness of access governance controls",
    "severity": "Medium"
    },

    {
    "review": "identity management reports",
    "scope": "for temporary users",
    "gap": "identified temporary accounts remaining active beyond approved validity periods",
    "impact": "which may result in continued unauthorized access",
    "severity": "Medium"
    },

    {
    "review": "access governance reports",
    "scope": "for privileged users",
    "gap": "indicate that user entitlement reviews are performed inconsistently",
    "impact": "which may impact effectiveness of periodic access reviews",
    "severity": "Medium"
    },

    {
    "review": "administrative account inventories",
    "scope": "for infrastructure administrators",
    "gap": "identified incomplete inventory of administrative accounts",
    "impact": "which may result in unmanaged privileged access",
    "severity": "Medium"
    },

    {
    "review": "user provisioning records",
    "scope": "for contractor accounts",
    "gap": "identified delays in access revocation after contract completion",
    "impact": "which may increase risk of unauthorized access",
    "severity": "Medium"
    },

    {
    "review": "user access matrices",
    "scope": "for critical applications",
    "gap": "indicate that access matrices are not periodically updated",
    "impact": "which may affect accuracy of access governance records",
    "severity": "Medium"
    },

    {
    "review": "service account inventories",
    "scope": "for application services",
    "gap": "identified service accounts without periodic review",
    "impact": "which may result in unmanaged access privileges",
    "severity": "Medium"
    },

    {
    "review": "vendor access review reports",
    "scope": "for outsourced support teams",
    "gap": "indicate that vendor access reviews are not evidenced",
    "impact": "which may increase exposure to third-party risks",
    "severity": "Medium"
    },

    {
    "review": "role ownership records",
    "scope": "for application roles",
    "gap": "identified roles without formally assigned owners",
    "impact": "which may impact periodic access governance activities",
    "severity": "Medium"
    },

    {
    "review": "access matrix documentation",
    "scope": "for business applications",
    "gap": "was not updated to reflect recent organizational changes",
    "impact": "which may result in inaccurate role definitions",
    "severity": "Low"
    },

    {
    "review": "user entitlement documentation",
    "scope": "for operational users",
    "gap": "could not be provided during review",
    "impact": "which may limit validation of access assignments",
    "severity": "Low"
    },

    {
    "review": "access certification reports",
    "scope": "for business users",
    "gap": "were maintained manually without documented review workflow",
    "impact": "which may affect reliability of review records",
    "severity": "Low"
    },

    {
    "review": "role management documentation",
    "scope": "for application users",
    "gap": "indicate absence of formally documented role definitions",
    "impact": "which may affect consistency of access assignments",
    "severity": "Low"
    },

    {
    "review": "user access governance procedures",
    "scope": "for critical applications",
    "gap": "could not be evidenced during review",
    "impact": "which may limit assessment of governance effectiveness",
    "severity": "Low"
    }

]

# ============================================================
# OBSERVATION CONTEXT LIBRARY
# ============================================================

REVIEW_CONTEXT = [

    "Review of submitted evidences",
    "Review of quarterly access recertification records",
    "Review of user entitlement reports",
    "Review of privileged access review records",
    "Review of administrative account inventories",
    "Review of access governance reports",
    "Review of identity management reports",
    "Review of user provisioning records",
    "Review of user de-provisioning records",
    "Review of role assignment records"

]

# ============================================================

SCOPE_CONTEXT = [

    "for active privileged accounts",
    "for administrative users",
    "for production environment users",
    "for application support accounts",
    "for vendor accounts",
    "for temporary access users",
    "for service accounts",
    "for database administrators",
    "for application administrators",
    "for critical business users"

]

# ============================================================

IMPACT_CONTEXT = [

    "which may result in unauthorized access",
    "which may lead to privilege misuse",
    "which may expose sensitive information",
    "which may increase insider threat exposure",
    "which may result in unauthorized system modifications",
    "which may increase the likelihood of fraudulent activities",
    "which may lead to regulatory non-compliance",
    "which may result in excessive privilege accumulation",
    "which may increase the risk of data confidentiality breaches",
    "which may impact overall access governance effectiveness"

]
print("Observation Template Engine Loaded Successfully")