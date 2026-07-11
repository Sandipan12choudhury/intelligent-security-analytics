import os
from collections import OrderedDict

import pandas as pd


# =============================================================================
# Repository Paths
# =============================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_DIR = os.path.join(
    BASE_DIR,
    "dataset"
)

OBSERVATION_LIBRARY_PATH = os.path.join(
    DATASET_DIR,
    "observation_library.xlsx"
)

THREAT_LIBRARY_PATH = os.path.join(
    DATASET_DIR,
    "threat_library.xlsx"
)

OBSERVATION_THREAT_MAPPING_PATH = os.path.join(
    DATASET_DIR,
    "observation_threat_mapping.xlsx"
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

DOMAIN_THREATS = OrderedDict()

THREAT_LOOKUP = {}

THREAT_RECORDS = []

OBSERVATION_THREAT_MAPPING = []

threat_counter = 1

# =============================================================================
# Threat ID Generator
# =============================================================================

def generate_threat_id():

    """
    Generates sequential Threat IDs.

    Example

    THR-0001
    THR-0002
    """

    global threat_counter

    threat_id = f"THR-{threat_counter:04d}"

    threat_counter += 1

    return threat_id


# =============================================================================
# Register Threats
# =============================================================================

def register_domain_threats(

    activity,

    domain,

    threats

):

    """
    Registers enterprise threats
    belonging to one security domain.
    """

    DOMAIN_THREATS[(activity, domain)] = threats


# =============================================================================
# Threat Categories
# =============================================================================

THREAT_CATEGORIES = [

    "Identity",

    "Access",

    "Application",

    "Network",

    "Database",

    "Data",

    "Malware",

    "Infrastructure",

    "Insider",

    "Supply Chain"

]


# =============================================================================
# Attack Vectors
# =============================================================================

ATTACK_VECTORS = [

    "Password",

    "Credential",

    "Application",

    "API",

    "Network",

    "Database",

    "VPN",

    "Endpoint",

    "Email",

    "Cloud",

    "Third Party",

    "Insider"

]


# =============================================================================
# MITRE ATT&CK Tactics
# =============================================================================

MITRE_TACTICS = [

    "Initial Access",

    "Execution",

    "Persistence",

    "Privilege Escalation",

    "Defense Evasion",

    "Credential Access",

    "Discovery",

    "Lateral Movement",

    "Collection",

    "Command and Control",

    "Exfiltration",

    "Impact"
]

# =============================================================================
# Register All Enterprise Threats
# =============================================================================

def register_all_domain_threats():

    """
    Registers enterprise threats.

    IMPORTANT

    Registration order MUST follow

    observation_library.xlsx exactly.

    Duplicate threats are removed later
    while generating the master Threat Library.
    """

    # ==============================================================
    # DFA / DFD
    # ==============================================================

        # ==============================================================
    # DFA / DFD
    # ==============================================================

    register_domain_threats(

        "DFA / DFD",

        "DFD Governance & Change Management",

        [

            {
                "threat_name":
                    "Unauthorized Data Flow",

                "category":
                    "Data",

                "description":
                    "Unapproved or undocumented data flows may bypass enterprise security controls.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Architecture Manipulation",

                "category":
                    "Application",

                "description":
                    "Attackers exploit poorly governed architecture changes to introduce insecure data paths.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Persistence"
            },

            {
                "threat_name":
                    "Shadow Data Processing",

                "category":
                    "Data",

                "description":
                    "Undocumented business processes process sensitive information outside approved governance.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Collection"
            }

        ]

    )



    register_domain_threats(

        "DFA / DFD",

        "Data Flow Documentation & Completeness",

        [

            {
                "threat_name":
                    "Unknown Data Exposure",

                "category":
                    "Data",

                "description":
                    "Incomplete documentation causes unidentified sensitive data exposure.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Collection"
            },

            {
                "threat_name":
                    "Data Leakage",

                "category":
                    "Data",

                "description":
                    "Sensitive information flows through undocumented communication paths.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Exfiltration"
            },

            {
                "threat_name":
                    "Unauthorized Information Disclosure",

                "category":
                    "Data",

                "description":
                    "Lack of visibility into information flows exposes confidential information.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Exfiltration"
            }

        ]

    )



    register_domain_threats(

        "DFA / DFD",

        "Interface & Integration Security",

        [

            {
                "threat_name":
                    "API Abuse",

                "category":
                    "Application",

                "description":
                    "Attackers exploit insecure interfaces or integrations.",

                "attack_vector":
                    "API",

                "mitre_tactic":
                    "Initial Access"
            },

            {
                "threat_name":
                    "Unauthorized System Integration",

                "category":
                    "Application",

                "description":
                    "Untrusted systems communicate with enterprise applications.",

                "attack_vector":
                    "API",

                "mitre_tactic":
                    "Lateral Movement"
            },

            {
                "threat_name":
                    "Interface Tampering",

                "category":
                    "Application",

                "description":
                    "Malicious modification of enterprise system interfaces.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Defense Evasion"
            }

        ]

    )



    register_domain_threats(

        "DFA / DFD",

        "Sensitive Data Flow Protection",

        [

            {
                "threat_name":
                    "Sensitive Data Exfiltration",

                "category":
                    "Data",

                "description":
                    "Attackers steal confidential enterprise information during transmission.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Exfiltration"
            },

            {
                "threat_name":
                    "Data Interception",

                "category":
                    "Network",

                "description":
                    "Sensitive information is intercepted during communication.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Collection"
            },

            {
                "threat_name":
                    "Information Disclosure",

                "category":
                    "Data",

                "description":
                    "Confidential information becomes exposed through insecure data flows.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Exfiltration"
            }

        ]

    )



    register_domain_threats(

        "DFA / DFD",

        "Trust Boundaries & Data Flow Security",

        [

            {
                "threat_name":
                    "Lateral Movement",

                "category":
                    "Network",

                "description":
                    "Attackers move across enterprise trust boundaries after initial compromise.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Lateral Movement"
            },

            {
                "threat_name":
                    "Trust Boundary Bypass",

                "category":
                    "Network",

                "description":
                    "Security boundaries are bypassed allowing unauthorized communication.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Unauthorized Network Access",

                "category":
                    "Network",

                "description":
                    "Attackers obtain access across improperly protected trust zones.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Initial Access"
            }

        ]

    )

    # ==============================================================
    # DFRA
    # ==============================================================

    register_domain_threats(

        "DFRA",

        "Digital Evidence Management",

        [

            {
                "threat_name":
                    "Evidence Tampering",

                "category":
                    "Data",

                "description":
                    "Attackers modify or alter digital evidence to obstruct investigations.",

                "attack_vector":
                    "Insider",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Evidence Destruction",

                "category":
                    "Data",

                "description":
                    "Critical forensic evidence is intentionally deleted or destroyed.",

                "attack_vector":
                    "Insider",

                "mitre_tactic":
                    "Impact"
            },

            {
                "threat_name":
                    "Chain of Custody Compromise",

                "category":
                    "Data",

                "description":
                    "Loss of integrity in digital evidence due to improper handling or malicious actions.",

                "attack_vector":
                    "Insider",

                "mitre_tactic":
                    "Defense Evasion"
            }

        ]

    )



    register_domain_threats(

        "DFRA",

        "Evidence Logging & Event Capture",

        [

            {
                "threat_name":
                    "Log Deletion",

                "category":
                    "Infrastructure",

                "description":
                    "Security logs are deleted to conceal malicious activities.",

                "attack_vector":
                    "Endpoint",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Log Poisoning",

                "category":
                    "Infrastructure",

                "description":
                    "Attackers inject misleading log entries to disrupt investigations.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Security Event Suppression",

                "category":
                    "Infrastructure",

                "description":
                    "Critical security events fail to be captured or reported.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Defense Evasion"
            }

        ]

    )



    register_domain_threats(

        "DFRA",

        "Forensic Investigation Readiness",

        [

            {
                "threat_name":
                    "Anti-Forensics",

                "category":
                    "Insider",

                "description":
                    "Techniques used to obstruct or mislead forensic investigations.",

                "attack_vector":
                    "Endpoint",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Investigation Evasion",

                "category":
                    "Insider",

                "description":
                    "Attackers evade forensic detection through deliberate manipulation.",

                "attack_vector":
                    "Endpoint",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Forensic Artifact Removal",

                "category":
                    "Infrastructure",

                "description":
                    "Deletion of forensic artifacts to prevent incident reconstruction.",

                "attack_vector":
                    "Endpoint",

                "mitre_tactic":
                    "Impact"
            }

        ]

    )



    register_domain_threats(

        "DFRA",

        "Log Retention & Preservation",

        [

            {
                "threat_name":
                    "Audit Trail Manipulation",

                "category":
                    "Infrastructure",

                "description":
                    "Audit trails are modified or truncated to conceal malicious activities.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Log Retention Bypass",

                "category":
                    "Infrastructure",

                "description":
                    "Security logs are removed before the required retention period.",

                "attack_vector":
                    "Endpoint",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Audit Evidence Loss",

                "category":
                    "Data",

                "description":
                    "Loss of audit evidence prevents accurate incident investigations.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Impact"
            }

        ]

    )



    register_domain_threats(

        "DFRA",

        "Time Synchronization & Log Integrity",

        [

            {
                "threat_name":
                    "Timestamp Manipulation",

                "category":
                    "Infrastructure",

                "description":
                    "System timestamps are altered to hide attacker activities.",

                "attack_vector":
                    "Endpoint",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Clock Synchronization Attack",

                "category":
                    "Infrastructure",

                "description":
                    "Compromise of enterprise time synchronization affecting forensic timelines.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Impact"
            },

            {
                "threat_name":
                    "Log Integrity Compromise",

                "category":
                    "Infrastructure",

                "description":
                    "Security logs lose integrity due to unauthorized modification.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Defense Evasion"
            }

        ]

    )

    # ==============================================================
    # Database
    # ==============================================================

    register_domain_threats(

        "Database",

        "Database Auditing & Monitoring",

        [

            {
                "threat_name":
                    "Unauthorized Database Access",

                "category":
                    "Database",

                "description":
                    "Attackers access enterprise databases without detection due to inadequate auditing and monitoring.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Credential Access"
            },

            {
                "threat_name":
                    "Audit Log Evasion",

                "category":
                    "Database",

                "description":
                    "Malicious database activities remain undetected because audit logging is incomplete or disabled.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Database Activity Concealment",

                "category":
                    "Database",

                "description":
                    "Attackers conceal unauthorized database activities by bypassing monitoring controls.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Defense Evasion"
            }

        ]

    )



    register_domain_threats(

        "Database",

        "Database Backup, Recovery & Availability",

        [

            {
                "threat_name":
                    "Backup Data Theft",

                "category":
                    "Data",

                "description":
                    "Database backups are stolen, exposing sensitive enterprise information.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Collection"
            },

            {
                "threat_name":
                    "Database Service Disruption",

                "category":
                    "Infrastructure",

                "description":
                    "Failure or corruption of database backups results in prolonged service disruption.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Impact"
            },

            {
                "threat_name":
                    "Recovery Process Manipulation",

                "category":
                    "Infrastructure",

                "description":
                    "Recovery mechanisms are manipulated, delaying restoration following an incident.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Impact"
            }

        ]

    )



    register_domain_threats(

        "Database",

        "Database Configuration & Hardening",

        [

            {
                "threat_name":
                    "Database Configuration Abuse",

                "category":
                    "Database",

                "description":
                    "Attackers exploit insecure database configurations to gain unauthorized capabilities.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Privilege Escalation"
            },

            {
                "threat_name":
                    "Database Privilege Escalation",

                "category":
                    "Database",

                "description":
                    "Weak hardening enables attackers to obtain elevated database privileges.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Privilege Escalation"
            },

            {
                "threat_name":
                    "SQL Injection",

                "category":
                    "Application",

                "description":
                    "Attackers exploit insecure application-database interactions to execute unauthorized SQL commands.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Execution"
            }

        ]

    )



    register_domain_threats(

        "Database",

        "Database Encryption & Data Protection",

        [

            {
                "threat_name":
                    "Database Encryption Bypass",

                "category":
                    "Database",

                "description":
                    "Attackers bypass encryption controls protecting enterprise databases.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Sensitive Data Exfiltration",

                "category":
                    "Data",

                "description":
                    "Sensitive enterprise information is extracted from databases.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Exfiltration"
            },

            {
                "threat_name":
                    "Cryptographic Key Compromise",

                "category":
                    "Data",

                "description":
                    "Compromise of encryption keys results in unauthorized access to protected database information.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Credential Access"
            }

        ]

    )



    register_domain_threats(

        "Database",

        "Database User & Access Management",

        [

            {
                "threat_name":
                    "Database Credential Theft",

                "category":
                    "Identity",

                "description":
                    "Attackers steal database credentials to gain unauthorized access.",

                "attack_vector":
                    "Credential",

                "mitre_tactic":
                    "Credential Access"
            },

            {
                "threat_name":
                    "Insider Database Abuse",

                "category":
                    "Insider",

                "description":
                    "Privileged insiders misuse legitimate database access for unauthorized purposes.",

                "attack_vector":
                    "Insider",

                "mitre_tactic":
                    "Collection"
            },

            {
                "threat_name":
                    "Unauthorized Privileged Database Access",

                "category":
                    "Database",

                "description":
                    "Attackers exploit excessive or unmanaged privileges to access critical database resources.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Privilege Escalation"
            }

        ]

    )

    # ==============================================================
    # ITGC
    # ==============================================================

    register_domain_threats(

        "ITGC",

        "Application Security Management",

        [

            {
                "threat_name":
                    "Application Exploitation",

                "category":
                    "Application",

                "description":
                    "Attackers exploit weaknesses in enterprise applications to gain unauthorized access or execute malicious actions.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Execution"
            },

            {
                "threat_name":
                    "Remote Code Execution",

                "category":
                    "Application",

                "description":
                    "Application vulnerabilities allow attackers to execute arbitrary code.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Execution"
            },

            {
                "threat_name":
                    "Application Privilege Escalation",

                "category":
                    "Application",

                "description":
                    "Weak application security enables attackers to elevate privileges within enterprise systems.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Privilege Escalation"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Asset Management",

        [

            {
                "threat_name":
                    "Shadow IT",

                "category":
                    "Infrastructure",

                "description":
                    "Unmanaged enterprise assets operate outside approved governance and security controls.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Initial Access"
            },

            {
                "threat_name":
                    "Unauthorized Asset Usage",

                "category":
                    "Infrastructure",

                "description":
                    "Enterprise assets are used without authorization or ownership accountability.",

                "attack_vector":
                    "Insider",

                "mitre_tactic":
                    "Persistence"
            },

            {
                "threat_name":
                    "Unknown Critical Assets",

                "category":
                    "Infrastructure",

                "description":
                    "Critical enterprise assets remain unidentified, increasing attack exposure.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Discovery"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Backup & Restoration",

        [

            {
                "threat_name":
                    "Backup Compromise",

                "category":
                    "Data",

                "description":
                    "Attackers compromise enterprise backups, reducing recovery capability.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Impact"
            },

            {
                "threat_name":
                    "Backup Deletion",

                "category":
                    "Data",

                "description":
                    "Enterprise backup repositories are intentionally deleted or corrupted.",

                "attack_vector":
                    "Insider",

                "mitre_tactic":
                    "Impact"
            },

            {
                "threat_name":
                    "Recovery Failure",

                "category":
                    "Infrastructure",

                "description":
                    "Recovery procedures fail due to compromised or untested backups.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Impact"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Business Continuity & Disaster Recovery",

        [

            {
                "threat_name":
                    "Service Outage",

                "category":
                    "Infrastructure",

                "description":
                    "Critical enterprise services become unavailable following disruptive events.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Impact"
            },

            {
                "threat_name":
                    "Disaster Recovery Failure",

                "category":
                    "Infrastructure",

                "description":
                    "Recovery capabilities fail during major incidents due to inadequate preparedness.",

                "attack_vector":
                    "Infrastructure",

                "mitre_tactic":
                    "Impact"
            },

            {
                "threat_name":
                    "Business Process Disruption",

                "category":
                    "Infrastructure",

                "description":
                    "Critical business operations are interrupted because continuity controls are ineffective.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Impact"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Certificate Management",

        [

            {
                "threat_name":
                    "Certificate Spoofing",

                "category":
                    "Identity",

                "description":
                    "Attackers exploit weak certificate management to impersonate trusted systems.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Credential Access"
            },

            {
                "threat_name":
                    "Man-in-the-Middle Attack",

                "category":
                    "Network",

                "description":
                    "Weak or expired certificates enable interception of enterprise communications.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Collection"
            },

            {
                "threat_name":
                    "Certificate Trust Compromise",

                "category":
                    "Identity",

                "description":
                    "Compromised certificate trust relationships enable unauthorized communications.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Defense Evasion"
            }

        ]

    )

    register_domain_threats(

        "ITGC",

        "Change Management",

        [

            {
                "threat_name":
                    "Unauthorized Change Deployment",

                "category":
                    "Application",

                "description":
                    "Unauthorized or unapproved changes introduce security weaknesses into enterprise systems.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Persistence"
            },

            {
                "threat_name":
                    "Malicious Configuration Change",

                "category":
                    "Infrastructure",

                "description":
                    "Attackers modify configurations to weaken enterprise security controls.",

                "attack_vector":
                    "Insider",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Backdoor Introduction",

                "category":
                    "Application",

                "description":
                    "Unauthorized software changes introduce hidden backdoors into production systems.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Persistence"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Cryptographic Key Management",

        [

            {
                "threat_name":
                    "Cryptographic Key Theft",

                "category":
                    "Identity",

                "description":
                    "Attackers obtain cryptographic keys used to protect enterprise information.",

                "attack_vector":
                    "Credential",

                "mitre_tactic":
                    "Credential Access"
            },

            {
                "threat_name":
                    "Key Compromise",

                "category":
                    "Data",

                "description":
                    "Compromised cryptographic keys expose sensitive enterprise information.",

                "attack_vector":
                    "Database",

                "mitre_tactic":
                    "Credential Access"
            },

            {
                "threat_name":
                    "Unauthorized Key Usage",

                "category":
                    "Identity",

                "description":
                    "Compromised or unmanaged cryptographic keys are used for unauthorized operations.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Defense Evasion"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Endpoint Security Management",

        [

            {
                "threat_name":
                    "Endpoint Malware Infection",

                "category":
                    "Malware",

                "description":
                    "Malware infects enterprise endpoints due to weak endpoint protection controls.",

                "attack_vector":
                    "Endpoint",

                "mitre_tactic":
                    "Execution"
            },

            {
                "threat_name":
                    "Ransomware Infection",

                "category":
                    "Malware",

                "description":
                    "Enterprise endpoints are encrypted or disrupted by ransomware attacks.",

                "attack_vector":
                    "Endpoint",

                "mitre_tactic":
                    "Impact"
            },

            {
                "threat_name":
                    "Endpoint Compromise",

                "category":
                    "Infrastructure",

                "description":
                    "Attackers gain persistent control over enterprise endpoint devices.",

                "attack_vector":
                    "Endpoint",

                "mitre_tactic":
                    "Persistence"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Firewall Security Management",

        [

            {
                "threat_name":
                    "Firewall Rule Manipulation",

                "category":
                    "Network",

                "description":
                    "Firewall rules are modified to allow unauthorized network access.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Network Perimeter Bypass",

                "category":
                    "Network",

                "description":
                    "Weak firewall controls allow attackers to bypass perimeter defenses.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Initial Access"
            },

            {
                "threat_name":
                    "Unauthorized Network Exposure",

                "category":
                    "Network",

                "description":
                    "Misconfigured firewall rules expose internal enterprise services to attackers.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Discovery"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Incident Management",

        [

            {
                "threat_name":
                    "Incident Response Evasion",

                "category":
                    "Insider",

                "description":
                    "Attackers evade enterprise incident response processes to prolong unauthorized access.",

                "attack_vector":
                    "Endpoint",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Persistent Unauthorized Access",

                "category":
                    "Identity",

                "description":
                    "Delayed incident response enables attackers to maintain persistent access.",

                "attack_vector":
                    "Credential",

                "mitre_tactic":
                    "Persistence"
            },

            {
                "threat_name":
                    "Attack Escalation",

                "category":
                    "Infrastructure",

                "description":
                    "Failure to contain security incidents allows attacks to spread across enterprise systems.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Lateral Movement"
            }

        ]

    )

    register_domain_threats(

        "ITGC",

        "Logging & Monitoring",

        [

            {
                "threat_name":
                    "Log Tampering",

                "category":
                    "Infrastructure",

                "description":
                    "Attackers modify or delete security logs to conceal malicious activities.",

                "attack_vector":
                    "Endpoint",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Security Monitoring Evasion",

                "category":
                    "Infrastructure",

                "description":
                    "Malicious activities remain undetected due to ineffective security monitoring.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Unauthorized Activity Concealment",

                "category":
                    "Infrastructure",

                "description":
                    "Attackers conceal unauthorized activities by bypassing enterprise monitoring controls.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Defense Evasion"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Network Security Architecture",

        [

            {
                "threat_name":
                    "Network Reconnaissance",

                "category":
                    "Network",

                "description":
                    "Attackers gather information about enterprise network architecture before launching attacks.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Discovery"
            },

            {
                "threat_name":
                    "Infrastructure Enumeration",

                "category":
                    "Network",

                "description":
                    "Network devices, services and communication paths are enumerated by attackers.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Discovery"
            },

            {
                "threat_name":
                    "Network Architecture Exploitation",

                "category":
                    "Network",

                "description":
                    "Weak network architecture enables attackers to exploit insecure communication paths.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Initial Access"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Network Segmentation & Perimeter Security",

        [

            {
                "threat_name":
                    "Lateral Movement",

                "category":
                    "Network",

                "description":
                    "Attackers move between enterprise systems because network segmentation is ineffective.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Lateral Movement"
            },

            {
                "threat_name":
                    "Network Boundary Bypass",

                "category":
                    "Network",

                "description":
                    "Attackers bypass enterprise perimeter controls to access protected environments.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Initial Access"
            },

            {
                "threat_name":
                    "Internal Network Compromise",

                "category":
                    "Network",

                "description":
                    "Weak perimeter controls enable compromise of internal enterprise networks.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Lateral Movement"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Password Management",

        [

            {
                "threat_name":
                    "Credential Theft",

                "category":
                    "Identity",

                "description":
                    "Attackers steal enterprise user credentials to obtain unauthorized access.",

                "attack_vector":
                    "Credential",

                "mitre_tactic":
                    "Credential Access"
            },

            {
                "threat_name":
                    "Password Spraying",

                "category":
                    "Identity",

                "description":
                    "Attackers attempt commonly used passwords across multiple enterprise accounts.",

                "attack_vector":
                    "Password",

                "mitre_tactic":
                    "Credential Access"
            },

            {
                "threat_name":
                    "Brute Force Authentication Attack",

                "category":
                    "Identity",

                "description":
                    "Repeated authentication attempts are used to compromise enterprise user accounts.",

                "attack_vector":
                    "Password",

                "mitre_tactic":
                    "Credential Access"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Patch Management",

        [

            {
                "threat_name":
                    "Exploitation of Unpatched Systems",

                "category":
                    "Infrastructure",

                "description":
                    "Attackers exploit known vulnerabilities in systems that have not received security patches.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Initial Access"
            },

            {
                "threat_name":
                    "Remote Exploitation",

                "category":
                    "Infrastructure",

                "description":
                    "Unpatched enterprise systems are remotely compromised through publicly known vulnerabilities.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Execution"
            },

            {
                "threat_name":
                    "Privilege Escalation via Vulnerabilities",

                "category":
                    "Infrastructure",

                "description":
                    "Known software vulnerabilities are exploited to obtain elevated privileges.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Privilege Escalation"
            }

        ]

    )

    register_domain_threats(

        "ITGC",

        "Privileged Access Management",

        [

            {
                "threat_name":
                    "Privilege Escalation",

                "category":
                    "Identity",

                "description":
                    "Attackers obtain elevated privileges by exploiting weak privileged access controls.",

                "attack_vector":
                    "Credential",

                "mitre_tactic":
                    "Privilege Escalation"
            },

            {
                "threat_name":
                    "Privileged Account Misuse",

                "category":
                    "Insider",

                "description":
                    "Administrative accounts are intentionally or unintentionally misused to perform unauthorized activities.",

                "attack_vector":
                    "Insider",

                "mitre_tactic":
                    "Collection"
            },

            {
                "threat_name":
                    "Administrative Credential Compromise",

                "category":
                    "Identity",

                "description":
                    "Administrative credentials are compromised, allowing attackers unrestricted system access.",

                "attack_vector":
                    "Credential",

                "mitre_tactic":
                    "Credential Access"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Secure Configuration Management",

        [

            {
                "threat_name":
                    "Configuration Drift",

                "category":
                    "Infrastructure",

                "description":
                    "Systems gradually deviate from approved security baselines, increasing attack exposure.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Baseline Configuration Compromise",

                "category":
                    "Infrastructure",

                "description":
                    "Attackers exploit insecure or modified security baselines.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Privilege Escalation"
            },

            {
                "threat_name":
                    "Default Configuration Exploitation",

                "category":
                    "Infrastructure",

                "description":
                    "Default or insecure configurations provide attackers with an easy entry point.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Initial Access"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Third-Party / Vendor Management",

        [

            {
                "threat_name":
                    "Supply Chain Compromise",

                "category":
                    "Supply Chain",

                "description":
                    "Compromise of vendors or service providers introduces threats into enterprise environments.",

                "attack_vector":
                    "Third Party",

                "mitre_tactic":
                    "Initial Access"
            },

            {
                "threat_name":
                    "Third-Party Account Compromise",

                "category":
                    "Supply Chain",

                "description":
                    "Compromised vendor accounts are used to gain unauthorized enterprise access.",

                "attack_vector":
                    "Third Party",

                "mitre_tactic":
                    "Credential Access"
            },

            {
                "threat_name":
                    "Vendor Remote Access Abuse",

                "category":
                    "Supply Chain",

                "description":
                    "Remote vendor connectivity is abused to access enterprise systems.",

                "attack_vector":
                    "Third Party",

                "mitre_tactic":
                    "Lateral Movement"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "User Management",

        [

            {
                "threat_name":
                    "Unauthorized User Access",

                "category":
                    "Identity",

                "description":
                    "Improper user lifecycle management results in unauthorized access.",

                "attack_vector":
                    "Credential",

                "mitre_tactic":
                    "Initial Access"
            },

            {
                "threat_name":
                    "Dormant Account Abuse",

                "category":
                    "Identity",

                "description":
                    "Unused or orphaned user accounts are exploited by attackers.",

                "attack_vector":
                    "Credential",

                "mitre_tactic":
                    "Persistence"
            },

            {
                "threat_name":
                    "Identity Impersonation",

                "category":
                    "Identity",

                "description":
                    "Attackers impersonate legitimate enterprise users to perform unauthorized actions.",

                "attack_vector":
                    "Credential",

                "mitre_tactic":
                    "Credential Access"
            }

        ]

    )



    register_domain_threats(

        "ITGC",

        "Vulnerability Management",

        [

            {
                "threat_name":
                    "Zero-Day Exploitation",

                "category":
                    "Application",

                "description":
                    "Previously unknown software vulnerabilities are exploited before remediation is available.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Execution"
            },

            {
                "threat_name":
                    "Known Vulnerability Exploitation",

                "category":
                    "Application",

                "description":
                    "Attackers exploit publicly known vulnerabilities that remain unpatched.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Initial Access"
            },

            {
                "threat_name":
                    "Exploit Chaining",

                "category":
                    "Application",

                "description":
                    "Multiple vulnerabilities are combined to achieve deeper compromise of enterprise systems.",

                "attack_vector":
                    "Application",

                "mitre_tactic":
                    "Privilege Escalation"
            }

        ]

    )

    # ==============================================================
    # SNA
    # ==============================================================

    register_domain_threats(

        "SNA",

        "Architecture Governance & Change Management",

        [

            {
                "threat_name":
                    "Network Architecture Manipulation",

                "category":
                    "Network",

                "description":
                    "Unauthorized modifications to enterprise network architecture weaken security controls.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Defense Evasion"
            },

            {
                "threat_name":
                    "Unauthorized Infrastructure Change",

                "category":
                    "Infrastructure",

                "description":
                    "Unapproved changes introduce security weaknesses into enterprise network environments.",

                "attack_vector":
                    "Insider",

                "mitre_tactic":
                    "Persistence"
            },

            {
                "threat_name":
                    "Network Trust Exploitation",

                "category":
                    "Network",

                "description":
                    "Weak governance over network architecture enables attackers to exploit trusted communication paths.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Initial Access"
            }

        ]

    )



    register_domain_threats(

        "SNA",

        "Infrastructure Resilience & High Availability",

        [

            {
                "threat_name":
                    "Denial of Service",

                "category":
                    "Infrastructure",

                "description":
                    "Critical enterprise infrastructure becomes unavailable due to service disruption attacks.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Impact"
            },

            {
                "threat_name":
                    "Infrastructure Failure Exploitation",

                "category":
                    "Infrastructure",

                "description":
                    "Attackers exploit single points of failure in enterprise infrastructure.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Impact"
            },

            {
                "threat_name":
                    "High Availability Bypass",

                "category":
                    "Infrastructure",

                "description":
                    "Weak redundancy mechanisms enable prolonged service disruption.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Impact"
            }

        ]

    )



    register_domain_threats(

        "SNA",

        "Network Architecture & Documentation",

        [

            {
                "threat_name":
                    "Network Reconnaissance",

                "category":
                    "Network",

                "description":
                    "Attackers collect information about enterprise network topology prior to exploitation.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Discovery"
            },

            {
                "threat_name":
                    "Infrastructure Enumeration",

                "category":
                    "Network",

                "description":
                    "Enterprise network devices and communication paths are systematically identified by attackers.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Discovery"
            },

            {
                "threat_name":
                    "Topology Information Disclosure",

                "category":
                    "Network",

                "description":
                    "Unauthorized disclosure of network documentation assists adversaries during attack planning.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Collection"
            }

        ]

    )



    register_domain_threats(

        "SNA",

        "Network Segmentation & Perimeter Security",

        [

            {
                "threat_name":
                    "Lateral Movement",

                "category":
                    "Network",

                "description":
                    "Attackers move between enterprise systems because network segmentation is ineffective.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Lateral Movement"
            },

            {
                "threat_name":
                    "Perimeter Defense Bypass",

                "category":
                    "Network",

                "description":
                    "Enterprise perimeter controls are bypassed to gain unauthorized access.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Initial Access"
            },

            {
                "threat_name":
                    "East-West Network Compromise",

                "category":
                    "Network",

                "description":
                    "Weak internal segmentation enables attackers to compromise interconnected enterprise systems.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Lateral Movement"
            }

        ]

    )



    register_domain_threats(

        "SNA",

        "Secure Connectivity & Communication",

        [

            {
                "threat_name":
                    "Man-in-the-Middle Attack",

                "category":
                    "Network",

                "description":
                    "Attackers intercept enterprise communications through insecure channels.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Collection"
            },

            {
                "threat_name":
                    "Session Hijacking",

                "category":
                    "Identity",

                "description":
                    "Active communication sessions are taken over by attackers to gain unauthorized access.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Credential Access"
            },

            {
                "threat_name":
                    "Encrypted Traffic Abuse",

                "category":
                    "Network",

                "description":
                    "Attackers abuse trusted encrypted communication channels to evade security monitoring.",

                "attack_vector":
                    "Network",

                "mitre_tactic":
                    "Defense Evasion"
            }

        ]

    )

# =============================================================================
# Register All Enterprise Threats
# =============================================================================

register_all_domain_threats()

print()

print("=" * 80)

print("Registering Enterprise Threats...")

print("=" * 80)

for threats in DOMAIN_THREATS.values():

    for threat in threats:

        threat_name = threat["threat_name"]

        if threat_name in THREAT_LOOKUP:

            continue

        threat_id = generate_threat_id()

        THREAT_LOOKUP[threat_name] = threat_id

        THREAT_RECORDS.append({

            "Threat ID": threat_id,

            "Threat Name":
                threat["threat_name"],

            "Threat Category":
                threat["category"],

            "Description":
                threat["description"],

            "Attack Vector":
                threat["attack_vector"],

            "MITRE Tactic":
                threat["mitre_tactic"]

        })

print(

    f"Registered {len(THREAT_RECORDS)} unique threats."

)

# =============================================================================
# Build Threat Library
# =============================================================================

print()

print("=" * 80)

print("Creating Threat Library...")

print("=" * 80)

threat_library_df = pd.DataFrame(

    THREAT_RECORDS

)

print(

    f"Total Threats : {len(threat_library_df)}"

)


# =============================================================================
# Build Observation → Threat Mapping
# =============================================================================

print()

print("=" * 80)

print("Building Observation-Threat Mapping...")

print("=" * 80)


def select_primary_threat(observation, threats):

    """
    Select the most appropriate threat.

    Current Strategy
    ----------------
    Keyword-based matching.

    Future versions can replace this logic
    using semantic similarity or ML.
    """

    observation = str(observation).lower()

    keyword_map = {

        # ==========================================================
        # Identity
        # ==========================================================

        "password": "Credential Theft",

        "credential": "Credential Theft",

        "authentication": "Credential Theft",

        "brute": "Brute Force Authentication Attack",

        "privileged": "Privilege Escalation",

        "admin": "Administrative Credential Compromise",

        "user": "Unauthorized User Access",

        "account": "Dormant Account Abuse",

        # ==========================================================
        # Database
        # ==========================================================

        "database": "Unauthorized Database Access",

        "audit": "Audit Log Evasion",

        "sql": "SQL Injection",

        "encryption": "Database Encryption Bypass",

        "backup": "Backup Data Theft",

        # ==========================================================
        # Logging
        # ==========================================================

        "log": "Log Tampering",

        "logging": "Log Tampering",

        "siem": "Security Monitoring Evasion",

        # ==========================================================
        # Network
        # ==========================================================

        "network": "Network Reconnaissance",

        "segmentation": "Lateral Movement",

        "firewall": "Firewall Rule Manipulation",

        "vpn": "Man-in-the-Middle Attack",

        "certificate": "Certificate Spoofing",

        # ==========================================================
        # Endpoint
        # ==========================================================

        "endpoint": "Endpoint Malware Infection",

        "malware": "Endpoint Malware Infection",

        "ransomware": "Ransomware Infection",

        # ==========================================================
        # Patch
        # ==========================================================

        "patch": "Exploitation of Unpatched Systems",

        "vulnerability": "Known Vulnerability Exploitation",

        # ==========================================================
        # Vendor
        # ==========================================================

        "vendor": "Supply Chain Compromise",

        "third party": "Supply Chain Compromise",

        # ==========================================================
        # Change
        # ==========================================================

        "change": "Unauthorized Change Deployment",

        # ==========================================================
        # DFD
        # ==========================================================

        "dfd": "Unauthorized Data Flow",

        "data flow": "Data Leakage",

        "interface": "API Abuse",

        # ==========================================================
        # DFRA
        # ==========================================================

        "evidence": "Evidence Tampering",

        "forensic": "Anti-Forensics",

        "timestamp": "Timestamp Manipulation",

        "ntp": "Clock Synchronization Attack"

    }

    for keyword, threat_name in keyword_map.items():

        if keyword in observation:

            for threat in threats:

                if threat["threat_name"] == threat_name:

                    return threat

    return threats[0]


for index, row in observation_df.iterrows():

    activity = str(row["Activity"]).strip()

    domain = str(row["Domain"]).strip()

    observation = row["Observation"]

    threats = DOMAIN_THREATS.get(

        (activity, domain),

        []

    )

    if not threats:

        continue

    selected_threat = select_primary_threat(

        observation,

        threats

    )

    threat_id = THREAT_LOOKUP[

        selected_threat["threat_name"]

    ]

    OBSERVATION_THREAT_MAPPING.append({

        "Observation ID":

            f"OBS-{index+1:04d}",

        "Activity":

            activity,

        "Domain":

            domain,

        "Observation":

            observation,

        "Threat ID":

            threat_id,

        "Threat Name":

            selected_threat["threat_name"],

        "Threat Category":

            selected_threat["category"],

        "Attack Vector":

            selected_threat["attack_vector"],

        "MITRE Tactic":

            selected_threat["mitre_tactic"]

    })

print(

    f"Generated {len(OBSERVATION_THREAT_MAPPING)} mappings."

)

# =============================================================================
# Export Threat Library
# =============================================================================

observation_threat_mapping_df = pd.DataFrame(

    OBSERVATION_THREAT_MAPPING

)

threat_library_df.to_excel(

    THREAT_LIBRARY_PATH,

    index=False

)

observation_threat_mapping_df.to_excel(

    OBSERVATION_THREAT_MAPPING_PATH,

    index=False

)

print()

print("Threat Library exported successfully.")

print("Observation-Threat Mapping exported successfully.")

print()

print("=" * 80)

print("BUILD SUMMARY")

print("=" * 80)

print(f"Observations Processed : {len(observation_df)}")

print(f"Unique Threats         : {len(threat_library_df)}")

print(f"Mappings Generated     : {len(observation_threat_mapping_df)}")

print("=" * 80)