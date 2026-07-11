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

EVIDENCE_LIBRARY_PATH = os.path.join(
    DATASET_DIR,
    "evidence_library.xlsx"
)

OBSERVATION_EVIDENCE_MAPPING_PATH = os.path.join(
    DATASET_DIR,
    "observation_evidence_mapping.xlsx"
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

# Remove accidental leading/trailing spaces from column names
observation_df.columns = observation_df.columns.str.strip()

print(f"Loaded {len(observation_df)} observations.")


# =============================================================================
# Runtime Containers
# =============================================================================

DOMAIN_EVIDENCES = OrderedDict()

EVIDENCE_LOOKUP = {}

EVIDENCE_RECORDS = []

OBSERVATION_EVIDENCE_MAPPING = []

evidence_counter = 1

# =============================================================================
# Evidence ID Generator
# =============================================================================

def generate_evidence_id():
    """
    Generates sequential Evidence IDs.

    Example

    EVD-0001
    EVD-0002
    """

    global evidence_counter

    evidence_id = f"EVD-{evidence_counter:04d}"

    evidence_counter += 1

    return evidence_id

# =============================================================================
# Register Domain Evidences
# =============================================================================

def register_domain_evidences(
    activity,
    domain,
    evidences
):
    """
    Registers all enterprise evidences
    belonging to a security domain.
    """

    DOMAIN_EVIDENCES[(activity, domain)] = evidences

# =============================================================================
# Register All Enterprise Evidences
# =============================================================================

def register_all_domain_evidences():
    """
    Registers enterprise evidences.

    IMPORTANT

    Registration order MUST follow
    observation_library.xlsx exactly.

    Duplicate evidence names are
    automatically removed later while
    generating the master Evidence Library.
    """

    # ======================================================================
    # DFA / DFD
    # ======================================================================

    register_domain_evidences(

        "DFA / DFD",

        "DFD Governance & Change Management",

        [

            {
                "evidence_name": "Approved DFD Governance Policy",

                "description":
                    "Approved policy defining governance, ownership, "
                    "maintenance and lifecycle management of enterprise "
                    "Data Flow Diagrams (DFDs).",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "DFD Ownership Matrix",

                "description":
                    "Document assigning business owners, application "
                    "owners and technical custodians for enterprise DFDs.",

                "evidence_type": "Document",

                "collection_method": "Ownership Register"
            },

            {
                "evidence_name": "Architecture Review Board Approval Records",

                "description":
                    "Approval records demonstrating Architecture Review "
                    "Board review and approval of newly created or modified DFDs.",

                "evidence_type": "Approval",

                "collection_method": "Approval Records"
            },

            {
                "evidence_name": "DFD Version History Register",

                "description":
                    "Version-controlled history showing all revisions, "
                    "updates and approvals of enterprise DFDs.",

                "evidence_type": "Register",

                "collection_method": "Repository Export"
            },

            {
                "evidence_name": "DFD Periodic Review Register",

                "description":
                    "Evidence demonstrating periodic review, validation "
                    "and recertification of enterprise DFDs.",

                "evidence_type": "Register",

                "collection_method": "Review Register"
            },

            {
                "evidence_name": "DFD Change Management Records",

                "description":
                    "Approved change requests, implementation records "
                    "and supporting documentation associated with DFD updates.",

                "evidence_type": "Record",

                "collection_method": "Change Management Records"
            },

            {
                "evidence_name": "Enterprise DFD Repository",

                "description":
                    "Central repository containing approved enterprise "
                    "Data Flow Diagrams with version control.",

                "evidence_type": "Repository",

                "collection_method": "Repository Export"
            },

            {
                "evidence_name": "DFD Governance Dashboard",

                "description":
                    "Management dashboard showing DFD governance KPIs, "
                    "review status, ownership status and compliance metrics.",

                "evidence_type": "Dashboard",

                "collection_method": "Dashboard Export"
            }

        ]

    )
     
    register_domain_evidences(

        "DFA / DFD",

        "Data Flow Documentation & Completeness",

        [

            {
                "evidence_name": "Enterprise Data Flow Diagrams",

                "description":
                    "Approved enterprise Data Flow Diagrams covering all "
                    "applications, interfaces and business processes.",

                "evidence_type": "Diagram",

                "collection_method": "Architecture Repository"
            },

            {
                "evidence_name": "Application Interface Inventory",

                "description":
                    "Inventory of application interfaces and associated "
                    "data exchange mechanisms.",

                "evidence_type": "Inventory",

                "collection_method": "Inventory Export"
            },

            {
                "evidence_name": "Application Data Dictionary",

                "description":
                    "Document describing data elements, classifications "
                    "and data ownership.",

                "evidence_type": "Document",

                "collection_method": "Documentation Repository"
            },

            {
                "evidence_name": "DFD Completeness Review Report",

                "description":
                    "Review report validating completeness and accuracy "
                    "of enterprise DFDs.",

                "evidence_type": "Report",

                "collection_method": "Review Report"
            },

            {
                "evidence_name": "Business Process Flow Documents",

                "description":
                    "Business process documentation supporting "
                    "enterprise data flows.",

                "evidence_type": "Document",

                "collection_method": "Documentation Repository"
            }

        ]

    )
    
    register_domain_evidences(

        "DFA / DFD",

        "Interface & Integration Security",

        [

            {
                "evidence_name": "API Security Configuration",

                "description":
                    "Configuration demonstrating API authentication, "
                    "authorization and security controls.",

                "evidence_type": "Configuration",

                "collection_method": "API Configuration Export"
            },

            {
                "evidence_name": "Interface Configuration Export",

                "description":
                    "Configuration of enterprise interfaces including "
                    "security parameters.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "TLS/SSL Configuration Report",

                "description":
                    "Configuration showing encryption settings for "
                    "secure communications.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Interface Access Control Matrix",

                "description":
                    "Access control matrix governing interface access.",

                "evidence_type": "Matrix",

                "collection_method": "Access Control Register"
            },

            {
                "evidence_name": "Interface Security Test Report",

                "description":
                    "Security assessment results for enterprise "
                    "interfaces and integrations.",

                "evidence_type": "Report",

                "collection_method": "Assessment Report"
            }

        ]

    )

    register_domain_evidences(

        "DFA / DFD",

        "Sensitive Data Flow Protection",

        [

            {
                "evidence_name": "Enterprise Data Classification Policy",

                "description":
                    "Policy defining classification and handling of "
                    "enterprise information assets.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Sensitive Data Inventory",

                "description":
                    "Inventory of sensitive and regulated data assets.",

                "evidence_type": "Inventory",

                "collection_method": "Inventory Export"
            },

            {
                "evidence_name": "Encryption Configuration Report",

                "description":
                    "Configuration demonstrating encryption of "
                    "sensitive information.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Data Masking Configuration",

                "description":
                    "Configuration implementing masking or tokenization "
                    "of sensitive information.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Data Leakage Prevention Report",

                "description":
                    "Evidence demonstrating implementation of DLP "
                    "controls for enterprise information.",

                "evidence_type": "Report",

                "collection_method": "DLP Dashboard"
            }

        ]

    )

    register_domain_evidences(

        "DFA / DFD",

        "Trust Boundaries & Data Flow Security",

        [

            {
                "evidence_name": "Network Trust Boundary Diagram",

                "description":
                    "Architecture diagram illustrating enterprise "
                    "trust boundaries.",

                "evidence_type": "Diagram",

                "collection_method": "Architecture Repository"
            },

            {
                "evidence_name": "Network Segmentation Configuration",

                "description":
                    "Configuration demonstrating logical network "
                    "segmentation controls.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Firewall Rule Review Report",

                "description":
                    "Approved firewall rule review and recertification "
                    "records.",

                "evidence_type": "Report",

                "collection_method": "Firewall Export"
            },

            {
                "evidence_name": "Trust Boundary Risk Assessment",

                "description":
                    "Assessment evaluating risks across enterprise "
                    "trust boundaries.",

                "evidence_type": "Assessment",

                "collection_method": "Risk Assessment Report"
            },

            {
                "evidence_name": "Network Architecture Diagram",

                "description":
                    "Enterprise network architecture illustrating "
                    "security zones and communication paths.",

                "evidence_type": "Diagram",

                "collection_method": "Architecture Repository"
            }

        ]

    )

    register_domain_evidences(

        "DFRA",

        "Digital Evidence Management",

        [

            {
                "evidence_name": "Digital Evidence Management Policy",

                "description":
                    "Approved policy governing identification, collection, "
                    "handling, preservation and disposal of digital evidence.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Chain of Custody Register",

                "description":
                    "Chain of custody records documenting evidence collection, "
                    "custodian transfers and preservation activities.",

                "evidence_type": "Register",

                "collection_method": "Evidence Register"
            },

            {
                "evidence_name": "Digital Evidence Inventory",

                "description":
                    "Central inventory of collected forensic evidence, "
                    "custodians, locations and preservation status.",

                "evidence_type": "Inventory",

                "collection_method": "Inventory Export"
            },

            {
                "evidence_name": "Evidence Collection Procedures",

                "description":
                    "Standard operating procedures governing digital "
                    "evidence acquisition and handling.",

                "evidence_type": "SOP",

                "collection_method": "Procedure Document"
            },

            {
                "evidence_name": "Evidence Repository Access Report",

                "description":
                    "Access control records for digital evidence repositories.",

                "evidence_type": "Report",

                "collection_method": "Access Control Export"
            },

            {
                "evidence_name": "Hash Verification Report",

                "description":
                    "Evidence integrity verification using cryptographic hashes.",

                "evidence_type": "Report",

                "collection_method": "Hash Verification Tool"
            }

        ]

    )

    register_domain_evidences(

        "DFRA",

        "Evidence Logging & Event Capture",

        [

            {
                "evidence_name": "SIEM Event Log Export",

                "description":
                    "Export of security events collected by the enterprise SIEM.",

                "evidence_type": "Log",

                "collection_method": "SIEM Export"
            },

            {
                "evidence_name": "Windows Event Log Export",

                "description":
                    "Windows security event logs collected from production systems.",

                "evidence_type": "Log",

                "collection_method": "Event Viewer Export"
            },

            {
                "evidence_name": "Linux Audit Log Export",

                "description":
                    "Linux audit logs demonstrating security event capture.",

                "evidence_type": "Log",

                "collection_method": "Audit Log Export"
            },

            {
                "evidence_name": "Logging Configuration Report",

                "description":
                    "Configuration showing enterprise logging settings "
                    "for critical applications and infrastructure.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Security Event Monitoring Dashboard",

                "description":
                    "Dashboard showing monitored security events "
                    "and alert generation.",

                "evidence_type": "Dashboard",

                "collection_method": "SIEM Dashboard"
            }

        ]

    )

    register_domain_evidences(

        "DFRA",

        "Forensic Investigation Readiness",

        [

            {
                "evidence_name": "Forensic Investigation SOP",

                "description":
                    "Standard operating procedures governing forensic investigations.",

                "evidence_type": "SOP",

                "collection_method": "Procedure Document"
            },

            {
                "evidence_name": "Incident Investigation Reports",

                "description":
                    "Completed forensic investigation reports for security incidents.",

                "evidence_type": "Report",

                "collection_method": "Investigation Repository"
            },

            {
                "evidence_name": "Forensic Tool Validation Records",

                "description":
                    "Validation records for approved forensic acquisition tools.",

                "evidence_type": "Record",

                "collection_method": "Validation Report"
            },

            {
                "evidence_name": "Forensic Team Training Records",

                "description":
                    "Training records demonstrating investigator competency.",

                "evidence_type": "Record",

                "collection_method": "Training Register"
            },

            {
                "evidence_name": "Forensic Readiness Assessment Report",

                "description":
                    "Assessment of organizational forensic preparedness.",

                "evidence_type": "Assessment",

                "collection_method": "Assessment Report"
            }

        ]

    )


    register_domain_evidences(

        "DFRA",

        "Log Retention & Preservation",

        [

            {
                "evidence_name": "Log Retention Policy",

                "description":
                    "Approved enterprise log retention policy.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Log Retention Configuration",

                "description":
                    "Configuration demonstrating enterprise log retention periods.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Archived Security Logs",

                "description":
                    "Archived enterprise security logs maintained "
                    "according to retention requirements.",

                "evidence_type": "Log",

                "collection_method": "Archive Export"
            },

            {
                "evidence_name": "Log Preservation Procedure",

                "description":
                    "Procedure for preservation of logs during investigations.",

                "evidence_type": "Procedure",

                "collection_method": "Procedure Document"
            },

            {
                "evidence_name": "Log Archive Verification Report",

                "description":
                    "Verification report confirming integrity and "
                    "availability of archived logs.",

                "evidence_type": "Report",

                "collection_method": "Verification Report"
            }

        ]

    )

    register_domain_evidences(

        "DFRA",

        "Time Synchronization & Log Integrity",

        [

            {
                "evidence_name": "NTP Configuration Export",

                "description":
                    "Configuration demonstrating enterprise time synchronization.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Time Synchronization Monitoring Report",

                "description":
                    "Monitoring report validating synchronization "
                    "of enterprise systems.",

                "evidence_type": "Report",

                "collection_method": "Monitoring Dashboard"
            },

            {
                "evidence_name": "Log Integrity Verification Report",

                "description":
                    "Verification demonstrating integrity of "
                    "enterprise security logs.",

                "evidence_type": "Report",

                "collection_method": "Integrity Verification Tool"
            },

            {
                "evidence_name": "Time Synchronization Policy",

                "description":
                    "Policy governing enterprise time synchronization.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Secure Time Source Configuration",

                "description":
                    "Configuration of approved enterprise time sources.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            }

        ]

    )

    register_domain_evidences(

        "Database",

        "Database Auditing & Monitoring",

        [

            {
                "evidence_name": "Database Audit Log Export",

                "description":
                    "Database audit logs capturing administrative "
                    "activities, user access and security events.",

                "evidence_type": "Log",

                "collection_method": "Database Audit Log Export"
            },

            {
                "evidence_name": "Database Monitoring Dashboard",

                "description":
                    "Dashboard showing database health, alerts "
                    "and security monitoring status.",

                "evidence_type": "Dashboard",

                "collection_method": "Monitoring Dashboard"
            },

            {
                "evidence_name": "Database Audit Configuration",

                "description":
                    "Configuration demonstrating enabled database "
                    "auditing parameters.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Privileged Database Activity Report",

                "description":
                    "Report containing privileged database user activities.",

                "evidence_type": "Report",

                "collection_method": "Audit Report"
            },

            {
                "evidence_name": "Database Security Alert Report",

                "description":
                    "Security alerts generated for suspicious "
                    "database activities.",

                "evidence_type": "Report",

                "collection_method": "Monitoring Dashboard"
            }

        ]

    )


    register_domain_evidences(

        "Database",

        "Database Backup, Recovery & Availability",

        [

            {
                "evidence_name": "Database Backup Policy",

                "description":
                    "Approved policy governing database backup "
                    "and recovery operations.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Database Backup Reports",

                "description":
                    "Backup execution reports demonstrating "
                    "successful backup completion.",

                "evidence_type": "Report",

                "collection_method": "Backup Console Export"
            },

            {
                "evidence_name": "Database Restore Test Reports",

                "description":
                    "Evidence demonstrating periodic database "
                    "restoration testing.",

                "evidence_type": "Report",

                "collection_method": "Restore Test Report"
            },

            {
                "evidence_name": "Recovery Procedure Document",

                "description":
                    "Document describing database recovery procedures.",

                "evidence_type": "Procedure",

                "collection_method": "Procedure Document"
            },

            {
                "evidence_name": "Backup Schedule Configuration",

                "description":
                    "Configuration of enterprise backup schedules.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            }

        ]

    )

    register_domain_evidences(

        "Database",

        "Database Configuration & Hardening",

        [

            {
                "evidence_name": "Database Security Configuration",

                "description":
                    "Current database security configuration parameters.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Database Hardening Checklist",

                "description":
                    "Checklist validating implementation of database "
                    "hardening controls.",

                "evidence_type": "Checklist",

                "collection_method": "Hardening Assessment"
            },

            {
                "evidence_name": "Database Patch Status Report",

                "description":
                    "Current database patch and version status.",

                "evidence_type": "Report",

                "collection_method": "Patch Management Report"
            },

            {
                "evidence_name": "Database Parameter Configuration",

                "description":
                    "Export of database initialization parameters.",

                "evidence_type": "Configuration",

                "collection_method": "Parameter Export"
            },

            {
                "evidence_name": "Database Vulnerability Assessment Report",

                "description":
                    "Assessment report identifying database security weaknesses.",

                "evidence_type": "Assessment",

                "collection_method": "VA Report"
            }

        ]

    )

    register_domain_evidences(

        "Database",

        "Database Encryption & Data Protection",

        [

            {
                "evidence_name": "Database Encryption Configuration",

                "description":
                    "Configuration demonstrating encryption of "
                    "database files and sensitive information.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Encryption Key Management Records",

                "description":
                    "Evidence demonstrating lifecycle management "
                    "of database encryption keys.",

                "evidence_type": "Record",

                "collection_method": "Key Management Console"
            },

            {
                "evidence_name": "Transparent Data Encryption Report",

                "description":
                    "Report showing implementation status of "
                    "transparent data encryption.",

                "evidence_type": "Report",

                "collection_method": "Database Console Export"
            },

            {
                "evidence_name": "Data Classification Register",

                "description":
                    "Register identifying sensitive information "
                    "stored within databases.",

                "evidence_type": "Register",

                "collection_method": "Classification Repository"
            },

            {
                "evidence_name": "Database Encryption Policy",

                "description":
                    "Approved policy governing encryption of "
                    "enterprise database information.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            }

        ]

    )

    register_domain_evidences(

        "Database",

        "Database User & Access Management",

        [

            {
                "evidence_name": "Database User Access Register",

                "description":
                    "Register containing all authorized database users "
                    "and assigned privileges.",

                "evidence_type": "Register",

                "collection_method": "User Export"
            },

            {
                "evidence_name": "Database Privileged User Report",

                "description":
                    "Report of privileged database accounts and "
                    "assigned administrative roles.",

                "evidence_type": "Report",

                "collection_method": "Privilege Export"
            },

            {
                "evidence_name": "Database Access Review Records",

                "description":
                    "Evidence of periodic review and recertification "
                    "of database access rights.",

                "evidence_type": "Record",

                "collection_method": "Access Review Register"
            },

            {
                "evidence_name": "Database Account Provisioning Records",

                "description":
                    "Records demonstrating approval and provisioning "
                    "of database user accounts.",

                "evidence_type": "Record",

                "collection_method": "Identity Management System"
            },

            {
                "evidence_name": "Database Authentication Configuration",

                "description":
                    "Configuration governing authentication mechanisms "
                    "for database users.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            }

        ]

    )

    register_domain_evidences(

        "ITGC",

        "Application Security Management",

        [

            {
                "evidence_name": "Application Security Policy",

                "description":
                    "Approved policy governing enterprise application security controls.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Application Security Configuration",

                "description":
                    "Security configuration of enterprise applications.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Secure SDLC Documentation",

                "description":
                    "Documentation demonstrating secure software development practices.",

                "evidence_type": "Document",

                "collection_method": "SDLC Repository"
            },

            {
                "evidence_name": "Application Security Assessment Report",

                "description":
                    "Security assessment report identifying application vulnerabilities.",

                "evidence_type": "Assessment",

                "collection_method": "Assessment Report"
            },

            {
                "evidence_name": "Application Security Dashboard",

                "description":
                    "Dashboard showing application security posture and metrics.",

                "evidence_type": "Dashboard",

                "collection_method": "Dashboard Export"
            }

        ]

    )

    register_domain_evidences(

        "ITGC",

        "Asset Management",

        [

            {
                "evidence_name": "Enterprise Asset Inventory",

                "description":
                    "Inventory of enterprise IT assets with ownership and classification.",

                "evidence_type": "Inventory",

                "collection_method": "Asset Management Export"
            },

            {
                "evidence_name": "Asset Management Policy",

                "description":
                    "Approved policy governing enterprise asset lifecycle management.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Asset Ownership Register",

                "description":
                    "Register assigning business and technical owners for assets.",

                "evidence_type": "Register",

                "collection_method": "Ownership Register"
            },

            {
                "evidence_name": "Asset Discovery Report",

                "description":
                    "Report demonstrating periodic discovery of enterprise assets.",

                "evidence_type": "Report",

                "collection_method": "Discovery Tool Export"
            },

            {
                "evidence_name": "Asset Lifecycle Records",

                "description":
                    "Records covering asset onboarding, maintenance and disposal.",

                "evidence_type": "Record",

                "collection_method": "Asset Management System"
            }

        ]

    )

    register_domain_evidences(

        "ITGC",

        "Backup & Restoration",

        [

            {
                "evidence_name": "Enterprise Backup Policy",

                "description":
                    "Approved enterprise backup and restoration policy.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Backup Job Reports",

                "description":
                    "Reports showing successful execution of scheduled backups.",

                "evidence_type": "Report",

                "collection_method": "Backup Console Export"
            },

            {
                "evidence_name": "Backup Restoration Test Report",

                "description":
                    "Evidence demonstrating successful restoration testing.",

                "evidence_type": "Report",

                "collection_method": "Restore Test Report"
            },

            {
                "evidence_name": "Backup Configuration Export",

                "description":
                    "Configuration of enterprise backup schedules and retention.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Backup Monitoring Dashboard",

                "description":
                    "Dashboard showing enterprise backup status.",

                "evidence_type": "Dashboard",

                "collection_method": "Dashboard Export"
            }

        ]

    )

    register_domain_evidences(

        "ITGC",

        "Business Continuity & Disaster Recovery",

        [

            {
                "evidence_name": "Business Continuity Policy",

                "description":
                    "Approved policy governing business continuity planning.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Disaster Recovery Plan",

                "description":
                    "Approved disaster recovery procedures for enterprise applications.",

                "evidence_type": "Plan",

                "collection_method": "Document Repository"
            },

            {
                "evidence_name": "BCP/DR Drill Report",

                "description":
                    "Evidence demonstrating periodic disaster recovery exercises.",

                "evidence_type": "Report",

                "collection_method": "Exercise Report"
            },

            {
                "evidence_name": "Recovery Time Objective Report",

                "description":
                    "Evidence validating RTO and RPO objectives.",

                "evidence_type": "Report",

                "collection_method": "Assessment Report"
            },

            {
                "evidence_name": "Business Impact Analysis",

                "description":
                    "Business impact assessment supporting continuity planning.",

                "evidence_type": "Assessment",

                "collection_method": "BIA Document"
            }

        ]

    )

    register_domain_evidences(

        "ITGC",

        "Certificate Management",

        [

            {
                "evidence_name": "Certificate Inventory",

                "description":
                    "Inventory of enterprise digital certificates.",

                "evidence_type": "Inventory",

                "collection_method": "Certificate Management Export"
            },

            {
                "evidence_name": "Certificate Expiry Report",

                "description":
                    "Report showing certificate validity and expiry status.",

                "evidence_type": "Report",

                "collection_method": "Certificate Dashboard"
            },

            {
                "evidence_name": "PKI Configuration",

                "description":
                    "Configuration of enterprise public key infrastructure.",

                "evidence_type": "Configuration",

                "collection_method": "PKI Export"
            },

            {
                "evidence_name": "Certificate Management Policy",

                "description":
                    "Policy governing lifecycle management of certificates.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            }

        ]

    )

    register_domain_evidences(

        "ITGC",

        "Change Management",

        [

            {
                "evidence_name": "Change Management Policy",

                "description":
                    "Approved policy governing enterprise IT change management.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Approved Change Tickets",

                "description":
                    "Approved change requests with implementation and rollback details.",

                "evidence_type": "Record",

                "collection_method": "ITSM Export"
            },

            {
                "evidence_name": "CAB Approval Records",

                "description":
                    "Change Advisory Board approval records for production changes.",

                "evidence_type": "Approval",

                "collection_method": "CAB Minutes"
            },

            {
                "evidence_name": "Emergency Change Register",

                "description":
                    "Register of emergency changes and post-implementation approvals.",

                "evidence_type": "Register",

                "collection_method": "ITSM Export"
            },

            {
                "evidence_name": "Post Implementation Review Reports",

                "description":
                    "Evidence demonstrating successful review of completed changes.",

                "evidence_type": "Report",

                "collection_method": "PIR Report"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "Cryptographic Key Management",

        [

            {
                "evidence_name": "Cryptographic Key Management Policy",

                "description":
                    "Approved policy governing encryption key lifecycle management.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Encryption Key Inventory",

                "description":
                    "Inventory of enterprise cryptographic keys and ownership.",

                "evidence_type": "Inventory",

                "collection_method": "Key Management Console"
            },

            {
                "evidence_name": "Key Rotation Records",

                "description":
                    "Evidence demonstrating periodic key rotation activities.",

                "evidence_type": "Record",

                "collection_method": "Key Management Console"
            },

            {
                "evidence_name": "HSM Configuration Export",

                "description":
                    "Configuration of Hardware Security Modules used for key protection.",

                "evidence_type": "Configuration",

                "collection_method": "HSM Export"
            },

            {
                "evidence_name": "Key Access Review Report",

                "description":
                    "Periodic review of privileged access to cryptographic keys.",

                "evidence_type": "Report",

                "collection_method": "Access Review Report"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "Endpoint Security Management",

        [

            {
                "evidence_name": "Endpoint Security Policy",

                "description":
                    "Approved policy governing endpoint protection controls.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Endpoint Protection Dashboard",

                "description":
                    "Dashboard showing antivirus, EDR and endpoint compliance status.",

                "evidence_type": "Dashboard",

                "collection_method": "Security Console"
            },

            {
                "evidence_name": "Endpoint Compliance Report",

                "description":
                    "Compliance report for enterprise endpoints.",

                "evidence_type": "Report",

                "collection_method": "Endpoint Management Console"
            },

            {
                "evidence_name": "Endpoint Configuration Baseline",

                "description":
                    "Approved secure configuration baseline for endpoints.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Malware Detection Report",

                "description":
                    "Enterprise malware detection and remediation report.",

                "evidence_type": "Report",

                "collection_method": "EDR Dashboard"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "Firewall Security Management",

        [

            {
                "evidence_name": "Firewall Rule Base Export",

                "description":
                    "Export of current enterprise firewall rules.",

                "evidence_type": "Configuration",

                "collection_method": "Firewall Export"
            },

            {
                "evidence_name": "Firewall Rule Review Report",

                "description":
                    "Periodic review and recertification of firewall rules.",

                "evidence_type": "Report",

                "collection_method": "Firewall Dashboard"
            },

            {
                "evidence_name": "Firewall Security Policy",

                "description":
                    "Policy governing firewall administration and security.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Firewall Change Records",

                "description":
                    "Approved firewall configuration change records.",

                "evidence_type": "Record",

                "collection_method": "ITSM Export"
            },

            {
                "evidence_name": "Firewall Configuration Backup",

                "description":
                    "Backup of enterprise firewall configuration.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "Incident Management",

        [

            {
                "evidence_name": "Incident Response Policy",

                "description":
                    "Approved enterprise incident response policy.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Incident Response SOP",

                "description":
                    "Standard operating procedures for incident handling.",

                "evidence_type": "SOP",

                "collection_method": "Procedure Repository"
            },

            {
                "evidence_name": "Security Incident Register",

                "description":
                    "Register containing reported security incidents.",

                "evidence_type": "Register",

                "collection_method": "Incident Management System"
            },

            {
                "evidence_name": "Incident Investigation Reports",

                "description":
                    "Reports documenting investigation and root cause analysis.",

                "evidence_type": "Report",

                "collection_method": "Investigation Repository"
            },

            {
                "evidence_name": "Incident Response Dashboard",

                "description":
                    "Dashboard tracking incident response metrics and SLAs.",

                "evidence_type": "Dashboard",

                "collection_method": "SOC Dashboard"
            }

        ]

    )

    register_domain_evidences(

        "ITGC",

        "Logging & Monitoring",

        [

            {
                "evidence_name": "Enterprise Logging Policy",

                "description":
                    "Approved policy governing enterprise logging and monitoring.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "SIEM Dashboard",

                "description":
                    "Dashboard showing monitored security events and alerts.",

                "evidence_type": "Dashboard",

                "collection_method": "SIEM Console"
            },

            {
                "evidence_name": "SIEM Event Log Export",

                "description":
                    "Export of enterprise security events collected by SIEM.",

                "evidence_type": "Log",

                "collection_method": "SIEM Export"
            },

            {
                "evidence_name": "Log Retention Configuration",

                "description":
                    "Configuration defining enterprise log retention periods.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Security Monitoring Report",

                "description":
                    "Periodic report summarizing security monitoring activities.",

                "evidence_type": "Report",

                "collection_method": "Monitoring Dashboard"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "Network Security Architecture",

        [

            {
                "evidence_name": "Enterprise Network Architecture Diagram",

                "description":
                    "Approved network architecture showing security zones.",

                "evidence_type": "Diagram",

                "collection_method": "Architecture Repository"
            },

            {
                "evidence_name": "Network Security Standards",

                "description":
                    "Enterprise standards governing network security architecture.",

                "evidence_type": "Standard",

                "collection_method": "Standards Repository"
            },

            {
                "evidence_name": "Network Device Inventory",

                "description":
                    "Inventory of routers, switches, firewalls and network devices.",

                "evidence_type": "Inventory",

                "collection_method": "Network Inventory Export"
            },

            {
                "evidence_name": "Network Architecture Review Report",

                "description":
                    "Periodic review of enterprise network architecture.",

                "evidence_type": "Report",

                "collection_method": "Architecture Review"
            },

            {
                "evidence_name": "Network Topology Diagram",

                "description":
                    "Logical and physical topology of enterprise networks.",

                "evidence_type": "Diagram",

                "collection_method": "Network Repository"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "Network Segmentation & Perimeter Security",

        [

            {
                "evidence_name": "Network Segmentation Design",

                "description":
                    "Design document showing segmentation of enterprise networks.",

                "evidence_type": "Diagram",

                "collection_method": "Architecture Repository"
            },

            {
                "evidence_name": "Firewall Zone Configuration",

                "description":
                    "Configuration of security zones and firewall boundaries.",

                "evidence_type": "Configuration",

                "collection_method": "Firewall Export"
            },

            {
                "evidence_name": "DMZ Architecture Diagram",

                "description":
                    "Architecture diagram of DMZ and perimeter security.",

                "evidence_type": "Diagram",

                "collection_method": "Architecture Repository"
            },

            {
                "evidence_name": "Network Segmentation Review Report",

                "description":
                    "Review validating implementation of segmentation controls.",

                "evidence_type": "Report",

                "collection_method": "Assessment Report"
            },

            {
                "evidence_name": "Firewall Rule Review Report",

                "description":
                    "Evidence demonstrating periodic firewall rule review.",

                "evidence_type": "Report",

                "collection_method": "Firewall Dashboard"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "Password Management",

        [

            {
                "evidence_name": "Enterprise Password Policy",

                "description":
                    "Approved enterprise password policy.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Password Policy Configuration",

                "description":
                    "Configuration showing password complexity, expiry and history.",

                "evidence_type": "Configuration",

                "collection_method": "Active Directory Export"
            },

            {
                "evidence_name": "Password Compliance Report",

                "description":
                    "Report demonstrating compliance with password standards.",

                "evidence_type": "Report",

                "collection_method": "Identity Management Console"
            },

            {
                "evidence_name": "Authentication Configuration",

                "description":
                    "Configuration of enterprise authentication mechanisms.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Password Exception Register",

                "description":
                    "Approved exceptions related to enterprise password controls.",

                "evidence_type": "Register",

                "collection_method": "Risk Register"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "Patch Management",

        [

            {
                "evidence_name": "Patch Management Policy",

                "description":
                    "Approved enterprise patch management policy.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Patch Compliance Report",

                "description":
                    "Compliance report showing current patch status.",

                "evidence_type": "Report",

                "collection_method": "Patch Management Console"
            },

            {
                "evidence_name": "Patch Deployment Records",

                "description":
                    "Records demonstrating deployment of security patches.",

                "evidence_type": "Record",

                "collection_method": "Patch Management System"
            },

            {
                "evidence_name": "Missing Patch Report",

                "description":
                    "Report identifying systems with pending security patches.",

                "evidence_type": "Report",

                "collection_method": "Vulnerability Scanner"
            },

            {
                "evidence_name": "Patch Testing Report",

                "description":
                    "Evidence demonstrating patch validation before deployment.",

                "evidence_type": "Report",

                "collection_method": "Testing Report"
            }

        ]

    )

    register_domain_evidences(

        "ITGC",

        "Privileged Access Management",

        [

            {
                "evidence_name": "Privileged Access Management Policy",

                "description":
                    "Approved policy governing privileged account lifecycle and usage.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "PAM Vault Configuration",

                "description":
                    "Configuration of the Privileged Access Management solution.",

                "evidence_type": "Configuration",

                "collection_method": "PAM Console Export"
            },

            {
                "evidence_name": "Privileged Account Inventory",

                "description":
                    "Inventory of privileged accounts and system owners.",

                "evidence_type": "Inventory",

                "collection_method": "PAM Export"
            },

            {
                "evidence_name": "Privileged Access Review Report",

                "description":
                    "Periodic review and recertification of privileged accounts.",

                "evidence_type": "Report",

                "collection_method": "Access Review Report"
            },

            {
                "evidence_name": "Privileged Session Logs",

                "description":
                    "Logs capturing privileged user sessions and activities.",

                "evidence_type": "Log",

                "collection_method": "PAM Session Export"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "Secure Configuration Management",

        [

            {
                "evidence_name": "Secure Configuration Policy",

                "description":
                    "Approved policy governing secure system configuration baselines.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Secure Configuration Baseline",

                "description":
                    "Approved baseline configuration for enterprise systems.",

                "evidence_type": "Configuration",

                "collection_method": "Baseline Repository"
            },

            {
                "evidence_name": "System Configuration Export",

                "description":
                    "Current configuration exported from production systems.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Configuration Compliance Report",

                "description":
                    "Compliance report comparing systems against approved baselines.",

                "evidence_type": "Report",

                "collection_method": "Compliance Dashboard"
            },

            {
                "evidence_name": "CIS Benchmark Assessment Report",

                "description":
                    "Assessment report against applicable CIS Benchmarks.",

                "evidence_type": "Assessment",

                "collection_method": "Assessment Tool"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "Third-Party / Vendor Management",

        [

            {
                "evidence_name": "Vendor Security Policy",

                "description":
                    "Approved policy governing third-party security requirements.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Vendor Risk Assessment Report",

                "description":
                    "Security assessment report for third-party vendors.",

                "evidence_type": "Assessment",

                "collection_method": "Assessment Report"
            },

            {
                "evidence_name": "Vendor Inventory Register",

                "description":
                    "Inventory of approved vendors and service providers.",

                "evidence_type": "Inventory",

                "collection_method": "Vendor Management System"
            },

            {
                "evidence_name": "Vendor Security Agreement",

                "description":
                    "Executed agreements containing security and confidentiality clauses.",

                "evidence_type": "Agreement",

                "collection_method": "Contract Repository"
            },

            {
                "evidence_name": "Vendor Compliance Review Report",

                "description":
                    "Periodic review of vendor security compliance.",

                "evidence_type": "Report",

                "collection_method": "Vendor Review Report"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "User Management",

        [

            {
                "evidence_name": "User Account Management Policy",

                "description":
                    "Approved policy governing enterprise user account management.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "User Access Register",

                "description":
                    "Inventory of enterprise user accounts and assigned roles.",

                "evidence_type": "Register",

                "collection_method": "Identity Management Export"
            },

            {
                "evidence_name": "Joiner Mover Leaver Records",

                "description":
                    "Lifecycle records for user provisioning, modification and deprovisioning.",

                "evidence_type": "Record",

                "collection_method": "Identity Management System"
            },

            {
                "evidence_name": "User Access Review Report",

                "description":
                    "Periodic review and certification of user access rights.",

                "evidence_type": "Report",

                "collection_method": "Access Review Report"
            },

            {
                "evidence_name": "User Provisioning Approval Records",

                "description":
                    "Approved requests for creation and modification of user accounts.",

                "evidence_type": "Approval",

                "collection_method": "ITSM Export"
            }

        ]

    )



    register_domain_evidences(

        "ITGC",

        "Vulnerability Management",

        [

            {
                "evidence_name": "Vulnerability Management Policy",

                "description":
                    "Approved policy governing identification and remediation of vulnerabilities.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Vulnerability Scan Report",

                "description":
                    "Enterprise vulnerability assessment report.",

                "evidence_type": "Assessment",

                "collection_method": "VA Scanner Export"
            },

            {
                "evidence_name": "Remediation Tracking Report",

                "description":
                    "Report tracking remediation of identified vulnerabilities.",

                "evidence_type": "Report",

                "collection_method": "Remediation Dashboard"
            },

            {
                "evidence_name": "Risk Acceptance Register",

                "description":
                    "Approved register documenting accepted security risks.",

                "evidence_type": "Register",

                "collection_method": "Risk Register"
            },

            {
                "evidence_name": "Vulnerability Metrics Dashboard",

                "description":
                    "Dashboard showing vulnerability trends and remediation KPIs.",

                "evidence_type": "Dashboard",

                "collection_method": "Security Dashboard"
            }

        ]

    )

    # ======================================================================
    # SNA
    # ======================================================================

    register_domain_evidences(

        "SNA",

        "Architecture Governance & Change Management",

        [

            {
                "evidence_name": "Network Architecture Governance Policy",

                "description":
                    "Approved policy governing enterprise network architecture, "
                    "governance and lifecycle management.",

                "evidence_type": "Policy",

                "collection_method": "Policy Document"
            },

            {
                "evidence_name": "Network Architecture Approval Records",

                "description":
                    "Architecture Review Board approvals for network architecture "
                    "changes and implementations.",

                "evidence_type": "Approval",

                "collection_method": "Approval Records"
            },

            {
                "evidence_name": "Network Change Management Records",

                "description":
                    "Approved change requests associated with enterprise "
                    "network architecture.",

                "evidence_type": "Record",

                "collection_method": "ITSM Export"
            },

            {
                "evidence_name": "Network Architecture Standards",

                "description":
                    "Enterprise standards defining approved network "
                    "architecture principles.",

                "evidence_type": "Standard",

                "collection_method": "Standards Repository"
            },

            {
                "evidence_name": "Architecture Review Reports",

                "description":
                    "Periodic review reports validating network architecture "
                    "compliance.",

                "evidence_type": "Report",

                "collection_method": "Architecture Review"
            }

        ]

    )



    register_domain_evidences(

        "SNA",

        "Infrastructure Resilience & High Availability",

        [

            {
                "evidence_name": "High Availability Architecture Diagram",

                "description":
                    "Architecture demonstrating redundancy and "
                    "high availability design.",

                "evidence_type": "Diagram",

                "collection_method": "Architecture Repository"
            },

            {
                "evidence_name": "Infrastructure Redundancy Report",

                "description":
                    "Evidence of redundant infrastructure components "
                    "supporting business continuity.",

                "evidence_type": "Report",

                "collection_method": "Infrastructure Dashboard"
            },

            {
                "evidence_name": "Failover Test Report",

                "description":
                    "Evidence demonstrating successful failover testing.",

                "evidence_type": "Report",

                "collection_method": "DR Test Report"
            },

            {
                "evidence_name": "Load Balancer Configuration",

                "description":
                    "Configuration of enterprise load balancing infrastructure.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Infrastructure Availability Dashboard",

                "description":
                    "Dashboard monitoring availability and uptime of "
                    "critical infrastructure.",

                "evidence_type": "Dashboard",

                "collection_method": "Monitoring Dashboard"
            }

        ]

    )



    register_domain_evidences(

        "SNA",

        "Network Architecture & Documentation",

        [

            {
                "evidence_name": "Enterprise Network Architecture Document",

                "description":
                    "Approved documentation describing enterprise "
                    "network architecture.",

                "evidence_type": "Document",

                "collection_method": "Documentation Repository"
            },

            {
                "evidence_name": "Logical Network Diagram",

                "description":
                    "Logical representation of enterprise network connectivity.",

                "evidence_type": "Diagram",

                "collection_method": "Architecture Repository"
            },

            {
                "evidence_name": "Physical Network Diagram",

                "description":
                    "Physical topology of enterprise network infrastructure.",

                "evidence_type": "Diagram",

                "collection_method": "Architecture Repository"
            },

            {
                "evidence_name": "Network Device Inventory",

                "description":
                    "Inventory of routers, switches, firewalls and "
                    "network appliances.",

                "evidence_type": "Inventory",

                "collection_method": "Inventory Export"
            },

            {
                "evidence_name": "IP Address Management Register",

                "description":
                    "Enterprise IP addressing and subnet allocation register.",

                "evidence_type": "Register",

                "collection_method": "IPAM Export"
            }

        ]

    )



    register_domain_evidences(

        "SNA",

        "Network Segmentation & Perimeter Security",

        [

            {
                "evidence_name": "Network Segmentation Architecture",

                "description":
                    "Architecture demonstrating implementation of "
                    "network segmentation.",

                "evidence_type": "Diagram",

                "collection_method": "Architecture Repository"
            },

            {
                "evidence_name": "Firewall Zone Configuration",

                "description":
                    "Configuration of enterprise firewall security zones.",

                "evidence_type": "Configuration",

                "collection_method": "Firewall Export"
            },

            {
                "evidence_name": "Perimeter Security Assessment Report",

                "description":
                    "Assessment validating effectiveness of perimeter controls.",

                "evidence_type": "Assessment",

                "collection_method": "Assessment Report"
            },

            {
                "evidence_name": "Network Segmentation Review Report",

                "description":
                    "Periodic review validating implementation of "
                    "network segmentation controls.",

                "evidence_type": "Report",

                "collection_method": "Architecture Review"
            },

            {
                "evidence_name": "ACL Configuration Export",

                "description":
                    "Access Control List configuration for network devices.",

                "evidence_type": "Configuration",

                "collection_method": "Configuration Export"
            }

        ]

    )



    register_domain_evidences(

        "SNA",

        "Secure Connectivity & Communication",

        [

            {
                "evidence_name": "VPN Configuration Export",

                "description":
                    "Configuration of enterprise VPN connectivity.",

                "evidence_type": "Configuration",

                "collection_method": "VPN Console Export"
            },

            {
                "evidence_name": "TLS Configuration Report",

                "description":
                    "Configuration demonstrating secure communication protocols.",

                "evidence_type": "Report",

                "collection_method": "Configuration Export"
            },

            {
                "evidence_name": "Network Encryption Standards",

                "description":
                    "Enterprise standards governing encrypted communications.",

                "evidence_type": "Standard",

                "collection_method": "Standards Repository"
            },

            {
                "evidence_name": "Secure Communication Assessment Report",

                "description":
                    "Assessment validating secure communication controls.",

                "evidence_type": "Assessment",

                "collection_method": "Assessment Report"
            },

            {
                "evidence_name": "Network Connectivity Monitoring Dashboard",

                "description":
                    "Dashboard monitoring secure enterprise network connectivity.",

                "evidence_type": "Dashboard",

                "collection_method": "Network Monitoring Console"
            }

        ]

    )


# =============================================================================
# Register All Evidences
# =============================================================================

register_all_domain_evidences()

print()
print("=" * 80)
print("Registering Enterprise Evidences...")
print("=" * 80)

for evidences in DOMAIN_EVIDENCES.values():

    for evidence in evidences:

        evidence_name = evidence["evidence_name"]

        if evidence_name in EVIDENCE_LOOKUP:
            continue

        evidence_id = generate_evidence_id()

        EVIDENCE_LOOKUP[evidence_name] = evidence_id

        EVIDENCE_RECORDS.append({

            "Evidence ID": evidence_id,

            "Evidence Name": evidence["evidence_name"],

            "Description": evidence["description"],

            "Evidence Type": evidence["evidence_type"],

            "Collection Method": evidence["collection_method"],

            # Optional field (recommended)
            "Evidence Source": evidence.get(
                "evidence_source",
                "Not Specified"
            )

        })

print(

    f"Registered {len(EVIDENCE_RECORDS)} unique evidences."

)

# =============================================================================
# Build Evidence Library
# =============================================================================

print()
print("=" * 80)
print("Creating Evidence Library...")
print("=" * 80)

evidence_library_df = pd.DataFrame(
    EVIDENCE_RECORDS
)

print(

    f"Total Evidences : {len(evidence_library_df)}"

)

# =============================================================================
# Build Observation → Primary Evidence Mapping
# =============================================================================

print()
print("=" * 80)
print("Building Observation-Evidence Mapping...")
print("=" * 80)


def select_primary_evidence(observation, evidences):
    """
    Select the most appropriate enterprise evidence.

    Current Strategy
    ----------------
    Keyword-based matching.

    Future versions can replace this logic
    with semantic similarity or AI models
    without changing the dataset structure.
    """

    observation = str(observation).lower()

    keyword_map = {

        # ==========================================================
        # Password / IAM
        # ==========================================================

        "password": "Enterprise Password Policy",

        "complexity": "Password Policy Configuration",

        "history": "Password Policy Configuration",

        "expiry": "Password Policy Configuration",

        "lockout": "Password Policy Configuration",

        "authentication": "Authentication Configuration",

        "user": "User Access Register",

        "account": "User Access Register",

        "access": "User Access Review Report",

        "privileged": "Privileged Access Review Report",

        "pam": "PAM Vault Configuration",

        # ==========================================================
        # Backup
        # ==========================================================

        "backup": "Backup Job Reports",

        "restore": "Backup Restoration Test Report",

        "recovery": "Recovery Procedure Document",

        # ==========================================================
        # Asset
        # ==========================================================

        "asset": "Enterprise Asset Inventory",

        "inventory": "Enterprise Asset Inventory",

        # ==========================================================
        # Firewall
        # ==========================================================

        "firewall": "Firewall Rule Base Export",

        "rule": "Firewall Rule Review Report",

        # ==========================================================
        # Logging
        # ==========================================================

        "log": "SIEM Event Log Export",

        "siem": "SIEM Dashboard",

        "monitor": "Security Monitoring Report",

        "event": "SIEM Event Log Export",

        # ==========================================================
        # Incident
        # ==========================================================

        "incident": "Security Incident Register",

        "response": "Incident Response SOP",

        # ==========================================================
        # Patch
        # ==========================================================

        "patch": "Patch Compliance Report",

        "update": "Patch Deployment Records",

        # ==========================================================
        # Vulnerability
        # ==========================================================

        "vulnerability": "Vulnerability Scan Report",

        "va": "Vulnerability Scan Report",

        "remediation": "Remediation Tracking Report",

        # ==========================================================
        # Endpoint
        # ==========================================================

        "endpoint": "Endpoint Protection Dashboard",

        "antivirus": "Endpoint Protection Dashboard",

        "malware": "Malware Detection Report",

        # ==========================================================
        # Database
        # ==========================================================

        "database": "Database Audit Log Export",

        "audit": "Database Audit Log Export",

        "encryption": "Database Encryption Configuration",

        "db": "Database Security Configuration",

        # ==========================================================
        # Vendor
        # ==========================================================

        "vendor": "Vendor Risk Assessment Report",

        "third party": "Vendor Risk Assessment Report",

        # ==========================================================
        # Certificate
        # ==========================================================

        "certificate": "Certificate Inventory",

        "ssl": "Certificate Inventory",

        "tls": "TLS Configuration Report",

        # ==========================================================
        # DFD
        # ==========================================================

        "dfd": "Enterprise DFD Repository",

        "data flow": "Enterprise Data Flow Diagrams",

        "interface": "Interface Configuration Export",

        # ==========================================================
        # DFRA
        # ==========================================================

        "evidence": "Digital Evidence Inventory",

        "forensic": "Forensic Investigation SOP",

        "chain": "Chain of Custody Register",

        "hash": "Hash Verification Report",

        "ntp": "NTP Configuration Export",

        # ==========================================================
        # Network
        # ==========================================================

        "network": "Enterprise Network Architecture Document",

        "segmentation": "Network Segmentation Architecture",

        "vpn": "VPN Configuration Export",

        "communication": "TLS Configuration Report"

    }

    for keyword, evidence_name in keyword_map.items():

        if keyword in observation:

            for evidence in evidences:

                if evidence["evidence_name"] == evidence_name:

                    return evidence

    if evidences:

        return evidences[0]

    return None


for index, row in observation_df.iterrows():

    activity = str(row["Activity"]).strip()

    domain = str(row["Domain"]).strip()

    observation = row["Observation"]

    evidences = DOMAIN_EVIDENCES.get(

        (activity, domain),

        []

    )

    selected_evidence = select_primary_evidence(

        observation,

        evidences

    )

    if selected_evidence is None:

        continue

    evidence_name = selected_evidence["evidence_name"]

    evidence_id = EVIDENCE_LOOKUP[evidence_name]

    OBSERVATION_EVIDENCE_MAPPING.append({

        "Observation ID": f"OBS-{index + 1:04d}",

        "Activity": activity,

        "Domain": domain,

        "Observation": observation,

        "Evidence ID": evidence_id,

        "Evidence Name": evidence_name,

        "Evidence Type": selected_evidence["evidence_type"],

        "Collection Method": selected_evidence["collection_method"],

        "Evidence Source": selected_evidence.get(

            "evidence_source",

            "Not Specified"

        )

    })

print(

    f"Generated {len(OBSERVATION_EVIDENCE_MAPPING)} mappings."

)


# =============================================================================
# Export Evidence Library
# =============================================================================

observation_evidence_mapping_df = pd.DataFrame(
    OBSERVATION_EVIDENCE_MAPPING
)

evidence_library_df.to_excel(

    EVIDENCE_LIBRARY_PATH,

    index=False

)

observation_evidence_mapping_df.to_excel(

    OBSERVATION_EVIDENCE_MAPPING_PATH,

    index=False

)

print()

print("Evidence Library exported successfully.")

print("Observation-Evidence Mapping exported successfully.")

print()

print("=" * 80)

print("BUILD SUMMARY")

print("=" * 80)

print(f"Observations Processed : {len(observation_df)}")

print(f"Unique Evidences       : {len(evidence_library_df)}")

print(f"Mappings Generated     : {len(observation_evidence_mapping_df)}")

print("=" * 80)