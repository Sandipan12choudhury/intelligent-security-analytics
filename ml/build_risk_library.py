import os
from collections import OrderedDict

import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_DIR = os.path.join(BASE_DIR, "dataset")

OBSERVATION_LIBRARY_PATH = os.path.join(
    DATASET_DIR,
    "observation_library.xlsx"
)

RISK_LIBRARY_PATH = os.path.join(
    DATASET_DIR,
    "risk_library.xlsx"
)

OBSERVATION_RISK_MAPPING_PATH = os.path.join(
    DATASET_DIR,
    "observation_risk_mapping.xlsx"
)

print("=" * 80)
print("Loading Observation Repository...")
print("=" * 80)

observation_df = pd.read_excel(
    OBSERVATION_LIBRARY_PATH
)

observation_df.columns = observation_df.columns.str.strip()

print(f"Loaded {len(observation_df)} observations.")

DOMAIN_RISKS = OrderedDict()

RISK_LOOKUP = {}

RISK_RECORDS = []

OBSERVATION_RISK_MAPPING = []

risk_counter = 1

def generate_risk_id():
    """
    Generates sequential Risk IDs.

    Example

    RISK-0001
    RISK-0002
    """

    global risk_counter

    risk_id = f"RISK-{risk_counter:04d}"

    risk_counter += 1

    return risk_id

def register_domain_risks(
    activity,
    domain,
    risks
):
    """
    Registers all risks belonging to a domain.
    """

    DOMAIN_RISKS[(activity, domain)] = risks

def register_all_domain_risks():
    """
    Registers enterprise security risks.

    The registration order MUST follow
    observation_library.xlsx exactly.
    """

    # ======================================================================
    # DFA / DFD
    # ======================================================================

    
    
    

    register_domain_risks(

        "DFA / DFD",

        "DFD Governance & Change Management",

        [

            {
                "risk_name": "Inadequate Data Flow Governance Risk",
                "description":
                    "Weak governance over data flow documentation may "
                    "result in undocumented data movement and security gaps.",
                "risk_category": "Governance"
            },

            {
                "risk_name": "Unauthorized Data Flow Change Risk",
                "description":
                    "Uncontrolled modifications to data flows may introduce "
                    "security vulnerabilities or compliance issues.",
                "risk_category": "Integrity"
            }

        ]

    )



    register_domain_risks(

        "DFA / DFD",

        "Data Flow Documentation & Completeness",

        [

            {
                "risk_name": "Incomplete Data Flow Visibility Risk",
                "description":
                    "Incomplete or outdated documentation may prevent "
                    "identification of security weaknesses.",
                "risk_category": "Governance"
            },

            {
                "risk_name": "Undocumented Data Movement Risk",
                "description":
                    "Undocumented movement of enterprise data may "
                    "lead to uncontrolled exposure.",
                "risk_category": "Confidentiality"
            }

        ]

    )



    register_domain_risks(

        "DFA / DFD",

        "Interface & Integration Security",

        [

            {
                "risk_name": "Insecure System Integration Risk",
                "description":
                    "Weakly secured interfaces may expose enterprise "
                    "systems to unauthorized access.",
                "risk_category": "Confidentiality"
            },

            {
                "risk_name": "Data Exchange Integrity Risk",
                "description":
                    "Improper interface controls may compromise "
                    "accuracy and integrity of exchanged information.",
                "risk_category": "Integrity"
            }

        ]

    )



    register_domain_risks(

        "DFA / DFD",

        "Sensitive Data Flow Protection",

        [

            {
                "risk_name": "Sensitive Data Exposure Risk",
                "description":
                    "Sensitive information may be disclosed through "
                    "unprotected data flows.",
                "risk_category": "Confidentiality"
            },

            {
                "risk_name": "Sensitive Data Leakage Risk",
                "description":
                    "Insufficient protection mechanisms may allow "
                    "unauthorized disclosure of confidential information.",
                "risk_category": "Confidentiality"
            }

        ]

    )



    register_domain_risks(

        "DFA / DFD",

        "Trust Boundaries & Data Flow Security",

        [

            {
                "risk_name": "Trust Boundary Violation Risk",
                "description":
                    "Weak enforcement of trust boundaries may permit "
                    "unauthorized interaction between security zones.",
                "risk_category": "Integrity"
            },

            {
                "risk_name": "Cross-Boundary Data Exposure Risk",
                "description":
                    "Improper protection across trust boundaries may "
                    "result in unintended data disclosure.",
                "risk_category": "Confidentiality"
            }

        ]

    )

        # ======================================================================
    # DFRA
    # ======================================================================

    register_domain_risks(

        "DFRA",

        "Digital Evidence Management",

        [

            {
                "risk_name": "Loss of Digital Evidence Risk",
                "description":
                    "Improper management of digital evidence may prevent "
                    "successful forensic investigations.",
                "risk_category": "Forensics"
            },

            {
                "risk_name": "Evidence Tampering Risk",
                "description":
                    "Weak protection of digital evidence may compromise "
                    "its authenticity and admissibility.",
                "risk_category": "Integrity"
            }

        ]

    )



    register_domain_risks(

        "DFRA",

        "Evidence Logging & Event Capture",

        [

            {
                "risk_name": "Insufficient Audit Trail Risk",
                "description":
                    "Incomplete event logging may prevent identification "
                    "of malicious activities.",
                "risk_category": "Monitoring"
            },

            {
                "risk_name": "Security Event Visibility Risk",
                "description":
                    "Failure to capture security events may delay "
                    "incident detection and response.",
                "risk_category": "Detection"
            }

        ]

    )



    register_domain_risks(

        "DFRA",

        "Forensic Investigation Readiness",

        [

            {
                "risk_name": "Forensic Readiness Risk",
                "description":
                    "Lack of forensic preparedness may hinder security "
                    "investigations after an incident.",
                "risk_category": "Forensics"
            },

            {
                "risk_name": "Incident Investigation Delay Risk",
                "description":
                    "Poor forensic readiness may delay identification "
                    "of root causes.",
                "risk_category": "Response"
            }

        ]

    )



    register_domain_risks(

        "DFRA",

        "Log Retention & Preservation",

        [

            {
                "risk_name": "Loss of Audit Records Risk",
                "description":
                    "Improper retention of security logs may prevent "
                    "investigation of historical incidents.",
                "risk_category": "Monitoring"
            },

            {
                "risk_name": "Regulatory Non-Compliance Risk",
                "description":
                    "Failure to preserve logs may violate regulatory "
                    "retention requirements.",
                "risk_category": "Compliance"
            }

        ]

    )



    register_domain_risks(

        "DFRA",

        "Time Synchronization & Log Integrity",

        [

            {
                "risk_name": "Log Integrity Risk",
                "description":
                    "Unsynchronized systems may compromise log accuracy "
                    "and event correlation.",
                "risk_category": "Integrity"
            },

            {
                "risk_name": "Event Correlation Failure Risk",
                "description":
                    "Inconsistent timestamps may affect forensic "
                    "investigations and monitoring.",
                "risk_category": "Monitoring"
            }

        ]

    )



    # ======================================================================
    # DATABASE
    # ======================================================================

    register_domain_risks(

        "Database",

        "Database Auditing & Monitoring",

        [

            {
                "risk_name": "Unauthorized Database Activity Risk",
                "description":
                    "Insufficient auditing may allow unauthorized "
                    "database activities to remain undetected.",
                "risk_category": "Monitoring"
            },

            {
                "risk_name": "Database Monitoring Failure Risk",
                "description":
                    "Lack of monitoring may delay detection of "
                    "security incidents affecting databases.",
                "risk_category": "Detection"
            }

        ]

    )



    register_domain_risks(

        "Database",

        "Database Backup, Recovery & Availability",

        [

            {
                "risk_name": "Database Data Loss Risk",
                "description":
                    "Failure of backup or recovery controls may "
                    "result in permanent loss of enterprise data.",
                "risk_category": "Availability"
            },

            {
                "risk_name": "Database Service Disruption Risk",
                "description":
                    "Inadequate recovery capability may lead to "
                    "extended database outages.",
                "risk_category": "Availability"
            }

        ]

    )



    register_domain_risks(

        "Database",

        "Database Configuration & Hardening",

        [

            {
                "risk_name": "Database Misconfiguration Risk",
                "description":
                    "Weak configuration settings may expose databases "
                    "to security attacks.",
                "risk_category": "Configuration"
            },

            {
                "risk_name": "Database Exploitation Risk",
                "description":
                    "Improper hardening increases the likelihood of "
                    "successful attacks.",
                "risk_category": "Integrity"
            }

        ]

    )



    register_domain_risks(

        "Database",

        "Database Encryption & Data Protection",

        [

            {
                "risk_name": "Sensitive Database Disclosure Risk",
                "description":
                    "Failure to encrypt sensitive data may lead to "
                    "unauthorized disclosure.",
                "risk_category": "Confidentiality"
            },

            {
                "risk_name": "Database Encryption Failure Risk",
                "description":
                    "Weak encryption controls may expose critical "
                    "business information.",
                "risk_category": "Confidentiality"
            }

        ]

    )



    register_domain_risks(

        "Database",

        "Database User & Access Management",

        [

            {
                "risk_name": "Unauthorized Database Access Risk",
                "description":
                    "Improper user management may allow unauthorized "
                    "access to enterprise databases.",
                "risk_category": "Access Control"
            },

            {
                "risk_name": "Excessive Database Privilege Risk",
                "description":
                    "Excessive privileges may enable unauthorized "
                    "database modifications.",
                "risk_category": "Access Control"
            }

        ]

    )

        # ======================================================================
    # ITGC
    # ======================================================================

    register_domain_risks(

        "ITGC",

        "Application Security Management",

        [

            {
                "risk_name": "Application Security Compromise Risk",
                "description":
                    "Weak application security controls may expose "
                    "business applications to cyber attacks.",
                "risk_category": "Application Security"
            },

            {
                "risk_name": "Unauthorized Access Risk",
                "description":
                    "Weak security controls may allow unauthorized "
                    "access to enterprise systems.",
                "risk_category": "Access Control"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Asset Management",

        [

            {
                "risk_name": "Asset Visibility Risk",
                "description":
                    "Incomplete asset inventories may prevent effective "
                    "security governance and risk management.",
                "risk_category": "Asset Management"
            },

            {
                "risk_name": "Unauthorized Asset Risk",
                "description":
                    "Unmanaged or unknown assets may introduce "
                    "security vulnerabilities.",
                "risk_category": "Asset Management"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Backup & Restoration",

        [

            {
                "risk_name": "Data Loss Risk",
                "description":
                    "Failure of backup and restoration controls may "
                    "lead to permanent loss of enterprise information.",
                "risk_category": "Availability"
            },

            {
                "risk_name": "Service Availability Risk",
                "description":
                    "Unsuccessful restoration may impact business "
                    "continuity and service availability.",
                "risk_category": "Availability"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Business Continuity & Disaster Recovery",

        [

            {
                "risk_name": "Business Continuity Failure Risk",
                "description":
                    "Inadequate continuity planning may interrupt "
                    "critical business operations.",
                "risk_category": "Availability"
            },

            {
                "risk_name": "Disaster Recovery Failure Risk",
                "description":
                    "Failure to recover critical services following "
                    "major incidents may impact business resilience.",
                "risk_category": "Availability"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Certificate Management",

        [

            {
                "risk_name": "Certificate Trust Failure Risk",
                "description":
                    "Expired or improperly managed certificates may "
                    "compromise secure communications.",
                "risk_category": "Cryptography"
            },

            {
                "risk_name": "Secure Communication Risk",
                "description":
                    "Invalid certificates may weaken encrypted "
                    "communications between systems.",
                "risk_category": "Confidentiality"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Change Management",

        [

            {
                "risk_name": "Unauthorized Change Risk",
                "description":
                    "Uncontrolled changes may introduce security "
                    "vulnerabilities into production systems.",
                "risk_category": "Change Management"
            },

            {
                "risk_name": "Configuration Drift Risk",
                "description":
                    "Improper change governance may lead to "
                    "unauthorized configuration deviations.",
                "risk_category": "Configuration"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Cryptographic Key Management",

        [

            {
                "risk_name": "Cryptographic Key Exposure Risk",
                "description":
                    "Improper key management may compromise encrypted "
                    "enterprise information.",
                "risk_category": "Cryptography"
            },

            {
                "risk_name": "Data Confidentiality Risk",
                "description":
                    "Weak cryptographic controls may expose "
                    "confidential business information.",
                "risk_category": "Confidentiality"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Endpoint Security Management",

        [

            {
                "risk_name": "Endpoint Compromise Risk",
                "description":
                    "Insufficient endpoint protection may expose "
                    "enterprise devices to malware attacks.",
                "risk_category": "Endpoint Security"
            },

            {
                "risk_name": "Malware Infection Risk",
                "description":
                    "Weak endpoint controls increase the likelihood "
                    "of malware infections.",
                "risk_category": "Malware"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Firewall Security Management",

        [

            {
                "risk_name": "Network Intrusion Risk",
                "description":
                    "Weak firewall controls may allow unauthorized "
                    "network access.",
                "risk_category": "Network Security"
            },

            {
                "risk_name": "Unauthorized Access Risk",
                "description":
                    "Improper firewall configurations may expose "
                    "internal systems.",
                "risk_category": "Access Control"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Incident Management",

        [

            {
                "risk_name": "Incident Response Failure Risk",
                "description":
                    "Ineffective incident management may increase "
                    "the impact of security incidents.",
                "risk_category": "Incident Response"
            },

            {
                "risk_name": "Delayed Incident Detection Risk",
                "description":
                    "Slow detection and response may increase "
                    "business impact.",
                "risk_category": "Monitoring"
            }

        ]

    )

    register_domain_risks(

        "ITGC",

        "Logging & Monitoring",

        [

            {
                "risk_name": "Insufficient Audit Trail Risk",
                "description":
                    "Incomplete logging may prevent timely detection "
                    "and investigation of security incidents.",
                "risk_category": "Monitoring"
            },

            {
                "risk_name": "Delayed Incident Detection Risk",
                "description":
                    "Failure to continuously monitor security events "
                    "may increase incident impact.",
                "risk_category": "Monitoring"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Network Security Architecture",

        [

            {
                "risk_name": "Network Architecture Weakness Risk",
                "description":
                    "Weak network architecture may expose enterprise "
                    "systems to cyber threats.",
                "risk_category": "Network Security"
            },

            {
                "risk_name": "Unauthorized Access Risk",
                "description":
                    "Improper network security architecture may allow "
                    "unauthorized network access.",
                "risk_category": "Access Control"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Network Segmentation & Perimeter Security",

        [

            {
                "risk_name": "Network Segmentation Failure Risk",
                "description":
                    "Weak segmentation may enable lateral movement "
                    "between enterprise systems.",
                "risk_category": "Network Security"
            },

            {
                "risk_name": "Perimeter Defense Failure Risk",
                "description":
                    "Improper perimeter controls may expose internal "
                    "networks to external attacks.",
                "risk_category": "Network Security"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Password Management",

        [

            {
                "risk_name": "Weak Authentication Risk",
                "description":
                    "Weak password controls may increase the likelihood "
                    "of unauthorized account compromise.",
                "risk_category": "Authentication"
            },

            {
                "risk_name": "Credential Compromise Risk",
                "description":
                    "Poor password management may expose user "
                    "credentials to attackers.",
                "risk_category": "Authentication"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Patch Management",

        [

            {
                "risk_name": "Unpatched Vulnerability Risk",
                "description":
                    "Delayed security patching may expose enterprise "
                    "systems to known exploits.",
                "risk_category": "Vulnerability Management"
            },

            {
                "risk_name": "System Exploitation Risk",
                "description":
                    "Failure to remediate security patches may allow "
                    "successful cyber attacks.",
                "risk_category": "Vulnerability Management"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Privileged Access Management",

        [

            {
                "risk_name": "Privileged Access Abuse Risk",
                "description":
                    "Improper management of privileged accounts may "
                    "result in unauthorized administrative activities.",
                "risk_category": "Access Control"
            },

            {
                "risk_name": "Unauthorized Access Risk",
                "description":
                    "Weak privileged access controls may permit "
                    "unauthorized administrative access.",
                "risk_category": "Access Control"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Secure Configuration Management",

        [

            {
                "risk_name": "Configuration Drift Risk",
                "description":
                    "Deviation from approved secure baselines may "
                    "introduce security weaknesses.",
                "risk_category": "Configuration"
            },

            {
                "risk_name": "System Misconfiguration Risk",
                "description":
                    "Improper security configurations may expose "
                    "enterprise systems to attacks.",
                "risk_category": "Configuration"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Third-Party / Vendor Management",

        [

            {
                "risk_name": "Third-Party Security Risk",
                "description":
                    "Weak vendor security governance may expose "
                    "enterprise systems through external parties.",
                "risk_category": "Third-Party"
            },

            {
                "risk_name": "Supply Chain Risk",
                "description":
                    "Compromise of third-party services may impact "
                    "enterprise security and operations.",
                "risk_category": "Third-Party"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "User Management",

        [

            {
                "risk_name": "Unauthorized Access Risk",
                "description":
                    "Improper user account management may permit "
                    "unauthorized access to enterprise resources.",
                "risk_category": "Access Control"
            },

            {
                "risk_name": "Orphan Account Risk",
                "description":
                    "Unused or unmanaged accounts may be exploited "
                    "by malicious users.",
                "risk_category": "Identity Management"
            }

        ]

    )



    register_domain_risks(

        "ITGC",

        "Vulnerability Management",

        [

            {
                "risk_name": "Unpatched Vulnerability Risk",
                "description":
                    "Failure to identify and remediate vulnerabilities "
                    "may expose systems to cyber attacks.",
                "risk_category": "Vulnerability Management"
            },

            {
                "risk_name": "System Exploitation Risk",
                "description":
                    "Known vulnerabilities may be exploited by "
                    "threat actors if left unresolved.",
                "risk_category": "Vulnerability Management"
            }

        ]

    )

        # ======================================================================
    # SNA
    # ======================================================================

    register_domain_risks(

        "SNA",

        "Architecture Governance & Change Management",

        [

            {
                "risk_name": "Network Architecture Governance Risk",
                "description":
                    "Weak governance over enterprise network architecture "
                    "may introduce security weaknesses and unmanaged changes.",
                "risk_category": "Architecture Governance"
            },

            {
                "risk_name": "Unauthorized Change Risk",
                "description":
                    "Unapproved architecture changes may compromise "
                    "network security and operational stability.",
                "risk_category": "Change Management"
            }

        ]

    )



    register_domain_risks(

        "SNA",

        "Infrastructure Resilience & High Availability",

        [

            {
                "risk_name": "Service Availability Risk",
                "description":
                    "Failure to implement resilient infrastructure may "
                    "cause prolonged service disruption.",
                "risk_category": "Availability"
            },

            {
                "risk_name": "Infrastructure Failure Risk",
                "description":
                    "Insufficient redundancy may increase the likelihood "
                    "of critical infrastructure failures.",
                "risk_category": "Availability"
            }

        ]

    )



    register_domain_risks(

        "SNA",

        "Network Architecture & Documentation",

        [

            {
                "risk_name": "Incomplete Network Documentation Risk",
                "description":
                    "Outdated or incomplete network documentation may "
                    "affect security operations and troubleshooting.",
                "risk_category": "Documentation"
            },

            {
                "risk_name": "Network Architecture Weakness Risk",
                "description":
                    "Poorly documented architecture may increase "
                    "security exposure and operational risk.",
                "risk_category": "Architecture Governance"
            }

        ]

    )



    register_domain_risks(

        "SNA",

        "Network Segmentation & Perimeter Security",

        [

            {
                "risk_name": "Network Segmentation Failure Risk",
                "description":
                    "Weak segmentation controls may enable lateral "
                    "movement across enterprise networks.",
                "risk_category": "Network Security"
            },

            {
                "risk_name": "Perimeter Defense Failure Risk",
                "description":
                    "Weak perimeter protection may expose internal "
                    "systems to external threats.",
                "risk_category": "Network Security"
            }

        ]

    )



    register_domain_risks(

        "SNA",

        "Secure Connectivity & Communication",

        [

            {
                "risk_name": "Secure Communication Risk",
                "description":
                    "Weak communication security may expose enterprise "
                    "information during transmission.",
                "risk_category": "Communication Security"
            },

            {
                "risk_name": "Data Interception Risk",
                "description":
                    "Insecure communication channels may allow "
                    "unauthorized interception of enterprise data.",
                "risk_category": "Confidentiality"
            }

        ]

    )

# =============================================================================
# Register All Risks
# =============================================================================

register_all_domain_risks()

print()
print("=" * 80)
print("Registering Enterprise Risks...")
print("=" * 80)

for risks in DOMAIN_RISKS.values():

    for risk in risks:

        risk_name = risk["risk_name"]

        if risk_name in RISK_LOOKUP:
            continue

        risk_id = generate_risk_id()

        RISK_LOOKUP[risk_name] = risk_id

        RISK_RECORDS.append({

            "Risk ID": risk_id,

            "Risk Name": risk_name,

            "Description": risk["description"],

            "Risk Category": risk["risk_category"]

        })

print(f"Registered {len(RISK_RECORDS)} unique risks.")

# =============================================================================
# Build Risk Library
# =============================================================================

print()
print("=" * 80)
print("Creating Risk Library...")
print("=" * 80)

risk_library_df = pd.DataFrame(RISK_RECORDS)

print(f"Total Risks : {len(risk_library_df)}")

# =============================================================================
# Build Observation → Primary Risk Mapping
# =============================================================================

print()
print("=" * 80)
print("Building Observation-Risk Mapping...")
print("=" * 80)


def select_primary_risk(observation, risks):
    """
    Selects the most appropriate enterprise risk.

    Current Strategy
    ----------------
    Keyword matching.

    Future versions may use semantic search
    or ML without changing dataset structure.
    """

    observation = str(observation).lower()

    keyword_map = {

        "password": "Weak Authentication Risk",

        "backup": "Data Loss Risk",

        "restore": "Service Availability Risk",

        "asset": "Asset Visibility Risk",

        "certificate": "Certificate Trust Failure Risk",

        "firewall": "Network Intrusion Risk",

        "incident": "Incident Response Failure Risk",

        "log": "Insufficient Audit Trail Risk",

        "audit": "Unauthorized Database Activity Risk",

        "database": "Unauthorized Database Access Risk",

        "patch": "Unpatched Vulnerability Risk",

        "vulnerability": "System Exploitation Risk",

        "privileged": "Privileged Access Abuse Risk",

        "account": "Unauthorized Access Risk",

        "vendor": "Third-Party Security Risk",

        "third party": "Third-Party Security Risk",

        "network": "Network Architecture Weakness Risk",

        "encryption": "Sensitive Database Disclosure Risk",

        "key": "Cryptographic Key Exposure Risk",

        "endpoint": "Endpoint Compromise Risk",

        "dfd": "Inadequate Data Flow Governance Risk",

        "data flow": "Undocumented Data Movement Risk",

        "evidence": "Loss of Digital Evidence Risk",

        "forensic": "Forensic Readiness Risk"

    }

    for keyword, risk_name in keyword_map.items():

        if keyword in observation:

            for risk in risks:

                if risk["risk_name"] == risk_name:

                    return risk

    if risks:
        return risks[0]

    return None

for index, row in observation_df.iterrows():

    activity = str(row["Activity"]).strip()

    domain = str(row["Domain"]).strip()

    observation = row["Observation"]

    risks = DOMAIN_RISKS.get((activity, domain), [])

    selected_risk = select_primary_risk(
        observation,
        risks
    )

    if selected_risk is None:
        continue

    risk_name = selected_risk["risk_name"]

    risk_id = RISK_LOOKUP[risk_name]

    OBSERVATION_RISK_MAPPING.append({

        "Observation ID": f"OBS-{index + 1:04d}",

        "Activity": activity,

        "Domain": domain,

        "Observation": observation,

        "Risk ID": risk_id,

        "Risk Name": risk_name,

        "Risk Category": selected_risk["risk_category"]

    })

print(
    f"Generated {len(OBSERVATION_RISK_MAPPING)} mappings."
)

# =============================================================================
# Export Datasets
# =============================================================================

observation_risk_mapping_df = pd.DataFrame(
    OBSERVATION_RISK_MAPPING
)

risk_library_df.to_excel(
    RISK_LIBRARY_PATH,
    index=False
)

observation_risk_mapping_df.to_excel(
    OBSERVATION_RISK_MAPPING_PATH,
    index=False
)

print("\nRisk Library exported successfully.")
print("Observation-Risk Mapping exported successfully.")

print()
print("=" * 80)
print("BUILD SUMMARY")
print("=" * 80)
print(f"Observations Processed : {len(observation_df)}")
print(f"Unique Risks           : {len(risk_library_df)}")
print(f"Mappings Generated     : {len(observation_risk_mapping_df)}")
print("=" * 80)