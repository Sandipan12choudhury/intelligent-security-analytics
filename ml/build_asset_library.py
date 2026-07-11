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

ASSET_LIBRARY_PATH = os.path.join(
    DATASET_DIR,
    "asset_library.xlsx"
)

OBSERVATION_ASSET_MAPPING_PATH = os.path.join(
    DATASET_DIR,
    "observation_asset_mapping.xlsx"
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

print(

    f"Loaded {len(observation_df)} observations."

)

# =============================================================================
# Runtime Containers
# =============================================================================

DOMAIN_ASSETS = OrderedDict()

ASSET_LOOKUP = {}

ASSET_RECORDS = []

OBSERVATION_ASSET_MAPPING = []

asset_counter = 1

# =============================================================================
# Asset ID Generator
# =============================================================================

def generate_asset_id():

    global asset_counter

    asset_id = f"AST-{asset_counter:04d}"

    asset_counter += 1

    return asset_id

# =============================================================================
# Register Assets
# =============================================================================

def register_domain_assets(

    activity,

    domain,

    assets

):

    DOMAIN_ASSETS[(activity, domain)] = assets









# =============================================================================
# Asset Categories
# =============================================================================

ASSET_CATEGORIES = [

    "Application",

    "Database",

    "Server",

    "Endpoint",

    "Network",

    "Identity",

    "Security",

    "Cloud",

    "Data",

    "Infrastructure"

]



# =============================================================================
# Criticality Levels
# =============================================================================

CRITICALITY_LEVELS = [

    "Critical",

    "High",

    "Medium",

    "Low"

]

# =============================================================================
# Register All Enterprise Assets
# =============================================================================

def register_all_domain_assets():

    """
    Registers enterprise assets.

    IMPORTANT

    Registration order MUST follow
    observation_library.xlsx exactly.

    Duplicate assets are removed later
    while generating the master Asset Library.
    """

    # ==============================================================
    # DFA / DFD
    # ==============================================================

        # ==============================================================
    # DFA / DFD
    # ==============================================================

    register_domain_assets(

        "DFA / DFD",

        "DFD Governance & Change Management",

        [

            {
                "asset_name":
                    "Enterprise Data Flow Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Central repository maintaining approved enterprise data flow diagrams."
            },

            {
                "asset_name":
                    "Architecture Governance Platform",

                "category":
                    "Application",

                "criticality":
                    "High",

                "description":
                    "Platform supporting architecture governance, approvals and change management."
            },

            {
                "asset_name":
                    "Enterprise Architecture Documentation",

                "category":
                    "Data",

                "criticality":
                    "Medium",

                "description":
                    "Repository containing enterprise architecture and DFD documentation."
            }

        ]

    )



    register_domain_assets(

        "DFA / DFD",

        "Data Flow Documentation & Completeness",

        [

            {
                "asset_name":
                    "Enterprise Data Flow Documentation",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Documentation describing enterprise data movement and processing."
            },

            {
                "asset_name":
                    "Business Application Repository",

                "category":
                    "Application",

                "criticality":
                    "High",

                "description":
                    "Repository containing enterprise application documentation and interfaces."
            },

            {
                "asset_name":
                    "Information Asset Register",

                "category":
                    "Data",

                "criticality":
                    "Medium",

                "description":
                    "Inventory of enterprise information assets."
            }

        ]

    )



    register_domain_assets(

        "DFA / DFD",

        "Interface & Integration Security",

        [

            {
                "asset_name":
                    "Application Integration Platform",

                "category":
                    "Application",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise platform managing system integrations and interfaces."
            },

            {
                "asset_name":
                    "Enterprise APIs",

                "category":
                    "Application",

                "criticality":
                    "High",

                "description":
                    "Enterprise APIs supporting business application communication."
            },

            {
                "asset_name":
                    "Integration Gateway",

                "category":
                    "Network",

                "criticality":
                    "High",

                "description":
                    "Gateway supporting secure communication between enterprise systems."
            }

        ]

    )



    register_domain_assets(

        "DFA / DFD",

        "Sensitive Data Flow Protection",

        [

            {
                "asset_name":
                    "Sensitive Business Data",

                "category":
                    "Data",

                "criticality":
                    "Critical",

                "description":
                    "Confidential enterprise information processed across business applications."
            },

            {
                "asset_name":
                    "Data Transmission Channels",

                "category":
                    "Network",

                "criticality":
                    "High",

                "description":
                    "Enterprise communication channels transporting sensitive information."
            },

            {
                "asset_name":
                    "Encryption Infrastructure",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Security infrastructure protecting sensitive enterprise information."
            }

        ]

    )



    register_domain_assets(

        "DFA / DFD",

        "Trust Boundaries & Data Flow Security",

        [

            {
                "asset_name":
                    "Enterprise Network Boundary",

                "category":
                    "Network",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise trust boundaries protecting internal systems."
            },

            {
                "asset_name":
                    "Security Zones",

                "category":
                    "Network",

                "criticality":
                    "Critical",

                "description":
                    "Logical network zones enforcing security segregation."
            },

            {
                "asset_name":
                    "Network Trust Infrastructure",

                "category":
                    "Infrastructure",

                "criticality":
                    "High",

                "description":
                    "Infrastructure enforcing trusted communication paths."
            }

        ]

    )

    # ==============================================================
    # DFRA
    # ==============================================================

    register_domain_assets(

        "DFRA",

        "Digital Evidence Management",

        [

            {
                "asset_name":
                    "Digital Evidence Repository",

                "category":
                    "Data",

                "criticality":
                    "Critical",

                "description":
                    "Central repository storing digital evidence collected during security investigations."
            },

            {
                "asset_name":
                    "Evidence Management System",

                "category":
                    "Application",

                "criticality":
                    "High",

                "description":
                    "Enterprise platform used to manage digital evidence throughout its lifecycle."
            },

            {
                "asset_name":
                    "Chain of Custody Records",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Records maintaining integrity and traceability of digital evidence."
            }

        ]

    )



    register_domain_assets(

        "DFRA",

        "Evidence Logging & Event Capture",

        [

            {
                "asset_name":
                    "SIEM Platform",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Security Information and Event Management platform collecting enterprise security events."
            },

            {
                "asset_name":
                    "Security Log Repository",

                "category":
                    "Data",

                "criticality":
                    "Critical",

                "description":
                    "Central repository storing enterprise audit and security logs."
            },

            {
                "asset_name":
                    "Enterprise Log Collectors",

                "category":
                    "Infrastructure",

                "criticality":
                    "High",

                "description":
                    "Infrastructure responsible for collecting security events from enterprise systems."
            }

        ]

    )



    register_domain_assets(

        "DFRA",

        "Forensic Investigation Readiness",

        [

            {
                "asset_name":
                    "Forensic Workstation",

                "category":
                    "Infrastructure",

                "criticality":
                    "High",

                "description":
                    "Dedicated workstation used for forensic analysis and investigations."
            },

            {
                "asset_name":
                    "Investigation Records",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Enterprise records documenting forensic investigations and findings."
            },

            {
                "asset_name":
                    "Incident Investigation Platform",

                "category":
                    "Application",

                "criticality":
                    "High",

                "description":
                    "Platform supporting enterprise forensic investigations and incident analysis."
            }

        ]

    )



    register_domain_assets(

        "DFRA",

        "Log Retention & Preservation",

        [

            {
                "asset_name":
                    "Audit Log Archive",

                "category":
                    "Data",

                "criticality":
                    "Critical",

                "description":
                    "Long-term archive preserving enterprise audit logs."
            },

            {
                "asset_name":
                    "Enterprise Log Storage",

                "category":
                    "Infrastructure",

                "criticality":
                    "High",

                "description":
                    "Storage infrastructure retaining enterprise security logs."
            },

            {
                "asset_name":
                    "Security Archive Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository preserving historical security information."
            }

        ]

    )



    register_domain_assets(

        "DFRA",

        "Time Synchronization & Log Integrity",

        [

            {
                "asset_name":
                    "Time Synchronization Infrastructure",

                "category":
                    "Infrastructure",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise infrastructure providing synchronized system time."
            },

            {
                "asset_name":
                    "NTP Servers",

                "category":
                    "Infrastructure",

                "criticality":
                    "High",

                "description":
                    "Enterprise Network Time Protocol servers maintaining accurate timestamps."
            },

            {
                "asset_name":
                    "Log Integrity Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository maintaining integrity-protected enterprise audit logs."
            }

        ]

    )

    # ==============================================================
    # Database
    # ==============================================================

    register_domain_assets(

        "Database",

        "Database Auditing & Monitoring",

        [

            {
                "asset_name":
                    "Enterprise Database",

                "category":
                    "Database",

                "criticality":
                    "Critical",

                "description":
                    "Primary enterprise database storing business-critical information."
            },

            {
                "asset_name":
                    "Database Audit Logs",

                "category":
                    "Data",

                "criticality":
                    "Critical",

                "description":
                    "Audit logs recording all significant database activities."
            },

            {
                "asset_name":
                    "Database Monitoring Platform",

                "category":
                    "Security",

                "criticality":
                    "High",

                "description":
                    "Platform monitoring database security events and operational health."
            }

        ]

    )



    register_domain_assets(

        "Database",

        "Database Backup, Recovery & Availability",

        [

            {
                "asset_name":
                    "Database Backup Repository",

                "category":
                    "Data",

                "criticality":
                    "Critical",

                "description":
                    "Repository storing enterprise database backups."
            },

            {
                "asset_name":
                    "Database Recovery Infrastructure",

                "category":
                    "Infrastructure",

                "criticality":
                    "Critical",

                "description":
                    "Infrastructure supporting restoration and recovery of enterprise databases."
            },

            {
                "asset_name":
                    "Database High Availability Cluster",

                "category":
                    "Infrastructure",

                "criticality":
                    "Critical",

                "description":
                    "Cluster ensuring continuous database availability and resilience."
            }

        ]

    )



    register_domain_assets(

        "Database",

        "Database Configuration & Hardening",

        [

            {
                "asset_name":
                    "Database Server",

                "category":
                    "Server",

                "criticality":
                    "Critical",

                "description":
                    "Server hosting enterprise database services."
            },

            {
                "asset_name":
                    "Database Configuration Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository containing approved database configuration baselines."
            },

            {
                "asset_name":
                    "Database Hardening Baseline",

                "category":
                    "Security",

                "criticality":
                    "High",

                "description":
                    "Approved database hardening standards and security baseline."
            }

        ]

    )



    register_domain_assets(

        "Database",

        "Database Encryption & Data Protection",

        [

            {
                "asset_name":
                    "Database Encryption Infrastructure",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Encryption infrastructure protecting enterprise databases."
            },

            {
                "asset_name":
                    "Database Encryption Keys",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Cryptographic keys protecting sensitive database information."
            },

            {
                "asset_name":
                    "Sensitive Database Records",

                "category":
                    "Data",

                "criticality":
                    "Critical",

                "description":
                    "Sensitive business information stored within enterprise databases."
            }

        ]

    )



    register_domain_assets(

        "Database",

        "Database User & Access Management",

        [

            {
                "asset_name":
                    "Database Access Control System",

                "category":
                    "Identity",

                "criticality":
                    "Critical",

                "description":
                    "System managing authentication and authorization for database users."
            },

            {
                "asset_name":
                    "Database Credential Vault",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Secure vault storing privileged database credentials."
            },

            {
                "asset_name":
                    "Database User Directory",

                "category":
                    "Identity",

                "criticality":
                    "High",

                "description":
                    "Repository maintaining enterprise database user identities and permissions."
            }

        ]

    )

    # ==============================================================
    # ITGC
    # ==============================================================

    register_domain_assets(

        "ITGC",

        "Application Security Management",

        [

            {
                "asset_name":
                    "Business Applications",

                "category":
                    "Application",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise business applications supporting critical organizational operations."
            },

            {
                "asset_name":
                    "Application Servers",

                "category":
                    "Server",

                "criticality":
                    "Critical",

                "description":
                    "Servers hosting enterprise business applications."
            },

            {
                "asset_name":
                    "Application Security Platform",

                "category":
                    "Security",

                "criticality":
                    "High",

                "description":
                    "Platform responsible for application security monitoring and protection."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Asset Management",

        [

            {
                "asset_name":
                    "Enterprise Asset Inventory",

                "category":
                    "Data",

                "criticality":
                    "Critical",

                "description":
                    "Central inventory of enterprise IT assets."
            },

            {
                "asset_name":
                    "Configuration Management Database (CMDB)",

                "category":
                    "Infrastructure",

                "criticality":
                    "Critical",

                "description":
                    "Repository containing configuration and lifecycle information for enterprise assets."
            },

            {
                "asset_name":
                    "Critical Asset Register",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Register identifying business-critical information assets."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Backup & Restoration",

        [

            {
                "asset_name":
                    "Enterprise Backup Infrastructure",

                "category":
                    "Infrastructure",

                "criticality":
                    "Critical",

                "description":
                    "Infrastructure responsible for enterprise backup operations."
            },

            {
                "asset_name":
                    "Backup Storage Repository",

                "category":
                    "Data",

                "criticality":
                    "Critical",

                "description":
                    "Repository storing enterprise backup copies."
            },

            {
                "asset_name":
                    "Backup Management Server",

                "category":
                    "Server",

                "criticality":
                    "High",

                "description":
                    "Server managing enterprise backup and restoration activities."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Business Continuity & Disaster Recovery",

        [

            {
                "asset_name":
                    "Disaster Recovery Site",

                "category":
                    "Infrastructure",

                "criticality":
                    "Critical",

                "description":
                    "Secondary site supporting enterprise disaster recovery operations."
            },

            {
                "asset_name":
                    "Business Continuity Platform",

                "category":
                    "Application",

                "criticality":
                    "High",

                "description":
                    "Platform supporting enterprise business continuity planning."
            },

            {
                "asset_name":
                    "Disaster Recovery Infrastructure",

                "category":
                    "Infrastructure",

                "criticality":
                    "Critical",

                "description":
                    "Infrastructure supporting enterprise disaster recovery capabilities."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Certificate Management",

        [

            {
                "asset_name":
                    "PKI Infrastructure",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise Public Key Infrastructure supporting digital trust."
            },

            {
                "asset_name":
                    "Digital Certificate Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository storing enterprise digital certificates."
            },

            {
                "asset_name":
                    "Certificate Authority",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise Certificate Authority issuing and managing digital certificates."
            }

        ]

    )

    register_domain_assets(

        "ITGC",

        "Change Management",

        [

            {
                "asset_name":
                    "Change Management System",

                "category":
                    "Application",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise platform managing IT change requests, approvals and implementation."
            },

            {
                "asset_name":
                    "Change Approval Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository storing approved enterprise change records."
            },

            {
                "asset_name":
                    "Production Environment",

                "category":
                    "Infrastructure",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise production environment where approved changes are deployed."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Cryptographic Key Management",

        [

            {
                "asset_name":
                    "Enterprise Key Management System",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Centralized system managing enterprise cryptographic keys."
            },

            {
                "asset_name":
                    "Hardware Security Module (HSM)",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Hardware device providing secure generation and storage of cryptographic keys."
            },

            {
                "asset_name":
                    "Enterprise Cryptographic Keys",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Cryptographic keys protecting enterprise applications and sensitive information."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Endpoint Security Management",

        [

            {
                "asset_name":
                    "Enterprise Endpoints",

                "category":
                    "Endpoint",

                "criticality":
                    "High",

                "description":
                    "Enterprise desktops, laptops and workstations used by employees."
            },

            {
                "asset_name":
                    "Endpoint Protection Platform",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise endpoint protection platform providing antivirus and EDR capabilities."
            },

            {
                "asset_name":
                    "Endpoint Management Server",

                "category":
                    "Server",

                "criticality":
                    "High",

                "description":
                    "Central server managing enterprise endpoint security policies."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Firewall Security Management",

        [

            {
                "asset_name":
                    "Enterprise Firewall",

                "category":
                    "Network",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise firewall protecting organizational network boundaries."
            },

            {
                "asset_name":
                    "Firewall Management Console",

                "category":
                    "Security",

                "criticality":
                    "High",

                "description":
                    "Centralized console used to manage firewall policies and configurations."
            },

            {
                "asset_name":
                    "Firewall Rule Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository containing approved enterprise firewall rules."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Incident Management",

        [

            {
                "asset_name":
                    "Incident Management Platform",

                "category":
                    "Application",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise platform managing security incidents throughout their lifecycle."
            },

            {
                "asset_name":
                    "Security Operations Center (SOC)",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Centralized security operations center monitoring enterprise security events."
            },

            {
                "asset_name":
                    "Incident Response Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository storing incident response records, investigations and lessons learned."
            }

        ]

    )


    register_domain_assets(

        "ITGC",

        "Logging & Monitoring",

        [

            {
                "asset_name":
                    "Enterprise SIEM Platform",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Centralized SIEM platform collecting, correlating and monitoring enterprise security events."
            },

            {
                "asset_name":
                    "Security Log Management System",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise platform managing audit logs from applications, servers and network devices."
            },

            {
                "asset_name":
                    "Security Monitoring Dashboard",

                "category":
                    "Application",

                "criticality":
                    "High",

                "description":
                    "Dashboard providing centralized visibility into enterprise security events."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Network Security Architecture",

        [

            {
                "asset_name":
                    "Enterprise Network Infrastructure",

                "category":
                    "Network",

                "criticality":
                    "Critical",

                "description":
                    "Core enterprise network infrastructure supporting organizational connectivity."
            },

            {
                "asset_name":
                    "Network Architecture Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository containing approved network architecture documentation."
            },

            {
                "asset_name":
                    "Core Network Devices",

                "category":
                    "Network",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise routers, switches and core networking equipment."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Network Segmentation & Perimeter Security",

        [

            {
                "asset_name":
                    "Internal Network Segments",

                "category":
                    "Network",

                "criticality":
                    "Critical",

                "description":
                    "Logical network segments separating enterprise business environments."
            },

            {
                "asset_name":
                    "Perimeter Security Infrastructure",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Security infrastructure protecting enterprise network boundaries."
            },

            {
                "asset_name":
                    "DMZ Infrastructure",

                "category":
                    "Network",

                "criticality":
                    "High",

                "description":
                    "Demilitarized zone hosting externally accessible enterprise services."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Password Management",

        [

            {
                "asset_name":
                    "Enterprise Identity Store",

                "category":
                    "Identity",

                "criticality":
                    "Critical",

                "description":
                    "Central repository storing enterprise user identities and credentials."
            },

            {
                "asset_name":
                    "Password Vault",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Secure vault storing privileged and service account passwords."
            },

            {
                "asset_name":
                    "Authentication Services",

                "category":
                    "Identity",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise authentication services validating user identities."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Patch Management",

        [

            {
                "asset_name":
                    "Patch Management Server",

                "category":
                    "Server",

                "criticality":
                    "High",

                "description":
                    "Server responsible for distributing security patches across enterprise systems."
            },

            {
                "asset_name":
                    "Enterprise Operating Systems",

                "category":
                    "Server",

                "criticality":
                    "Critical",

                "description":
                    "Operating systems supporting enterprise servers and business infrastructure."
            },

            {
                "asset_name":
                    "Vulnerability Remediation Platform",

                "category":
                    "Security",

                "criticality":
                    "High",

                "description":
                    "Platform managing vulnerability remediation and security patch deployment."
            }

        ]

    )

    register_domain_assets(

        "ITGC",

        "Privileged Access Management",

        [

            {
                "asset_name":
                    "Privileged Access Management (PAM) Solution",

                "category":
                    "Identity",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise PAM solution managing privileged identities and administrative sessions."
            },

            {
                "asset_name":
                    "Privileged Account Repository",

                "category":
                    "Identity",

                "criticality":
                    "Critical",

                "description":
                    "Repository maintaining privileged enterprise accounts."
            },

            {
                "asset_name":
                    "Administrative Workstations",

                "category":
                    "Endpoint",

                "criticality":
                    "High",

                "description":
                    "Dedicated workstations used for privileged administrative activities."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Secure Configuration Management",

        [

            {
                "asset_name":
                    "Configuration Management Platform",

                "category":
                    "Application",

                "criticality":
                    "Critical",

                "description":
                    "Platform managing secure configuration baselines across enterprise systems."
            },

            {
                "asset_name":
                    "Configuration Baseline Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository storing approved secure configuration baselines."
            },

            {
                "asset_name":
                    "Enterprise Configuration Database",

                "category":
                    "Infrastructure",

                "criticality":
                    "High",

                "description":
                    "Central database maintaining enterprise configuration information."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Third-Party / Vendor Management",

        [

            {
                "asset_name":
                    "Vendor Management System",

                "category":
                    "Application",

                "criticality":
                    "High",

                "description":
                    "Enterprise platform managing third-party vendors and suppliers."
            },

            {
                "asset_name":
                    "Third-Party Access Gateway",

                "category":
                    "Network",

                "criticality":
                    "Critical",

                "description":
                    "Gateway controlling vendor and third-party remote access."
            },

            {
                "asset_name":
                    "Vendor Risk Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository storing vendor risk assessments and compliance information."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "User Management",

        [

            {
                "asset_name":
                    "Enterprise Directory Services",

                "category":
                    "Identity",

                "criticality":
                    "Critical",

                "description":
                    "Central directory service managing enterprise user identities."
            },

            {
                "asset_name":
                    "Identity Governance Platform",

                "category":
                    "Identity",

                "criticality":
                    "Critical",

                "description":
                    "Platform supporting user provisioning, de-provisioning and access governance."
            },

            {
                "asset_name":
                    "HR Identity Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository synchronizing employee identity information with enterprise systems."
            }

        ]

    )



    register_domain_assets(

        "ITGC",

        "Vulnerability Management",

        [

            {
                "asset_name":
                    "Vulnerability Management Platform",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise platform managing vulnerability discovery, assessment and remediation."
            },

            {
                "asset_name":
                    "Vulnerability Assessment Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository storing vulnerability assessment reports and remediation status."
            },

            {
                "asset_name":
                    "Security Scanning Infrastructure",

                "category":
                    "Security",

                "criticality":
                    "High",

                "description":
                    "Infrastructure performing enterprise vulnerability scanning and security assessments."
            }

        ]

    )

    # ==============================================================
    # SNA
    # ==============================================================

    register_domain_assets(

        "SNA",

        "Architecture Governance & Change Management",

        [

            {
                "asset_name":
                    "Enterprise Network Architecture Repository",

                "category":
                    "Data",

                "criticality":
                    "Critical",

                "description":
                    "Repository maintaining approved enterprise network architecture documents."
            },

            {
                "asset_name":
                    "Network Architecture Governance Platform",

                "category":
                    "Application",

                "criticality":
                    "High",

                "description":
                    "Platform supporting governance, approval and lifecycle management of network architecture."
            },

            {
                "asset_name":
                    "Network Change Management System",

                "category":
                    "Application",

                "criticality":
                    "High",

                "description":
                    "Enterprise platform managing network infrastructure changes."
            }

        ]

    )



    register_domain_assets(

        "SNA",

        "Infrastructure Resilience & High Availability",

        [

            {
                "asset_name":
                    "Enterprise Network Infrastructure",

                "category":
                    "Infrastructure",

                "criticality":
                    "Critical",

                "description":
                    "Core enterprise infrastructure supporting resilient business operations."
            },

            {
                "asset_name":
                    "High Availability Cluster",

                "category":
                    "Infrastructure",

                "criticality":
                    "Critical",

                "description":
                    "Cluster providing redundancy and continuous service availability."
            },

            {
                "asset_name":
                    "Load Balancing Infrastructure",

                "category":
                    "Network",

                "criticality":
                    "High",

                "description":
                    "Infrastructure distributing traffic across enterprise services."
            }

        ]

    )



    register_domain_assets(

        "SNA",

        "Network Architecture & Documentation",

        [

            {
                "asset_name":
                    "Enterprise Network Documentation",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Approved documentation describing enterprise network topology."
            },

            {
                "asset_name":
                    "Network Topology Repository",

                "category":
                    "Data",

                "criticality":
                    "High",

                "description":
                    "Repository maintaining enterprise network diagrams and topology information."
            },

            {
                "asset_name":
                    "Core Network Architecture",

                "category":
                    "Network",

                "criticality":
                    "Critical",

                "description":
                    "Logical and physical architecture supporting enterprise networking."
            }

        ]

    )



    register_domain_assets(

        "SNA",

        "Network Segmentation & Perimeter Security",

        [

            {
                "asset_name":
                    "Enterprise Network Segments",

                "category":
                    "Network",

                "criticality":
                    "Critical",

                "description":
                    "Segmented enterprise networks enforcing security isolation."
            },

            {
                "asset_name":
                    "Perimeter Firewall Infrastructure",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Perimeter security infrastructure protecting enterprise network boundaries."
            },

            {
                "asset_name":
                    "Internal Security Zones",

                "category":
                    "Network",

                "criticality":
                    "High",

                "description":
                    "Security zones separating enterprise systems based on trust levels."
            }

        ]

    )



    register_domain_assets(

        "SNA",

        "Secure Connectivity & Communication",

        [

            {
                "asset_name":
                    "Enterprise VPN Infrastructure",

                "category":
                    "Network",

                "criticality":
                    "Critical",

                "description":
                    "Enterprise VPN infrastructure providing secure remote connectivity."
            },

            {
                "asset_name":
                    "Secure Communication Gateway",

                "category":
                    "Security",

                "criticality":
                    "Critical",

                "description":
                    "Gateway securing enterprise communication channels."
            },

            {
                "asset_name":
                    "TLS Certificate Infrastructure",

                "category":
                    "Security",

                "criticality":
                    "High",

                "description":
                    "Infrastructure supporting encrypted enterprise communications."
            }

        ]

    )

# =============================================================================
# Register All Enterprise Assets
# =============================================================================

register_all_domain_assets()

print()

print("=" * 80)

print("Registering Enterprise Assets...")

print("=" * 80)

for assets in DOMAIN_ASSETS.values():

    for asset in assets:

        asset_name = asset["asset_name"]

        if asset_name in ASSET_LOOKUP:

            continue

        asset_id = generate_asset_id()

        ASSET_LOOKUP[asset_name] = asset_id

        ASSET_RECORDS.append({

            "Asset ID":
                asset_id,

            "Asset Name":
                asset["asset_name"],

            "Asset Category":
                asset["category"],

            "Criticality":
                asset["criticality"],

            "Description":
                asset["description"]

        })

print(

    f"Registered {len(ASSET_RECORDS)} unique assets."

)

# =============================================================================
# Build Asset Library
# =============================================================================

print()

print("=" * 80)

print("Creating Asset Library...")

print("=" * 80)

asset_library_df = pd.DataFrame(

    ASSET_RECORDS

)

print(

    f"Total Assets : {len(asset_library_df)}"

)

# =============================================================================
# Build Observation → Asset Mapping
# =============================================================================

print()

print("=" * 80)

print("Building Observation-Asset Mapping...")

print("=" * 80)


def select_primary_asset(observation, assets):

    """
    Select the most appropriate enterprise asset.

    Current Strategy
    ----------------
    Keyword-based matching.

    Future versions may use
    semantic similarity or AI.
    """

    observation = str(observation).lower()

    keyword_map = {

        # ==========================================================
        # Identity
        # ==========================================================

        "password":
            "Password Vault",

        "credential":
            "Enterprise Identity Store",

        "authentication":
            "Authentication Services",

        "user":
            "Enterprise Directory Services",

        "privileged":
            "Privileged Access Management (PAM) Solution",

        "pam":
            "Privileged Access Management (PAM) Solution",

        # ==========================================================
        # Database
        # ==========================================================

        "database":
            "Enterprise Database",

        "audit":
            "Database Audit Logs",

        "backup":
            "Database Backup Repository",

        "restore":
            "Database Recovery Infrastructure",

        "encryption":
            "Database Encryption Infrastructure",

        "key":
            "Enterprise Key Management System",

        # ==========================================================
        # Logging
        # ==========================================================

        "log":
            "Enterprise SIEM Platform",

        "logging":
            "Security Log Management System",

        "siem":
            "Enterprise SIEM Platform",

        # ==========================================================
        # Network
        # ==========================================================

        "firewall":
            "Enterprise Firewall",

        "network":
            "Enterprise Network Infrastructure",

        "segmentation":
            "Enterprise Network Segments",

        "vpn":
            "Enterprise VPN Infrastructure",

        "certificate":
            "PKI Infrastructure",

        # ==========================================================
        # Endpoint
        # ==========================================================

        "endpoint":
            "Enterprise Endpoints",

        "antivirus":
            "Endpoint Protection Platform",

        # ==========================================================
        # Patch
        # ==========================================================

        "patch":
            "Patch Management Server",

        "vulnerability":
            "Vulnerability Management Platform",

        # ==========================================================
        # Application
        # ==========================================================

        "application":
            "Business Applications",

        "api":
            "Application Integration Platform",

        # ==========================================================
        # Vendor
        # ==========================================================

        "vendor":
            "Vendor Management System",

        "third party":
            "Third-Party Access Gateway",

        # ==========================================================
        # DFD
        # ==========================================================

        "dfd":
            "Enterprise Data Flow Repository",

        "data flow":
            "Enterprise Data Flow Documentation",

        "interface":
            "Application Integration Platform",

        # ==========================================================
        # DFRA
        # ==========================================================

        "evidence":
            "Digital Evidence Repository",

        "forensic":
            "Forensic Workstation",

        "timestamp":
            "Time Synchronization Infrastructure",

        "ntp":
            "NTP Servers"

    }

    for keyword, asset_name in keyword_map.items():

        if keyword in observation:

            for asset in assets:

                if asset["asset_name"] == asset_name:

                    return asset

    return assets[0]


for index, row in observation_df.iterrows():

    activity = str(row["Activity"]).strip()

    domain = str(row["Domain"]).strip()

    observation = row["Observation"]

    assets = DOMAIN_ASSETS.get(

        (activity, domain),

        []

    )

    if not assets:

        continue

    selected_asset = select_primary_asset(

        observation,

        assets

    )

    asset_id = ASSET_LOOKUP[

        selected_asset["asset_name"]

    ]

    OBSERVATION_ASSET_MAPPING.append({

        "Observation ID":

            f"OBS-{index + 1:04d}",

        "Activity":

            activity,

        "Domain":

            domain,

        "Observation":

            observation,

        "Asset ID":

            asset_id,

        "Asset Name":

            selected_asset["asset_name"],

        "Asset Category":

            selected_asset["category"],

        "Criticality":

            selected_asset["criticality"]

    })

print(

    f"Generated {len(OBSERVATION_ASSET_MAPPING)} mappings."

)

# =============================================================================
# Export Asset Library
# =============================================================================

observation_asset_mapping_df = pd.DataFrame(

    OBSERVATION_ASSET_MAPPING

)

asset_library_df.to_excel(

    ASSET_LIBRARY_PATH,

    index=False

)

observation_asset_mapping_df.to_excel(

    OBSERVATION_ASSET_MAPPING_PATH,

    index=False

)

print()

print("Asset Library exported successfully.")

print("Observation-Asset Mapping exported successfully.")

print()

print("=" * 80)

print("BUILD SUMMARY")

print("=" * 80)

print(f"Observations Processed : {len(observation_df)}")

print(f"Unique Assets          : {len(asset_library_df)}")

print(f"Mappings Generated     : {len(observation_asset_mapping_df)}")

print("=" * 80)

