import os
from collections import OrderedDict

import pandas as pd

# =============================================================================
# Repository Paths
# =============================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_DIR = os.path.join(BASE_DIR, "dataset")

OBSERVATION_LIBRARY_PATH = os.path.join(
    DATASET_DIR,
    "observation_library.xlsx"
)

COMPLIANCE_LIBRARY_PATH = os.path.join(
    DATASET_DIR,
    "compliance_library.xlsx"
)

OBSERVATION_COMPLIANCE_MAPPING_PATH = os.path.join(
    DATASET_DIR,
    "observation_compliance_mapping.xlsx"
)

# =============================================================================
# Load Observation Repository
# =============================================================================

print("=" * 80)
print("Loading Observation Repository...")
print("=" * 80)

observation_df = pd.read_excel(
    OBSERVATION_LIBRARY_PATH
)

observation_df.columns = observation_df.columns.str.strip()

print(f"Loaded {len(observation_df)} observations.")

# =============================================================================
# Runtime Containers
# =============================================================================

DOMAIN_COMPLIANCES = OrderedDict()

COMPLIANCE_LOOKUP = {}

COMPLIANCE_RECORDS = []

OBSERVATION_COMPLIANCE_MAPPING = []

compliance_counter = 1

# =============================================================================
# Compliance ID Generator
# =============================================================================

def generate_compliance_id():
    """
    Generates sequential Compliance IDs.

    Example

    CMP-0001
    CMP-0002
    """

    global compliance_counter

    compliance_id = f"CMP-{compliance_counter:04d}"

    compliance_counter += 1

    return compliance_id

# =============================================================================
# Register Domain Compliances
# =============================================================================

def register_domain_compliances(
    activity,
    domain,
    compliances
):
    """
    Registers all compliance requirements
    belonging to a security domain.
    """

    DOMAIN_COMPLIANCES[(activity, domain)] = compliances


# =============================================================================
# Compliance Frameworks
# =============================================================================

FRAMEWORKS = {

    "ISO": "ISO/IEC 27001:2022",

    "NIST": "NIST Cybersecurity Framework 2.0",

    "RBI": "RBI Cyber Security Framework",

    "CIS": "CIS Critical Security Controls v8"

}

# =============================================================================
# Register All Enterprise Compliances
# =============================================================================

def register_all_domain_compliances():
    """
    Registers enterprise compliance requirements.

    IMPORTANT

    Registration order MUST follow
    observation_library.xlsx exactly.

    Duplicate compliance entries are
    automatically removed later while
    generating the master Compliance Library.
    """

    # ==============================================================
    # DFA / DFD
    # ==============================================================

    # ==============================================================
    # DFA / DFD
    # ==============================================================

    register_domain_compliances(

        "DFA / DFD",

        "DFD Governance & Change Management",

        [

            {
                "compliance_name":
                    "Information Security Governance",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Clause 5 / Annex A.5",

                "description":
                    "Governance, ownership, accountability and management "
                    "oversight of information security."
            },

            {
                "compliance_name":
                    "Security Architecture Governance",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "GV.OV / GV.PO",

                "description":
                    "Governance processes supporting secure enterprise "
                    "architecture."
            },

            {
                "compliance_name":
                    "Enterprise Architecture Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "IT Governance",

                "description":
                    "Governance over enterprise architecture, approvals, "
                    "reviews and accountability."
            },

            {
                "compliance_name":
                    "Governance & Risk Management",

                "framework":
                    FRAMEWORKS["CIS"],

                "clause":
                    "Control 17",

                "description":
                    "Governance supporting security management."
            }

        ]

    )



    register_domain_compliances(

        "DFA / DFD",

        "Data Flow Documentation & Completeness",

        [

            {
                "compliance_name":
                    "Information Asset Documentation",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5",

                "description":
                    "Documentation and maintenance of information assets."
            },

            {
                "compliance_name":
                    "Information Flow Documentation",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "ID.AM",

                "description":
                    "Identification and documentation of information flows."
            },

            {
                "compliance_name":
                    "Application Documentation Standards",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Application Security",

                "description":
                    "Documentation supporting secure application operations."
            }

        ]

    )



    register_domain_compliances(

        "DFA / DFD",

        "Interface & Integration Security",

        [

            {
                "compliance_name":
                    "Secure Interface Management",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Protection of interfaces and data exchanges."
            },

            {
                "compliance_name":
                    "System Communication Protection",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.DS",

                "description":
                    "Protection of communications and interfaces."
            },

            {
                "compliance_name":
                    "Application Integration Security",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Application Security",

                "description":
                    "Security of enterprise interfaces and integrations."
            }

        ]

    )



    register_domain_compliances(

        "DFA / DFD",

        "Sensitive Data Flow Protection",

        [

            {
                "compliance_name":
                    "Sensitive Information Protection",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Protection of confidential information."
            },

            {
                "compliance_name":
                    "Data Security Controls",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.DS",

                "description":
                    "Protection of data throughout its lifecycle."
            },

            {
                "compliance_name":
                    "Sensitive Data Protection",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Data Security",

                "description":
                    "Protection of sensitive enterprise information."
            }

        ]

    )



    register_domain_compliances(

        "DFA / DFD",

        "Trust Boundaries & Data Flow Security",

        [

            {
                "compliance_name":
                    "Network Trust Boundary Protection",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Protection of trust boundaries and network zones."
            },

            {
                "compliance_name":
                    "Network Security Architecture",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.PT",

                "description":
                    "Secure architecture protecting information flows."
            },

            {
                "compliance_name":
                    "Perimeter Security Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Network Security",

                "description":
                    "Governance of network trust boundaries."
            }

        ]

    )

    # ==============================================================
    # DFRA
    # ==============================================================

    register_domain_compliances(

        "DFRA",

        "Digital Evidence Management",

        [

            {
                "compliance_name":
                    "Digital Evidence Governance",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5 / A.8",

                "description":
                    "Management, preservation and governance of digital evidence."
            },

            {
                "compliance_name":
                    "Forensic Evidence Handling",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "RS.AN",

                "description":
                    "Procedures for secure collection and preservation of digital evidence."
            },

            {
                "compliance_name":
                    "Digital Evidence Preservation",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Cyber Incident Response",

                "description":
                    "Preservation of evidence supporting investigations."
            }

        ]

    )



    register_domain_compliances(

        "DFRA",

        "Evidence Logging & Event Capture",

        [

            {
                "compliance_name":
                    "Security Event Logging",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Collection and monitoring of security event logs."
            },

            {
                "compliance_name":
                    "Continuous Security Monitoring",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "DE.CM",

                "description":
                    "Continuous monitoring of security events."
            },

            {
                "compliance_name":
                    "Enterprise Log Management",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Logging & Monitoring",

                "description":
                    "Collection and monitoring of enterprise security logs."
            }

        ]

    )



    register_domain_compliances(

        "DFRA",

        "Forensic Investigation Readiness",

        [

            {
                "compliance_name":
                    "Incident Investigation Readiness",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5",

                "description":
                    "Preparedness for security investigations."
            },

            {
                "compliance_name":
                    "Forensic Investigation Capability",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "RS.AN",

                "description":
                    "Capability to perform digital forensic investigations."
            },

            {
                "compliance_name":
                    "Cyber Investigation Readiness",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Incident Response",

                "description":
                    "Readiness to investigate cyber incidents."
            }

        ]

    )



    register_domain_compliances(

        "DFRA",

        "Log Retention & Preservation",

        [

            {
                "compliance_name":
                    "Log Retention Requirements",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Retention and preservation of audit logs."
            },

            {
                "compliance_name":
                    "Security Log Preservation",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.PS",

                "description":
                    "Protection and retention of security logs."
            },

            {
                "compliance_name":
                    "Audit Log Retention",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Logging & Monitoring",

                "description":
                    "Retention of audit trails and security logs."
            }

        ]

    )



    register_domain_compliances(

        "DFRA",

        "Time Synchronization & Log Integrity",

        [

            {
                "compliance_name":
                    "Time Synchronization Controls",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Synchronization of enterprise systems supporting audit accuracy."
            },

            {
                "compliance_name":
                    "Audit Log Integrity",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.PS",

                "description":
                    "Integrity and reliability of audit logs."
            },

            {
                "compliance_name":
                    "Enterprise Time Synchronization",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Infrastructure Security",

                "description":
                    "Accurate system time supporting audit investigations."
            }

        ]

    )

    # ==============================================================
    # Database
    # ==============================================================

    register_domain_compliances(

        "Database",

        "Database Auditing & Monitoring",

        [

            {
                "compliance_name":
                    "Database Audit Logging",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Logging and monitoring of database activities and administrative actions."
            },

            {
                "compliance_name":
                    "Database Security Monitoring",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "DE.CM",

                "description":
                    "Continuous monitoring of database security events."
            },

            {
                "compliance_name":
                    "Database Audit Compliance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Database Security",

                "description":
                    "Audit logging and monitoring of enterprise databases."
            }

        ]

    )



    register_domain_compliances(

        "Database",

        "Database Backup, Recovery & Availability",

        [

            {
                "compliance_name":
                    "Backup & Recovery Management",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Backup, restoration and recovery controls protecting enterprise information."
            },

            {
                "compliance_name":
                    "System Recovery Capability",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "RC.RP",

                "description":
                    "Recovery planning supporting business continuity."
            },

            {
                "compliance_name":
                    "Database Availability Controls",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Business Continuity",

                "description":
                    "Controls supporting recovery and availability of databases."
            }

        ]

    )



    register_domain_compliances(

        "Database",

        "Database Configuration & Hardening",

        [

            {
                "compliance_name":
                    "Secure Database Configuration",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Secure configuration and hardening of database platforms."
            },

            {
                "compliance_name":
                    "Configuration Baseline Management",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.PS",

                "description":
                    "Secure baseline configuration management."
            },

            {
                "compliance_name":
                    "Database Hardening Standards",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Database Security",

                "description":
                    "Secure configuration and hardening of enterprise databases."
            }

        ]

    )



    register_domain_compliances(

        "Database",

        "Database Encryption & Data Protection",

        [

            {
                "compliance_name":
                    "Database Encryption Controls",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Protection of database information using encryption."
            },

            {
                "compliance_name":
                    "Data Protection Controls",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.DS",

                "description":
                    "Protection of information confidentiality and integrity."
            },

            {
                "compliance_name":
                    "Sensitive Database Protection",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Data Security",

                "description":
                    "Protection of sensitive information stored in databases."
            }

        ]

    )



    register_domain_compliances(

        "Database",

        "Database User & Access Management",

        [

            {
                "compliance_name":
                    "Database Access Control",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5",

                "description":
                    "Management of database users, roles and privileges."
            },

            {
                "compliance_name":
                    "Identity & Privileged Access",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.AA",

                "description":
                    "Identity management and privileged access control."
            },

            {
                "compliance_name":
                    "Database User Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Access Control",

                "description":
                    "Governance over database user lifecycle and privileged access."
            }

        ]

    )

    # ==============================================================
    # ITGC
    # ==============================================================

    register_domain_compliances(

        "ITGC",

        "Application Security Management",

        [

            {
                "compliance_name": "Application Security Governance",

                "framework": FRAMEWORKS["ISO"],

                "clause": "Annex A.8",

                "description":
                    "Governance ensuring secure development, deployment and maintenance of applications."
            },

            {
                "compliance_name": "Secure Software Protection",

                "framework": FRAMEWORKS["NIST"],

                "clause": "PR.DS",

                "description":
                    "Protection of applications through secure development and security controls."
            },

            {
                "compliance_name": "Application Security Compliance",

                "framework": FRAMEWORKS["RBI"],

                "clause": "Application Security",

                "description":
                    "Compliance requirements governing enterprise application security."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Asset Management",

        [

            {
                "compliance_name": "Information Asset Management",

                "framework": FRAMEWORKS["ISO"],

                "clause": "Annex A.5",

                "description":
                    "Identification, ownership and lifecycle management of information assets."
            },

            {
                "compliance_name": "Asset Inventory Management",

                "framework": FRAMEWORKS["NIST"],

                "clause": "ID.AM",

                "description":
                    "Inventory and management of enterprise assets."
            },

            {
                "compliance_name": "IT Asset Governance",

                "framework": FRAMEWORKS["RBI"],

                "clause": "IT Asset Management",

                "description":
                    "Governance over enterprise technology assets."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Backup & Restoration",

        [

            {
                "compliance_name": "Enterprise Backup Controls",

                "framework": FRAMEWORKS["ISO"],

                "clause": "Annex A.8",

                "description":
                    "Protection of information through backup and restoration."
            },

            {
                "compliance_name": "Recovery Capability",

                "framework": FRAMEWORKS["NIST"],

                "clause": "RC.RP",

                "description":
                    "Recovery capability supporting resilience and continuity."
            },

            {
                "compliance_name": "Backup Governance",

                "framework": FRAMEWORKS["RBI"],

                "clause": "Business Continuity",

                "description":
                    "Governance of enterprise backup and restoration."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Business Continuity & Disaster Recovery",

        [

            {
                "compliance_name": "Business Continuity Management",

                "framework": FRAMEWORKS["ISO"],

                "clause": "Annex A.5",

                "description":
                    "Business continuity planning protecting enterprise services."
            },

            {
                "compliance_name": "Disaster Recovery Planning",

                "framework": FRAMEWORKS["NIST"],

                "clause": "RC.RP",

                "description":
                    "Planning and testing recovery from disruptive events."
            },

            {
                "compliance_name": "Operational Resilience",

                "framework": FRAMEWORKS["RBI"],

                "clause": "Business Continuity",

                "description":
                    "Operational resilience and disaster recovery preparedness."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Certificate Management",

        [

            {
                "compliance_name": "Digital Certificate Management",

                "framework": FRAMEWORKS["ISO"],

                "clause": "Annex A.8",

                "description":
                    "Lifecycle management of digital certificates and trust services."
            },

            {
                "compliance_name": "Cryptographic Trust Services",

                "framework": FRAMEWORKS["NIST"],

                "clause": "PR.DS",

                "description":
                    "Protection of communications using trusted certificates."
            },

            {
                "compliance_name": "PKI Governance",

                "framework": FRAMEWORKS["RBI"],

                "clause": "Cryptography",

                "description":
                    "Governance over enterprise certificate lifecycle."
            }

        ]

    )

    register_domain_compliances(

        "ITGC",

        "Change Management",

        [

            {
                "compliance_name":
                    "Enterprise Change Management",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Formal authorization, testing, implementation and review of changes."
            },

            {
                "compliance_name":
                    "Controlled Change Process",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.PS",

                "description":
                    "Controlled management of technology and configuration changes."
            },

            {
                "compliance_name":
                    "IT Change Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Change Management",

                "description":
                    "Governance over enterprise technology changes."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Cryptographic Key Management",

        [

            {
                "compliance_name":
                    "Cryptographic Key Management",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Lifecycle management of cryptographic keys."
            },

            {
                "compliance_name":
                    "Cryptographic Protection",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.DS",

                "description":
                    "Protection of information using cryptographic controls."
            },

            {
                "compliance_name":
                    "Enterprise Cryptography Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Cryptography",

                "description":
                    "Governance over cryptographic key lifecycle."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Endpoint Security Management",

        [

            {
                "compliance_name":
                    "Endpoint Protection",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Protection of enterprise endpoints against malware and cyber threats."
            },

            {
                "compliance_name":
                    "Endpoint Security Controls",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.PT",

                "description":
                    "Protection and monitoring of enterprise endpoint devices."
            },

            {
                "compliance_name":
                    "Endpoint Security Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Endpoint Security",

                "description":
                    "Governance of endpoint security controls."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Firewall Security Management",

        [

            {
                "compliance_name":
                    "Network Firewall Controls",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Management of enterprise firewall configurations and rule governance."
            },

            {
                "compliance_name":
                    "Network Boundary Protection",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.PT",

                "description":
                    "Protection of enterprise network boundaries."
            },

            {
                "compliance_name":
                    "Firewall Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Network Security",

                "description":
                    "Governance of enterprise firewall security."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Incident Management",

        [

            {
                "compliance_name":
                    "Security Incident Management",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5",

                "description":
                    "Identification, reporting, investigation and resolution of security incidents."
            },

            {
                "compliance_name":
                    "Incident Response Capability",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "RS",

                "description":
                    "Capability to respond to, analyze and recover from cybersecurity incidents."
            },

            {
                "compliance_name":
                    "Cyber Incident Response",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Incident Response",

                "description":
                    "Governance and response processes for cyber security incidents."
            }

        ]

    )

    register_domain_compliances(

        "ITGC",

        "Logging & Monitoring",

        [

            {
                "compliance_name":
                    "Security Logging & Monitoring",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Collection, monitoring and protection of audit logs and security events."
            },

            {
                "compliance_name":
                    "Continuous Security Monitoring",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "DE.CM",

                "description":
                    "Continuous monitoring of enterprise security events."
            },

            {
                "compliance_name":
                    "Enterprise Log Management",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Logging & Monitoring",

                "description":
                    "Governance over security logging, monitoring and alerting."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Network Security Architecture",

        [

            {
                "compliance_name":
                    "Secure Network Architecture",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Design and governance of secure enterprise network architecture."
            },

            {
                "compliance_name":
                    "Network Infrastructure Protection",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.PT",

                "description":
                    "Protection of enterprise network infrastructure."
            },

            {
                "compliance_name":
                    "Network Architecture Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Network Security",

                "description":
                    "Governance of secure network architecture."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Network Segmentation & Perimeter Security",

        [

            {
                "compliance_name":
                    "Network Segmentation Controls",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Segmentation of enterprise networks and protection of trust boundaries."
            },

            {
                "compliance_name":
                    "Boundary Defense",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.PT",

                "description":
                    "Protection of network boundaries and security zones."
            },

            {
                "compliance_name":
                    "Perimeter Security Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Network Security",

                "description":
                    "Governance of perimeter security controls."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Password Management",

        [

            {
                "compliance_name":
                    "Password & Authentication Controls",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5",

                "description":
                    "Management of passwords, authentication and credential security."
            },

            {
                "compliance_name":
                    "Identity Authentication",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.AA",

                "description":
                    "Authentication and identity verification for enterprise users."
            },

            {
                "compliance_name":
                    "Authentication Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Access Control",

                "description":
                    "Governance over password and authentication mechanisms."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Patch Management",

        [

            {
                "compliance_name":
                    "Security Patch Management",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Timely deployment of security patches and updates."
            },

            {
                "compliance_name":
                    "System Maintenance",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.MA",

                "description":
                    "Maintenance and updating of enterprise systems."
            },

            {
                "compliance_name":
                    "Patch Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Patch Management",

                "description":
                    "Governance of security patch deployment and remediation."
            }

        ]

    )

    register_domain_compliances(

        "ITGC",

        "Privileged Access Management",

        [

            {
                "compliance_name":
                    "Privileged Access Governance",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5",

                "description":
                    "Governance over privileged accounts, administrative access and periodic access reviews."
            },

            {
                "compliance_name":
                    "Privileged Identity Management",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.AA",

                "description":
                    "Management and monitoring of privileged identities and administrative access."
            },

            {
                "compliance_name":
                    "Privileged Account Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Access Control",

                "description":
                    "Governance of privileged accounts and administrative activities."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Secure Configuration Management",

        [

            {
                "compliance_name":
                    "Secure Configuration Baselines",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Implementation and maintenance of secure configuration baselines."
            },

            {
                "compliance_name":
                    "Configuration Integrity",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.PS",

                "description":
                    "Protection of systems through secure configuration management."
            },

            {
                "compliance_name":
                    "Configuration Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Configuration Management",

                "description":
                    "Governance of secure enterprise configurations."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Third-Party / Vendor Management",

        [

            {
                "compliance_name":
                    "Third-Party Security Governance",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5",

                "description":
                    "Governance of third-party relationships and supplier security."
            },

            {
                "compliance_name":
                    "Supply Chain Risk Management",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "GV.SC",

                "description":
                    "Management of cybersecurity risks associated with suppliers and third parties."
            },

            {
                "compliance_name":
                    "Vendor Risk Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Third-Party Risk Management",

                "description":
                    "Governance of vendor security and outsourced service providers."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "User Management",

        [

            {
                "compliance_name":
                    "Identity & User Lifecycle Management",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5",

                "description":
                    "Management of user provisioning, modification, review and de-provisioning."
            },

            {
                "compliance_name":
                    "Identity Management",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.AA",

                "description":
                    "Management of digital identities and user access throughout their lifecycle."
            },

            {
                "compliance_name":
                    "User Access Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Identity & Access Management",

                "description":
                    "Governance of user identities and access permissions."
            }

        ]

    )



    register_domain_compliances(

        "ITGC",

        "Vulnerability Management",

        [

            {
                "compliance_name":
                    "Vulnerability Management Program",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Identification, assessment and remediation of security vulnerabilities."
            },

            {
                "compliance_name":
                    "Vulnerability Identification & Remediation",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "ID.RA",

                "description":
                    "Identification, assessment and remediation of cybersecurity vulnerabilities."
            },

            {
                "compliance_name":
                    "Enterprise Vulnerability Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Vulnerability Management",

                "description":
                    "Governance over vulnerability assessment and remediation activities."
            }

        ]

    )

    # ==============================================================
    # SNA
    # ==============================================================

    register_domain_compliances(

        "SNA",

        "Architecture Governance & Change Management",

        [

            {
                "compliance_name":
                    "Network Architecture Governance",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5",

                "description":
                    "Governance over enterprise network architecture, "
                    "design reviews, approvals and lifecycle management."
            },

            {
                "compliance_name":
                    "Architecture Governance",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "GV.OV",

                "description":
                    "Governance supporting secure enterprise architecture."
            },

            {
                "compliance_name":
                    "Enterprise Architecture Compliance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "IT Governance",

                "description":
                    "Governance over enterprise network architecture."
            }

        ]

    )



    register_domain_compliances(

        "SNA",

        "Infrastructure Resilience & High Availability",

        [

            {
                "compliance_name":
                    "Infrastructure Resilience",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5",

                "description":
                    "Availability and resilience of critical infrastructure."
            },

            {
                "compliance_name":
                    "High Availability Controls",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "RC.RP",

                "description":
                    "Infrastructure resilience and recovery capability."
            },

            {
                "compliance_name":
                    "Operational Resilience Governance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Business Continuity",

                "description":
                    "Governance of highly available enterprise infrastructure."
            }

        ]

    )



    register_domain_compliances(

        "SNA",

        "Network Architecture & Documentation",

        [

            {
                "compliance_name":
                    "Network Documentation Management",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.5",

                "description":
                    "Documentation and maintenance of enterprise network architecture."
            },

            {
                "compliance_name":
                    "Network Asset Documentation",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "ID.AM",

                "description":
                    "Documentation of enterprise network assets and topology."
            },

            {
                "compliance_name":
                    "Network Documentation Compliance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Network Security",

                "description":
                    "Governance over enterprise network documentation."
            }

        ]

    )



    register_domain_compliances(

        "SNA",

        "Network Segmentation & Perimeter Security",

        [

            {
                "compliance_name":
                    "Enterprise Network Segmentation",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Implementation of secure network segmentation and boundary protection."
            },

            {
                "compliance_name":
                    "Boundary Defense",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.PT",

                "description":
                    "Protection of enterprise network boundaries and trust zones."
            },

            {
                "compliance_name":
                    "Perimeter Security Compliance",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Network Security",

                "description":
                    "Governance over enterprise perimeter security."
            }

        ]

    )



    register_domain_compliances(

        "SNA",

        "Secure Connectivity & Communication",

        [

            {
                "compliance_name":
                    "Secure Communication Controls",

                "framework":
                    FRAMEWORKS["ISO"],

                "clause":
                    "Annex A.8",

                "description":
                    "Protection of enterprise communications using secure protocols."
            },

            {
                "compliance_name":
                    "Protected Communications",

                "framework":
                    FRAMEWORKS["NIST"],

                "clause":
                    "PR.DS",

                "description":
                    "Protection of data in transit and secure communication channels."
            },

            {
                "compliance_name":
                    "Secure Network Communication",

                "framework":
                    FRAMEWORKS["RBI"],

                "clause":
                    "Network Security",

                "description":
                    "Governance over secure enterprise communications."
            }

        ]

    )

# =============================================================================
# Register All Compliances
# =============================================================================

register_all_domain_compliances()

print()
print("=" * 80)
print("Registering Enterprise Compliances...")
print("=" * 80)

for compliances in DOMAIN_COMPLIANCES.values():

    for compliance in compliances:

        lookup_key = (

            compliance["compliance_name"],

            compliance["framework"]

        )

        if lookup_key in COMPLIANCE_LOOKUP:

            continue

        compliance_id = generate_compliance_id()

        COMPLIANCE_LOOKUP[lookup_key] = compliance_id

        COMPLIANCE_RECORDS.append({

            "Compliance ID": compliance_id,

            "Compliance Name":
                compliance["compliance_name"],

            "Framework":
                compliance["framework"],

            "Clause":
                compliance["clause"],

            "Description":
                compliance["description"]

        })

print(

    f"Registered {len(COMPLIANCE_RECORDS)} unique compliances."

)

# =============================================================================
# Build Compliance Library
# =============================================================================

print()

print("=" * 80)

print("Creating Compliance Library...")

print("=" * 80)

compliance_library_df = pd.DataFrame(

    COMPLIANCE_RECORDS

)

print(

    f"Total Compliances : {len(compliance_library_df)}"

)

# =============================================================================
# Build Observation → Primary Compliance Mapping
# =============================================================================

print()
print("=" * 80)
print("Building Observation-Compliance Mapping...")
print("=" * 80)


def select_primary_compliance(observation, compliances):
    """
    Select the most appropriate compliance requirement.

    Current Strategy
    ----------------
    Keyword-based matching.

    Future versions can replace this logic with
    semantic similarity or AI models without
    changing the dataset structure.
    """

    observation = str(observation).lower()

    keyword_map = {

        # ==========================================================
        # Password / Identity
        # ==========================================================

        "password": "Password & Authentication Controls",

        "authentication": "Identity Authentication",

        "user": "Identity & User Lifecycle Management",

        "access": "Identity & User Lifecycle Management",

        "privileged": "Privileged Access Governance",

        "pam": "Privileged Identity Management",

        # ==========================================================
        # Asset
        # ==========================================================

        "asset": "Information Asset Management",

        "inventory": "Asset Inventory Management",

        # ==========================================================
        # Backup
        # ==========================================================

        "backup": "Enterprise Backup Controls",

        "restore": "Enterprise Backup Controls",

        "recovery": "Business Continuity Management",

        # ==========================================================
        # Logging
        # ==========================================================

        "log": "Security Logging & Monitoring",

        "logging": "Security Logging & Monitoring",

        "monitor": "Continuous Security Monitoring",

        "siem": "Enterprise Log Management",

        # ==========================================================
        # Firewall
        # ==========================================================

        "firewall": "Network Firewall Controls",

        # ==========================================================
        # Network
        # ==========================================================

        "network": "Secure Network Architecture",

        "segmentation": "Network Segmentation Controls",

        "perimeter": "Perimeter Security Governance",

        "vpn": "Secure Communication Controls",

        # ==========================================================
        # Patch / Vulnerability
        # ==========================================================

        "patch": "Security Patch Management",

        "vulnerability": "Vulnerability Management Program",

        "remediation": "Vulnerability Management Program",

        # ==========================================================
        # Database
        # ==========================================================

        "database": "Database Audit Logging",

        "encryption": "Database Encryption Controls",

        # ==========================================================
        # DFD
        # ==========================================================

        "dfd": "Information Security Governance",

        "data flow": "Information Flow Documentation",

        "interface": "Secure Interface Management",

        # ==========================================================
        # DFRA
        # ==========================================================

        "evidence": "Digital Evidence Governance",

        "forensic": "Forensic Investigation Capability",

        "chain": "Digital Evidence Governance",

        "ntp": "Time Synchronization Controls",

        # ==========================================================
        # Certificate / Keys
        # ==========================================================

        "certificate": "Digital Certificate Management",

        "key": "Cryptographic Key Management",

        # ==========================================================
        # Endpoint
        # ==========================================================

        "endpoint": "Endpoint Protection",

        # ==========================================================
        # Incident
        # ==========================================================

        "incident": "Security Incident Management",

        # ==========================================================
        # Vendor
        # ==========================================================

        "vendor": "Third-Party Security Governance",

        "third party": "Third-Party Security Governance"

    }

    for keyword, compliance_name in keyword_map.items():

        if keyword in observation:

            for compliance in compliances:

                if compliance["compliance_name"] == compliance_name:

                    return compliance

    return compliances[0]


for index, row in observation_df.iterrows():

    activity = str(row["Activity"]).strip()

    domain = str(row["Domain"]).strip()

    observation = row["Observation"]

    compliances = DOMAIN_COMPLIANCES.get(

        (activity, domain),

        []

    )

    if not compliances:

        continue

    selected_compliance = select_primary_compliance(

        observation,

        compliances

    )

    lookup_key = (

        selected_compliance["compliance_name"],

        selected_compliance["framework"]

    )

    compliance_id = COMPLIANCE_LOOKUP[lookup_key]

    OBSERVATION_COMPLIANCE_MAPPING.append({

        "Observation ID": f"OBS-{index + 1:04d}",

        "Activity": activity,

        "Domain": domain,

        "Observation": observation,

        "Compliance ID": compliance_id,

        "Compliance Name": selected_compliance["compliance_name"],

        "Framework": selected_compliance["framework"],

        "Clause": selected_compliance["clause"]

    })

print(

    f"Generated {len(OBSERVATION_COMPLIANCE_MAPPING)} mappings."

)

# =============================================================================
# Export Compliance Library
# =============================================================================

observation_compliance_mapping_df = pd.DataFrame(

    OBSERVATION_COMPLIANCE_MAPPING

)

compliance_library_df.to_excel(

    COMPLIANCE_LIBRARY_PATH,

    index=False

)

observation_compliance_mapping_df.to_excel(

    OBSERVATION_COMPLIANCE_MAPPING_PATH,

    index=False

)

print()

print("Compliance Library exported successfully.")

print("Observation-Compliance Mapping exported successfully.")

print()

print("=" * 80)

print("BUILD SUMMARY")

print("=" * 80)

print(f"Observations Processed : {len(observation_df)}")

print(f"Unique Compliances     : {len(compliance_library_df)}")

print(f"Mappings Generated     : {len(observation_compliance_mapping_df)}")

print("=" * 80)