"""
===============================================================================
Project : Intelligent Security Analytics and Risk Prediction Platform

File    : build_control_library.py

Purpose
-------
Generates:

1. dataset/control_library.xlsx
2. dataset/observation_control_mapping.xlsx

Source Dataset
--------------
dataset/observation_library.xlsx

Implementation Rules
--------------------
1. observation_library.xlsx is the canonical source.
2. Traversal order is NEVER modified.
3. Activities and Domains follow the exact order present in
   observation_library.xlsx.
4. Every Observation MUST map to at least one Control.
5. Controls are reusable.
6. Duplicate controls are automatically avoided.
===============================================================================
"""

from pathlib import Path
from collections import OrderedDict
import pandas as pd

# =============================================================================
# Repository Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_DIR = PROJECT_ROOT / "dataset"

OBSERVATION_LIBRARY_PATH = DATASET_DIR / "observation_library.xlsx"

CONTROL_LIBRARY_PATH = DATASET_DIR / "control_library.xlsx"

OBSERVATION_CONTROL_MAPPING_PATH = (
    DATASET_DIR / "observation_control_mapping.xlsx"
)

# =============================================================================
# Load Observation Repository
# =============================================================================

print("=" * 80)
print("Loading Observation Repository...")
print("=" * 80)

observation_df = pd.read_excel(OBSERVATION_LIBRARY_PATH)

print("\nColumns in observation_library.xlsx:")
print(observation_df.columns.tolist())

print(f"Loaded {len(observation_df)} observations.")

# =============================================================================
# Runtime Containers
# =============================================================================

DOMAIN_CONTROLS = OrderedDict()

CONTROL_LOOKUP = OrderedDict()

CONTROL_RECORDS = []

OBSERVATION_CONTROL_MAPPING = []

NEXT_CONTROL_ID = 1

# =============================================================================
# Helper Functions
# =============================================================================

def generate_control_id():
    """
    Generates sequential Control IDs.

    CTRL-0001
    CTRL-0002
    CTRL-0003
    """

    global NEXT_CONTROL_ID

    control_id = f"CTRL-{NEXT_CONTROL_ID:04d}"

    NEXT_CONTROL_ID += 1

    return control_id


def register_domain_controls(activity, domain, controls):
    """
    Registers enterprise controls for a domain.
    """

    DOMAIN_CONTROLS[(activity, domain)] = controls


def register_all_domain_controls():
    """
    Registers controls for every Activity/Domain.
    Controls are added in the exact order of
    observation_library.xlsx.
    """

    # ======================================================================
    # DFA / DFD
    # ======================================================================

    register_domain_controls(

        "DFA / DFD",

        "DFD Governance & Change Management",

        [

            {
                "control_name": "DFD Governance Framework",
                "description":
                    "Establish and maintain governance for creation, "
                    "review, approval and lifecycle management of "
                    "enterprise Data Flow Diagrams.",
                "control_type": "Preventive"
            },

            {
                "control_name": "DFD Ownership & Accountability",
                "description":
                    "Assign accountable owners responsible for approved "
                    "Data Flow Diagrams.",
                "control_type": "Preventive"
            },

            {
                "control_name": "DFD Change Management",
                "description":
                    "Ensure architecture changes are reflected within "
                    "approved Data Flow Diagrams.",
                "control_type": "Preventive"
            },

            {
                "control_name": "DFD Periodic Review",
                "description":
                    "Review Data Flow Diagrams periodically to ensure "
                    "continued accuracy.",
                "control_type": "Detective"
            },

            {
                "control_name": "DFD Approval Workflow",
                "description":
                    "Implement formal review and approval workflow for "
                    "Data Flow Diagrams.",
                "control_type": "Preventive"
            },

            {
                "control_name": "DFD Version Control",
                "description":
                    "Maintain version history for approved Data Flow "
                    "Diagrams.",
                "control_type": "Preventive"
            },

            {
                "control_name": "DFD Documentation Standards",
                "description":
                    "Define enterprise standards for Data Flow Diagram "
                    "documentation.",
                "control_type": "Preventive"
            },

            {
                "control_name": "DFD Governance Monitoring",
                "description":
                    "Monitor adherence to DFD governance requirements.",
                "control_type": "Detective"
            }

        ]

    )

    register_domain_controls(

        "DFA / DFD",

        "Data Flow Documentation & Completeness",

        [

            {
                "control_name": "Complete Data Flow Documentation",
                "description":
                    "Maintain complete Data Flow Diagrams covering all "
                    "application components and interfaces.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Data Flow Accuracy Validation",
                "description":
                    "Validate that documented flows accurately "
                    "represent production implementation.",
                "control_type": "Detective"
            }

        ]

    )

    register_domain_controls(

        "DFA / DFD",

        "Interface & Integration Security",

        [

            {
                "control_name": "Secure Interface Management",
                "description":
                    "Implement enterprise security controls for all "
                    "application interfaces including APIs, web services, "
                    "middleware and third-party integrations.",
                "control_type": "Preventive"
            },

            {
                "control_name": "API Authentication & Authorization",
                "description":
                    "Ensure every API and integration endpoint uses "
                    "strong authentication and authorization mechanisms.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Secure Interface Communication",
                "description":
                    "Protect application-to-application communication "
                    "using approved encryption protocols and secure "
                    "communication channels.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Interface Configuration Management",
                "description":
                    "Maintain approved configuration standards for all "
                    "enterprise interfaces and integrations.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Third-Party Integration Governance",
                "description":
                    "Review and approve all third-party integrations "
                    "to ensure compliance with enterprise security "
                    "requirements.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Interface Security Monitoring",
                "description":
                    "Continuously monitor application interfaces for "
                    "security failures, unauthorized access attempts "
                    "and abnormal communication.",
                "control_type": "Detective"
            }

        ]

    )

    register_domain_controls(

        "DFA / DFD",

        "Sensitive Data Flow Protection",

        [

            {
                "control_name": "Sensitive Data Identification",
                "description":
                    "Identify and classify sensitive information "
                    "processed throughout enterprise application "
                    "data flows.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Sensitive Data Encryption",
                "description":
                    "Protect sensitive information during transmission "
                    "using approved cryptographic controls.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Sensitive Data Access Control",
                "description":
                    "Restrict access to sensitive information using "
                    "least privilege and role-based access control.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Sensitive Data Transmission Validation",
                "description":
                    "Ensure sensitive information is transferred only "
                    "through approved communication channels.",
                "control_type": "Detective"
            },

            {
                "control_name": "Sensitive Data Flow Monitoring",
                "description":
                    "Continuously monitor movement of sensitive "
                    "information to detect unauthorized disclosure "
                    "or abnormal transfer.",
                "control_type": "Detective"
            }

        ]

    )

    register_domain_controls(

        "DFA / DFD",

        "Trust Boundaries & Data Flow Security",

        [

            {
                "control_name": "Trust Boundary Identification",
                "description":
                    "Identify and document trust boundaries between "
                    "enterprise systems, external entities and "
                    "security zones.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Trust Boundary Protection",
                "description":
                    "Implement appropriate security controls for "
                    "protecting data crossing organizational trust "
                    "boundaries.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Network Segmentation Enforcement",
                "description":
                    "Enforce controlled communication between "
                    "security zones using network segmentation.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Boundary Traffic Monitoring",
                "description":
                    "Monitor communication across trust boundaries "
                    "to identify suspicious or unauthorized activity.",
                "control_type": "Detective"
            },

            {
                "control_name": "External Communication Validation",
                "description":
                    "Review and approve communication paths between "
                    "enterprise applications and external systems.",
                "control_type": "Preventive"
            }

        ]

    )

    # ======================================================================
    # DFRA
    # ======================================================================

    register_domain_controls(

        "DFRA",

        "Digital Evidence Management",

        [

            {
                "control_name": "Digital Evidence Collection",
                "description":
                    "Establish standardized procedures for secure "
                    "collection of digital evidence from enterprise "
                    "systems.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Evidence Preservation",
                "description":
                    "Protect collected digital evidence against "
                    "alteration, deletion and corruption throughout "
                    "its lifecycle.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Chain of Custody Management",
                "description":
                    "Maintain documented chain of custody for all "
                    "digital evidence collected during forensic "
                    "investigations.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Evidence Storage Security",
                "description":
                    "Store digital evidence in secure repositories "
                    "with appropriate access restrictions and "
                    "integrity protection.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Evidence Access Monitoring",
                "description":
                    "Monitor and audit access to digital evidence "
                    "to maintain accountability and integrity.",
                "control_type": "Detective"
            }

        ]

    )

    register_domain_controls(

        "DFRA",

        "Evidence Logging & Event Capture",

        [

            {
                "control_name": "Security Event Logging",
                "description":
                    "Capture security-relevant events across "
                    "applications, databases, operating systems "
                    "and infrastructure.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Comprehensive Audit Logging",
                "description":
                    "Enable comprehensive audit logging to support "
                    "forensic investigations and incident response.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Centralized Log Collection",
                "description":
                    "Collect and consolidate security logs into "
                    "approved centralized logging platforms.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Critical Event Monitoring",
                "description":
                    "Continuously monitor critical security events "
                    "requiring immediate investigation.",
                "control_type": "Detective"
            },

            {
                "control_name": "Log Integrity Protection",
                "description":
                    "Protect audit logs against unauthorized "
                    "modification or deletion.",
                "control_type": "Preventive"
            }

        ]

    )

    register_domain_controls(

        "DFRA",

        "Forensic Investigation Readiness",

        [

            {
                "control_name": "Forensic Readiness Framework",
                "description":
                    "Establish an enterprise forensic readiness "
                    "framework supporting effective security "
                    "investigations.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Incident Evidence Readiness",
                "description":
                    "Ensure systems are capable of preserving "
                    "sufficient evidence during security incidents.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Forensic Tool Readiness",
                "description":
                    "Maintain approved forensic tools and procedures "
                    "for evidence acquisition and analysis.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Forensic Investigation Procedures",
                "description":
                    "Document standardized procedures for forensic "
                    "investigation and evidence handling.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Forensic Readiness Assessment",
                "description":
                    "Periodically assess organizational readiness "
                    "for conducting digital forensic investigations.",
                "control_type": "Detective"
            }

        ]

    )

    register_domain_controls(

        "DFRA",

        "Log Retention & Preservation",

        [

            {
                "control_name": "Log Retention Policy",
                "description":
                    "Define and enforce enterprise log retention "
                    "requirements in accordance with regulatory, "
                    "business and forensic requirements.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Secure Log Archival",
                "description":
                    "Archive security logs securely to prevent "
                    "unauthorized modification, deletion or loss.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Log Preservation During Incidents",
                "description":
                    "Preserve all relevant security logs immediately "
                    "after detection of a security incident.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Archived Log Integrity Verification",
                "description":
                    "Periodically verify integrity of archived logs "
                    "to ensure evidentiary reliability.",
                "control_type": "Detective"
            },

            {
                "control_name": "Log Retention Compliance Review",
                "description":
                    "Review compliance with enterprise log retention "
                    "requirements and regulatory obligations.",
                "control_type": "Detective"
            }

        ]

    )

    register_domain_controls(

        "DFRA",

        "Time Synchronization & Log Integrity",

        [

            {
                "control_name": "Enterprise Time Synchronization",
                "description":
                    "Synchronize clocks across enterprise systems "
                    "using approved time synchronization sources.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Trusted Time Source Management",
                "description":
                    "Configure enterprise systems to obtain time "
                    "from trusted and approved NTP sources.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Timestamp Integrity",
                "description":
                    "Ensure security logs contain accurate and "
                    "tamper-resistant timestamps.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Time Synchronization Monitoring",
                "description":
                    "Continuously monitor time synchronization "
                    "status across enterprise infrastructure.",
                "control_type": "Detective"
            },

            {
                "control_name": "Log Integrity Validation",
                "description":
                    "Validate integrity of audit logs using "
                    "approved integrity verification mechanisms.",
                "control_type": "Detective"
            }

        ]

    )



    # ======================================================================
    # DATABASE REVIEW
    # ======================================================================

    register_domain_controls(

        "Database",

        "Database Auditing & Monitoring",

        [

            {
                "control_name": "Database Audit Logging",
                "description":
                    "Enable comprehensive database audit logging "
                    "covering privileged activities, configuration "
                    "changes and security events.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Database Activity Monitoring",
                "description":
                    "Continuously monitor database activities to "
                    "identify unauthorized or suspicious behavior.",
                "control_type": "Detective"
            },

            {
                "control_name": "Database Audit Log Protection",
                "description":
                    "Protect database audit logs against "
                    "unauthorized modification or deletion.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Database Audit Review",
                "description":
                    "Review database audit logs periodically to "
                    "identify security incidents and policy violations.",
                "control_type": "Detective"
            },

            {
                "control_name": "Database Monitoring Configuration",
                "description":
                    "Configure database monitoring mechanisms "
                    "according to enterprise security standards.",
                "control_type": "Preventive"
            }

        ]

    )



    register_domain_controls(

        "Database",

        "Database Backup, Recovery & Availability",

        [

            {
                "control_name": "Database Backup Management",
                "description":
                    "Perform scheduled database backups according "
                    "to approved backup policies.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Backup Integrity Verification",
                "description":
                    "Verify integrity and usability of database "
                    "backups before archival.",
                "control_type": "Detective"
            },

            {
                "control_name": "Backup Restoration Testing",
                "description":
                    "Periodically perform restoration testing to "
                    "validate recoverability of database backups.",
                "control_type": "Detective"
            },

            {
                "control_name": "Database Recovery Procedures",
                "description":
                    "Maintain documented procedures for database "
                    "recovery following system failures.",
                "control_type": "Preventive"
            },

            {
                "control_name": "High Availability Configuration",
                "description":
                    "Implement approved database availability "
                    "mechanisms to minimize service disruption.",
                "control_type": "Preventive"
            }

        ]

    )



    register_domain_controls(

        "Database",

        "Database Configuration & Hardening",

        [

            {
                "control_name": "Database Hardening Standards",
                "description":
                    "Implement approved database hardening "
                    "standards before production deployment.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Secure Database Configuration",
                "description":
                    "Maintain secure database configuration in "
                    "accordance with enterprise security baselines.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Database Patch Management",
                "description":
                    "Apply approved security patches and updates "
                    "to database platforms within defined timelines.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Database Configuration Review",
                "description":
                    "Review database configuration periodically "
                    "to identify insecure settings.",
                "control_type": "Detective"
            },

            {
                "control_name": "Database Vulnerability Management",
                "description":
                    "Identify, assess and remediate database "
                    "security vulnerabilities.",
                "control_type": "Corrective"
            }

        ]

    )



    register_domain_controls(

        "Database",

        "Database Encryption & Data Protection",

        [

            {
                "control_name": "Database Encryption Management",
                "description":
                    "Protect sensitive database information using "
                    "approved encryption mechanisms.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Encryption Key Management",
                "description":
                    "Manage cryptographic keys securely throughout "
                    "their lifecycle.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Sensitive Data Protection",
                "description":
                    "Protect confidential database information "
                    "against unauthorized disclosure.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Data Masking & Tokenization",
                "description":
                    "Implement masking or tokenization for "
                    "sensitive information where appropriate.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Encryption Compliance Review",
                "description":
                    "Review encryption implementation against "
                    "enterprise security standards.",
                "control_type": "Detective"
            }

        ]

    )



    register_domain_controls(

        "Database",

        "Database User & Access Management",

        [

            {
                "control_name": "Database User Provisioning",
                "description":
                    "Provision database accounts using approved "
                    "access management procedures.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Database Privileged Access Control",
                "description":
                    "Restrict privileged database access using "
                    "least privilege principles.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Database Access Review",
                "description":
                    "Perform periodic review of database users "
                    "and assigned privileges.",
                "control_type": "Detective"
            },

            {
                "control_name": "Database Authentication Security",
                "description":
                    "Enforce secure authentication mechanisms "
                    "for database access.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Inactive Account Management",
                "description":
                    "Identify and remove inactive database "
                    "accounts in a timely manner.",
                "control_type": "Corrective"
            }

        ]

    )



    # ======================================================================
    # ITGC
    # ======================================================================

    register_domain_controls(

        "ITGC",

        "Application Security Management",

        [

            {
                "control_name": "Application Security Governance",
                "description":
                    "Establish governance processes ensuring "
                    "applications comply with enterprise security "
                    "requirements.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Secure Application Configuration",
                "description":
                    "Configure enterprise applications according "
                    "to approved security baselines.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Application Security Assessment",
                "description":
                    "Conduct periodic application security "
                    "assessments to identify security weaknesses.",
                "control_type": "Detective"
            },

            {
                "control_name": "Application Security Monitoring",
                "description":
                    "Continuously monitor enterprise applications "
                    "for security events and abnormal activities.",
                "control_type": "Detective"
            },

            {
                "control_name": "Application Security Compliance",
                "description":
                    "Review applications for compliance with "
                    "enterprise security policies.",
                "control_type": "Detective"
            }

        ]

    )

    register_domain_controls(

        "ITGC",

        "Asset Management",

        [

            {
                "control_name": "Asset Inventory Management",
                "description":
                    "Maintain an accurate and up-to-date inventory of all "
                    "enterprise information assets including hardware, "
                    "software, virtual assets and cloud resources.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Asset Ownership & Accountability",
                "description":
                    "Assign accountable owners for every enterprise asset "
                    "throughout its lifecycle.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Asset Classification",
                "description":
                    "Classify enterprise assets according to business "
                    "criticality, confidentiality and operational impact.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Asset Lifecycle Management",
                "description":
                    "Manage acquisition, deployment, maintenance, transfer "
                    "and secure disposal of enterprise assets.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Asset Inventory Review",
                "description":
                    "Periodically review and reconcile asset inventories "
                    "to identify missing, obsolete or unauthorized assets.",
                "control_type": "Detective"
            },

            {
                "control_name": "Unauthorized Asset Detection",
                "description":
                    "Identify and investigate unauthorized or unmanaged "
                    "assets connected to the enterprise environment.",
                "control_type": "Detective"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Backup & Restoration",

        [

            {
                "control_name": "Enterprise Backup Management",
                "description":
                    "Perform scheduled backups of enterprise systems and "
                    "critical information according to approved policies.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Backup Protection",
                "description":
                    "Protect backup media and backup repositories against "
                    "unauthorized access, alteration and deletion.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Backup Restoration Testing",
                "description":
                    "Perform periodic restoration testing to validate "
                    "backup recoverability and integrity.",
                "control_type": "Detective"
            },

            {
                "control_name": "Backup Retention Management",
                "description":
                    "Retain enterprise backups according to regulatory "
                    "and organizational retention requirements.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Backup Job Monitoring",
                "description":
                    "Monitor backup jobs and investigate failed or "
                    "incomplete backup operations.",
                "control_type": "Detective"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Business Continuity & Disaster Recovery",

        [

            {
                "control_name": "Business Continuity Planning",
                "description":
                    "Develop and maintain enterprise business continuity "
                    "plans for critical business services.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Disaster Recovery Planning",
                "description":
                    "Maintain disaster recovery plans supporting timely "
                    "restoration of critical IT services.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Business Impact Analysis",
                "description":
                    "Perform business impact assessments to determine "
                    "critical systems and recovery priorities.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Disaster Recovery Testing",
                "description":
                    "Conduct periodic disaster recovery exercises to "
                    "validate recovery capability.",
                "control_type": "Detective"
            },

            {
                "control_name": "Recovery Objective Management",
                "description":
                    "Define, monitor and periodically review Recovery "
                    "Time Objectives (RTO) and Recovery Point Objectives (RPO).",
                "control_type": "Preventive"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Certificate Management",

        [

            {
                "control_name": "Digital Certificate Lifecycle Management",
                "description":
                    "Manage issuance, renewal, replacement and revocation "
                    "of enterprise digital certificates.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Certificate Expiry Monitoring",
                "description":
                    "Continuously monitor certificate validity and "
                    "renew certificates before expiration.",
                "control_type": "Detective"
            },

            {
                "control_name": "Trusted Certificate Authority Management",
                "description":
                    "Use approved and trusted Certificate Authorities "
                    "for enterprise certificate issuance.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Private Key Protection",
                "description":
                    "Protect certificate private keys against "
                    "unauthorized disclosure or misuse.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Certificate Configuration Review",
                "description":
                    "Review certificate configuration and deployment "
                    "to ensure compliance with enterprise standards.",
                "control_type": "Detective"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Change Management",

        [

            {
                "control_name": "Formal Change Management Process",
                "description":
                    "Implement a formal process governing request, "
                    "approval, testing, implementation and closure "
                    "of changes.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Change Approval Management",
                "description":
                    "Ensure all production changes receive documented "
                    "management approval before implementation.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Change Testing & Validation",
                "description":
                    "Perform appropriate functional and security testing "
                    "before promoting changes to production.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Emergency Change Management",
                "description":
                    "Govern emergency changes through documented approval, "
                    "implementation and post-implementation review.",
                "control_type": "Corrective"
            },

            {
                "control_name": "Post Implementation Review",
                "description":
                    "Review implemented changes to verify successful "
                    "deployment and absence of unintended impact.",
                "control_type": "Detective"
            }

        ]

    )

    register_domain_controls(

        "ITGC",

        "Cryptographic Key Management",

        [

            {
                "control_name": "Cryptographic Key Lifecycle Management",
                "description":
                    "Manage cryptographic keys throughout their lifecycle "
                    "including generation, distribution, storage, rotation, "
                    "archival and destruction.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Secure Key Storage",
                "description":
                    "Store cryptographic keys securely using approved "
                    "key storage mechanisms such as HSMs or encrypted "
                    "key vaults.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Key Rotation Management",
                "description":
                    "Rotate cryptographic keys periodically in accordance "
                    "with enterprise security policies.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Key Access Control",
                "description":
                    "Restrict access to cryptographic keys using "
                    "least-privilege and dual-control principles.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Key Usage Monitoring",
                "description":
                    "Monitor cryptographic key usage to detect "
                    "unauthorized access or abnormal activities.",
                "control_type": "Detective"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Endpoint Security Management",

        [

            {
                "control_name": "Endpoint Protection Management",
                "description":
                    "Deploy and maintain enterprise endpoint protection "
                    "solutions across all managed systems.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Endpoint Hardening",
                "description":
                    "Configure enterprise endpoints according to approved "
                    "security baselines and hardening standards.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Endpoint Patch Management",
                "description":
                    "Apply operating system and endpoint security patches "
                    "within approved timelines.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Endpoint Malware Protection",
                "description":
                    "Protect enterprise endpoints against malware, "
                    "ransomware and other malicious software.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Endpoint Compliance Monitoring",
                "description":
                    "Continuously monitor endpoint security compliance "
                    "and investigate policy violations.",
                "control_type": "Detective"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Firewall Security Management",

        [

            {
                "control_name": "Firewall Rule Management",
                "description":
                    "Implement controlled creation, modification and "
                    "removal of firewall security rules.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Firewall Configuration Management",
                "description":
                    "Maintain firewall configurations according to "
                    "enterprise security standards.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Firewall Rule Review",
                "description":
                    "Perform periodic reviews of firewall rules to "
                    "identify obsolete, excessive or risky rules.",
                "control_type": "Detective"
            },

            {
                "control_name": "Firewall Log Monitoring",
                "description":
                    "Continuously monitor firewall logs for suspicious "
                    "traffic and unauthorized connection attempts.",
                "control_type": "Detective"
            },

            {
                "control_name": "Perimeter Security Enforcement",
                "description":
                    "Enforce enterprise network perimeter protection "
                    "through appropriately configured firewalls.",
                "control_type": "Preventive"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Incident Management",

        [

            {
                "control_name": "Security Incident Response Framework",
                "description":
                    "Establish an enterprise security incident response "
                    "framework defining roles, responsibilities and "
                    "response procedures.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Incident Identification & Reporting",
                "description":
                    "Identify, classify and report security incidents "
                    "through approved reporting mechanisms.",
                "control_type": "Detective"
            },

            {
                "control_name": "Incident Investigation",
                "description":
                    "Conduct timely investigation of reported security "
                    "incidents to determine root cause and impact.",
                "control_type": "Corrective"
            },

            {
                "control_name": "Incident Resolution & Recovery",
                "description":
                    "Contain, eradicate and recover from security "
                    "incidents using approved response procedures.",
                "control_type": "Corrective"
            },

            {
                "control_name": "Lessons Learned Review",
                "description":
                    "Perform post-incident reviews to improve future "
                    "security controls and response capability.",
                "control_type": "Detective"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Logging & Monitoring",

        [

            {
                "control_name": "Enterprise Security Logging",
                "description":
                    "Enable comprehensive security logging across "
                    "applications, operating systems, databases and "
                    "network infrastructure.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Centralized Log Management",
                "description":
                    "Collect and manage enterprise security logs within "
                    "centralized logging or SIEM platforms.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Security Event Monitoring",
                "description":
                    "Continuously monitor enterprise security events "
                    "to identify suspicious or malicious activities.",
                "control_type": "Detective"
            },

            {
                "control_name": "Log Review & Analysis",
                "description":
                    "Perform periodic review and analysis of security "
                    "logs to identify policy violations and security "
                    "incidents.",
                "control_type": "Detective"
            },

            {
                "control_name": "Log Integrity Protection",
                "description":
                    "Protect enterprise logs against unauthorized "
                    "modification or deletion.",
                "control_type": "Preventive"
            }

        ]

    )

    register_domain_controls(

        "ITGC",

        "Network Security Architecture",

        [

            {
                "control_name": "Enterprise Network Security Management",
                "description":
                    "Implement and maintain enterprise network security "
                    "controls protecting internal and external network "
                    "communications.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Secure Network Configuration",
                "description":
                    "Configure network devices according to approved "
                    "enterprise security baselines.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Network Access Control",
                "description":
                    "Restrict access to enterprise network resources "
                    "using approved authentication and authorization "
                    "mechanisms.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Network Traffic Monitoring",
                "description":
                    "Continuously monitor enterprise network traffic "
                    "to detect malicious, abnormal or unauthorized "
                    "communications.",
                "control_type": "Detective"
            },

            {
                "control_name": "Network Security Compliance Review",
                "description":
                    "Review network security controls periodically "
                    "to ensure compliance with enterprise standards.",
                "control_type": "Detective"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Network Segmentation & Perimeter Security",

        [

            {
                "control_name": "Network Segmentation Strategy",
                "description":
                    "Implement network segmentation separating systems "
                    "based on business function, trust level and "
                    "security requirements.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Security Zone Management",
                "description":
                    "Define and maintain security zones controlling "
                    "communication between enterprise environments.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Inter-Segment Access Control",
                "description":
                    "Restrict communication between network segments "
                    "using least-privilege principles.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Segmentation Rule Review",
                "description":
                    "Review network segmentation rules periodically "
                    "to identify unnecessary or risky communication paths.",
                "control_type": "Detective"
            },

            {
                "control_name": "Network Isolation Verification",
                "description":
                    "Verify that critical systems remain appropriately "
                    "isolated from lower trust environments.",
                "control_type": "Detective"
            }

        ]

    )

    register_domain_controls(

        "ITGC",

        "Password Management",

        [

            {
                "control_name": "Password Policy Enforcement",
                "description":
                    "Enforce enterprise password policies covering "
                    "minimum length, complexity, history and expiry "
                    "requirements.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Password Lifecycle Management",
                "description":
                    "Manage password creation, reset, expiry and "
                    "retirement throughout the account lifecycle.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Secure Password Storage",
                "description":
                    "Store passwords securely using approved hashing "
                    "and cryptographic protection mechanisms.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Password Policy Review",
                "description":
                    "Review password policies periodically to ensure "
                    "continued compliance with enterprise security "
                    "requirements.",
                "control_type": "Detective"
            },

            {
                "control_name": "Default & Shared Password Management",
                "description":
                    "Identify, eliminate and monitor default or shared "
                    "password usage across enterprise systems.",
                "control_type": "Corrective"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Patch Management",

        [

            {
                "control_name": "Enterprise Patch Management",
                "description":
                    "Implement an enterprise patch management process "
                    "covering identification, testing, approval and "
                    "deployment of security patches.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Patch Risk Assessment",
                "description":
                    "Assess security risks associated with missing "
                    "patches and prioritize remediation.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Patch Deployment Management",
                "description":
                    "Deploy approved security patches according to "
                    "defined enterprise timelines.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Patch Compliance Monitoring",
                "description":
                    "Continuously monitor enterprise systems for "
                    "patch compliance and identify missing updates.",
                "control_type": "Detective"
            },

            {
                "control_name": "Patch Verification Testing",
                "description":
                    "Verify successful installation of security "
                    "patches following deployment.",
                "control_type": "Detective"
            }

        ]

    )



    

    register_domain_controls(

        "ITGC",

        "Privileged Access Management",

        [

            {
                "control_name": "Privileged Account Governance",
                "description":
                    "Establish governance for creation, approval, "
                    "usage and retirement of privileged accounts.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Privileged Access Provisioning",
                "description":
                    "Provision privileged accounts only after formal "
                    "business approval and authorization.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Privileged Session Monitoring",
                "description":
                    "Monitor privileged sessions to detect "
                    "unauthorized or suspicious administrative activities.",
                "control_type": "Detective"
            },

            {
                "control_name": "Privileged Credential Protection",
                "description":
                    "Protect privileged credentials using approved "
                    "vaulting and credential management mechanisms.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Privileged Access Review",
                "description":
                    "Perform periodic review of privileged accounts "
                    "and assigned permissions.",
                "control_type": "Detective"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Secure Configuration Management",

        [

            {
                "control_name": "Enterprise Configuration Baseline",
                "description":
                    "Maintain approved secure configuration baselines "
                    "for enterprise systems and applications.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Configuration Change Control",
                "description":
                    "Manage security configuration changes through "
                    "formal approval and change management procedures.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Configuration Compliance Assessment",
                "description":
                    "Assess enterprise systems against approved "
                    "configuration baselines.",
                "control_type": "Detective"
            },

            {
                "control_name": "Configuration Drift Monitoring",
                "description":
                    "Monitor systems for unauthorized configuration "
                    "changes or baseline deviations.",
                "control_type": "Detective"
            },

            {
                "control_name": "Configuration Documentation",
                "description":
                    "Maintain complete documentation of approved "
                    "security configurations.",
                "control_type": "Preventive"
            }

        ]

    )

    register_domain_controls(

        "ITGC",

        "Third-Party / Vendor Management",

        [

            {
                "control_name": "Third-Party Risk Assessment",
                "description":
                    "Assess security risks before onboarding vendors "
                    "and external service providers.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Vendor Security Due Diligence",
                "description":
                    "Perform security due diligence to verify vendor "
                    "compliance with enterprise requirements.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Third-Party Security Monitoring",
                "description":
                    "Continuously monitor vendor security posture "
                    "throughout the engagement lifecycle.",
                "control_type": "Detective"
            },

            {
                "control_name": "Vendor Access Governance",
                "description":
                    "Control and periodically review third-party "
                    "access to enterprise resources.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Vendor Contract Compliance",
                "description":
                    "Ensure contractual security obligations are "
                    "implemented and periodically verified.",
                "control_type": "Detective"
            }

        ]
    )



    



    register_domain_controls(

        "ITGC",

        "User Management",

        [

            {
                "control_name": "User Provisioning Management",
                "description":
                    "Provision user accounts only after appropriate "
                    "authorization and business approval.",
                "control_type": "Preventive"
            },

            {
                "control_name": "User Access Review",
                "description":
                    "Conduct periodic reviews of user accounts and "
                    "assigned permissions.",
                "control_type": "Detective"
            },

            {
                "control_name": "Least Privilege Enforcement",
                "description":
                    "Grant users only the minimum level of access "
                    "required to perform assigned responsibilities.",
                "control_type": "Preventive"
            },

            {
                "control_name": "User Account Lifecycle Management",
                "description":
                    "Manage creation, modification, suspension and "
                    "termination of enterprise user accounts.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Inactive Account Management",
                "description":
                    "Identify, disable and remove inactive or "
                    "obsolete user accounts.",
                "control_type": "Corrective"
            }

        ]

    )



    register_domain_controls(

        "ITGC",

        "Vulnerability Management",

        [

            {
                "control_name": "Enterprise Vulnerability Assessment",
                "description":
                    "Conduct periodic vulnerability assessments across "
                    "enterprise applications, infrastructure and databases.",
                "control_type": "Detective"
            },

            {
                "control_name": "Vulnerability Risk Prioritization",
                "description":
                    "Prioritize identified vulnerabilities based on "
                    "risk, exploitability and business impact.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Vulnerability Remediation",
                "description":
                    "Remediate identified vulnerabilities within "
                    "approved enterprise timelines.",
                "control_type": "Corrective"
            },

            {
                "control_name": "Remediation Verification",
                "description":
                    "Verify that identified vulnerabilities have "
                    "been successfully remediated.",
                "control_type": "Detective"
            },

            {
                "control_name": "Continuous Vulnerability Monitoring",
                "description":
                    "Continuously monitor enterprise assets for newly "
                    "discovered vulnerabilities.",
                "control_type": "Detective"
            }

        ]

    )

    



    



    

    # ======================================================================
    # SNA
    # ======================================================================

    register_domain_controls(

        "SNA",

        "Architecture Governance & Change Management",

        [

            {
                "control_name": "Network Architecture Governance",
                "description":
                    "Establish governance for planning, approval, "
                    "maintenance and lifecycle management of network "
                    "architecture.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Architecture Change Management",
                "description":
                    "Ensure all network architecture changes follow "
                    "approved change management procedures.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Architecture Documentation Review",
                "description":
                    "Review architecture documentation periodically "
                    "to ensure continued accuracy.",
                "control_type": "Detective"
            },

            {
                "control_name": "Architecture Compliance Monitoring",
                "description":
                    "Monitor implementation against approved network "
                    "architecture standards.",
                "control_type": "Detective"
            }

        ]

    )

    register_domain_controls(

        "SNA",

        "Infrastructure Resilience & High Availability",

        [

            {
                "control_name": "High Availability Architecture",
                "description":
                    "Design enterprise infrastructure to provide high "
                    "availability for critical business services through "
                    "redundancy and fault tolerance.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Infrastructure Resilience Management",
                "description":
                    "Implement resilient infrastructure capable of "
                    "withstanding hardware, software and network failures.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Redundancy & Failover Configuration",
                "description":
                    "Configure redundancy and automated failover for "
                    "critical infrastructure components.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Infrastructure Availability Monitoring",
                "description":
                    "Continuously monitor infrastructure health and "
                    "availability to detect service degradation.",
                "control_type": "Detective"
            },

            {
                "control_name": "Resilience Testing",
                "description":
                    "Perform periodic resilience and failover testing "
                    "to validate infrastructure recovery capability.",
                "control_type": "Detective"
            }

        ]

    )



    register_domain_controls(

        "SNA",

        "Network Architecture & Documentation",

        [

            {
                "control_name": "Network Documentation Management",
                "description":
                    "Maintain complete, accurate and approved network "
                    "architecture documentation for enterprise environments.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Network Diagram Management",
                "description":
                    "Maintain up-to-date logical and physical network "
                    "diagrams representing production infrastructure.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Architecture Documentation Review",
                "description":
                    "Review network documentation periodically to ensure "
                    "accuracy and completeness.",
                "control_type": "Detective"
            },

            {
                "control_name": "Network Asset Documentation",
                "description":
                    "Document enterprise network devices, communication "
                    "paths and security zones.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Architecture Version Control",
                "description":
                    "Maintain version history and approval records for "
                    "network architecture documentation.",
                "control_type": "Preventive"
            }

        ]

    )



    register_domain_controls(

        "SNA",

        "Network Segmentation & Perimeter Security",

        [

            {
                "control_name": "Enterprise Network Segmentation",
                "description":
                    "Implement network segmentation separating enterprise "
                    "systems according to business criticality and trust levels.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Perimeter Firewall Protection",
                "description":
                    "Protect enterprise network boundaries using approved "
                    "firewall and perimeter security controls.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Security Zone Isolation",
                "description":
                    "Isolate enterprise security zones to minimize lateral "
                    "movement and unauthorized communication.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Perimeter Security Monitoring",
                "description":
                    "Continuously monitor perimeter security events and "
                    "network boundary traffic.",
                "control_type": "Detective"
            },

            {
                "control_name": "Segmentation Rule Review",
                "description":
                    "Review segmentation and perimeter rules periodically "
                    "to identify unnecessary exposure.",
                "control_type": "Detective"
            }

        ]

    )



    register_domain_controls(

        "SNA",

        "Secure Connectivity & Communication",

        [

            {
                "control_name": "Secure Communication Protocols",
                "description":
                    "Use approved secure communication protocols for all "
                    "enterprise network communications.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Encrypted Network Communication",
                "description":
                    "Protect enterprise network communication using "
                    "approved encryption mechanisms.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Remote Connectivity Security",
                "description":
                    "Secure remote connectivity using approved "
                    "authentication, authorization and encryption controls.",
                "control_type": "Preventive"
            },

            {
                "control_name": "Communication Channel Monitoring",
                "description":
                    "Monitor enterprise communication channels for "
                    "unauthorized access and abnormal activities.",
                "control_type": "Detective"
            },

            {
                "control_name": "Secure Connectivity Compliance",
                "description":
                    "Review secure connectivity implementation against "
                    "enterprise security standards.",
                "control_type": "Detective"
            }

        ]

    )


# =============================================================================
# Register All Controls
# =============================================================================

register_all_domain_controls()

print()
print("=" * 80)
print("Registering Enterprise Controls...")
print("=" * 80)

for controls in DOMAIN_CONTROLS.values():

    for control in controls:

        control_name = control["control_name"]

        if control_name in CONTROL_LOOKUP:
            continue

        control_id = generate_control_id()

        CONTROL_LOOKUP[control_name] = control_id

        CONTROL_RECORDS.append({

            "Control ID": control_id,

            "Control Name": control_name,

            "Description": control["description"],

            "Control Type": control["control_type"]

        })

print(f"Registered {len(CONTROL_RECORDS)} unique controls.")

# =============================================================================
# Build Control Library DataFrame
# =============================================================================

print()
print("=" * 80)
print("Creating Control Library...")
print("=" * 80)

control_library_df = pd.DataFrame(CONTROL_RECORDS)

print(f"Total Controls : {len(control_library_df)}")

# =============================================================================
# Build Observation → Primary Control Mapping
# =============================================================================

print()
print("=" * 80)
print("Building Observation-Control Mapping...")
print("=" * 80)


def select_primary_control(observation, controls):
    """
    Select the most appropriate control for an observation.

    Current Strategy
    ----------------
    Keyword-based matching.

    If no keyword matches,
    the first control of the domain is selected.

    Future versions can replace this logic with
    semantic similarity or ML models without
    changing the dataset structure.
    """

    observation = str(observation).lower()

    keyword_map = {

        "password": "Password Policy Enforcement",

        "backup": "Enterprise Backup Management",

        "restore": "Backup Restoration Testing",

        "asset": "Asset Inventory Management",

        "certificate": "Certificate Expiry Monitoring",

        "firewall": "Firewall Rule Management",

        "incident": "Security Incident Response Framework",

        "log": "Enterprise Security Logging",

        "audit": "Database Audit Logging",

        "database": "Database Audit Logging",

        "patch": "Enterprise Patch Management",

        "vulnerability": "Enterprise Vulnerability Assessment",

        "privileged": "Privileged Account Governance",

        "account": "User Provisioning Management",

        "vendor": "Third-Party Risk Assessment",

        "third party": "Third-Party Risk Assessment",

        "network architecture": "Network Architecture Governance",

        "network diagram": "Network Documentation Management",

        "encryption": "Database Encryption Management",

        "key": "Cryptographic Key Lifecycle Management",

        "endpoint": "Endpoint Protection Management",

        "dfd": "DFD Governance Framework",

        "data flow": "Complete Data Flow Documentation",

        "evidence": "Digital Evidence Collection",

        "forensic": "Forensic Readiness Framework"

    }

    for keyword, control_name in keyword_map.items():

        if keyword in observation:

            for control in controls:

                if control["control_name"] == control_name:

                    return control

    if controls:
        return controls[0]
    return None

for index, row in observation_df.iterrows():

    activity = str(row["Activity"]).strip()

    domain = str(row["Domain"]).strip()

    observation = row["Observation"]

    controls = DOMAIN_CONTROLS.get((activity, domain), [])
    

    selected_control = select_primary_control(

        observation,

        controls

    )
    if selected_control is None:
        continue

    control_name = selected_control["control_name"]

    control_id = CONTROL_LOOKUP[control_name]

    OBSERVATION_CONTROL_MAPPING.append({

        "Observation ID": f"OBS-{index + 1:04d}",

        "Activity": activity,

        "Domain": domain,

        "Observation": observation,

        "Control ID": control_id,

        "Control Name": control_name, 

        "Control Type": selected_control["control_type"]

    })

print(
    f"Generated {len(OBSERVATION_CONTROL_MAPPING)} mappings."
)

# =============================================================================
# Export Datasets
# =============================================================================

observation_control_mapping_df = pd.DataFrame(
    OBSERVATION_CONTROL_MAPPING
)

control_library_df.to_excel(
    CONTROL_LIBRARY_PATH,
    index=False
)

observation_control_mapping_df.to_excel(
    OBSERVATION_CONTROL_MAPPING_PATH,
    index=False
)

print("\nControl Library exported successfully.")
print("Observation-Control Mapping exported successfully.")

print()
print("=" * 80)
print("BUILD SUMMARY")
print("=" * 80)
print(f"Observations Processed : {len(observation_df)}")
print(f"Unique Controls        : {len(control_library_df)}")
print(f"Mappings Generated     : {len(observation_control_mapping_df)}")
print("=" * 80)

