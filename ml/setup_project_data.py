import pandas as pd
from pathlib import Path

# ============================================================
# Create Required Project Directories
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "dataset"
DATASET_DIR.mkdir(exist_ok=True)

# ============================================================
# Application Master Inventory
# ============================================================

applications = [

    # IT-Treasury Support Services
    ["Mercury FX", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["Murex", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["E-Forex", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["IDEA LRS TCS", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["CXLPM", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["IRM", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["CSGL", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["GMU", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["Khatabook", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["Mastercard SMS", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["NRM", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["NDTL", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["ITRP", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["CMM", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["NICE NTR", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["IPC", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["Cheque Collection", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["Datametrics Dashboard Application", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["FX-Out", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["Branch Portal", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["Rupee Express", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["Gulf to Nepal", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["Rupee Flash", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["NRI DMS", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["India to Nepal", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["PMS & CS", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],
    ["IRC", "IT-Treasury Support Services", "Y", "Y", "Y", "Y", "Y"],

    # Trade Finance
    ["CE", "Trade Finance", "Y", "Y", "Y", "Y", "Y"],
    ["EE", "Trade Finance", "Y", "Y", "Y", "Y", "Y"],
    ["SCF Revamp", "Trade Finance", "Y", "Y", "Y", "Y", "Y"],

    # Regulatory
    ["AMLOCK OTSS", "IT-Regulatory Applications", "Y", "Y", "Y", "Y", "Y"],
    ["AMLOCK TFSS", "IT-Regulatory Applications", "Y", "Y", "Y", "Y", "Y"],
    ["AMLOCK RMS", "IT-Regulatory Applications", "Y", "Y", "Y", "Y", "Y"],
    ["AMLOCK ESS", "IT-Regulatory Applications", "Y", "Y", "Y", "Y", "Y"],
    ["IAP SP&AW", "IT-Regulatory Applications", "Y", "Y", "Y", "Y", "Y"],
    ["CSIG", "IT-Regulatory Applications", "Y", "Y", "Y", "Y", "Y"],

    # Cloud Solutions
    ["Microsoft Azure", "Cloud Solutions", "Y", "N", "Y", "Y", "Y"],
    ["NetApp Storage", "Cloud Solutions", "Y", "N", "Y", "Y", "Y"],
    ["VMWare Virtualization", "Cloud Solutions", "Y", "N", "Y", "Y", "Y"],
    ["EBS Commvault", "Cloud Solutions", "Y", "Y", "Y", "Y", "Y"],

    # Network Technology
    ["DNS", "Network Technology", "Y", "N", "Y", "Y", "Y"],
    ["NTP", "Network Technology", "Y", "N", "Y", "Y", "Y"],
    ["NSPM", "Network Technology", "Y", "N", "Y", "Y", "Y"],
    ["Proxy", "Network Technology", "Y", "N", "Y", "Y", "Y"],
    ["NAC", "Network Technology", "Y", "N", "Y", "Y", "Y"],
    ["SB-Connect", "Network Technology", "Y", "N", "Y", "Y", "Y"],

    # NG Data Warehouse
    ["CP4D", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["RTC", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["CDC", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["CP4I", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["Cognos", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["DAS", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["ESS", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["ETL", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["IIAS", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["Portal", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["Query Surge", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["SCAPM", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["SFG", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["SKLM", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["TSM", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"],
    ["TWS", "NG-Data Warehouse", "Y", "Y", "Y", "Y", "Y"]
]

app_df = pd.DataFrame(
    applications,
    columns=[
        "Application_Name",
        "Department",
        "ITGC",
        "DB",
        "DFRA",
        "DFA",
        "SNA"
    ]
)

assert len(app_df) == 62, "Application count mismatch!"

# ============================================================
# Domain Master
# ============================================================

domains = [
# ============================================================
# ITGC
# ============================================================

["ITGC", "User Management"],
["ITGC", "Privileged Access Management"],
["ITGC", "Password Management"],
["ITGC", "Role & Access Governance"],
["ITGC", "Segregation of Duties"],
["ITGC", "Authentication & MFA"],
["ITGC", "Logging & Monitoring"],
["ITGC", "Security Incident Management"],
["ITGC", "Backup Management"],
["ITGC", "Restoration Management"],
["ITGC", "Business Continuity Management"],
["ITGC", "Disaster Recovery Management"],
["ITGC", "Change Management"],
["ITGC", "Release & Deployment Management"],
["ITGC", "Patch Management"],
["ITGC", "Vulnerability Management"],
["ITGC", "Asset Management"],
["ITGC", "Configuration Management"],
["ITGC", "Capacity Management"],
["ITGC", "Third Party Management"],
["ITGC", "Vendor Risk Management"],
["ITGC", "Secure SDLC"],
["ITGC", "Application Security Governance"],
["ITGC", "Cloud Security Governance"],
["ITGC", "Data Retention & Archival"],
["ITGC", "Security Policy Compliance"],
["ITGC", "Audit & Regulatory Compliance"],

# ============================================================
# DB
# ============================================================

["DB", "Database Access Management"],
["DB", "Privileged Database Access"],
["DB", "Database Account Management"],
["DB", "Database Authentication"],
["DB", "Database Authorization"],
["DB", "Database Auditing"],
["DB", "DAM Monitoring"],
["DB", "Database Hardening"],
["DB", "Database Configuration Security"],
["DB", "Database Patch Management"],
["DB", "Database Vulnerability Management"],
["DB", "Database Backup Management"],
["DB", "Database Recovery Management"],
["DB", "Database Encryption"],
["DB", "Database Key Management"],
["DB", "Database Link Security"],
["DB", "Database Job & Scheduler Security"],
["DB", "Database Logging & Monitoring"],
["DB", "Database Compliance Management"],

# ============================================================
# DFRA
# ============================================================

["DFRA", "Audit Trail Management"],
["DFRA", "Log Collection"],
["DFRA", "Log Correlation"],
["DFRA", "Log Retention"],
["DFRA", "Log Integrity"],
["DFRA", "Time Synchronization"],
["DFRA", "Security Event Monitoring"],
["DFRA", "SIEM Integration"],
["DFRA", "Forensic Readiness"],
["DFRA", "Evidence Preservation"],
["DFRA", "Incident Investigation Support"],
["DFRA", "User Activity Monitoring"],
["DFRA", "Privileged Activity Monitoring"],
["DFRA", "Compliance Logging"],

# ============================================================
# DFA
# ============================================================

["DFA", "Data Classification"],
["DFA", "Sensitive Data Identification"],
["DFA", "Data Flow Validation"],
["DFA", "Data Segregation"],
["DFA", "Trust Boundary Analysis"],
["DFA", "Data Encryption In Transit"],
["DFA", "Data Encryption At Rest"],
["DFA", "Third Party Data Exchange"],
["DFA", "API Data Security"],
["DFA", "Data Minimization"],
["DFA", "Data Leakage Prevention"],
["DFA", "Data Retention & Disposal"],
["DFA", "Cross Border Data Transfer"],
["DFA", "Data Integrity Validation"],

# ============================================================
# SNA
# ============================================================

["SNA", "Network Architecture Security"],
["SNA", "Network Segmentation"],
["SNA", "Firewall Security"],
["SNA", "IDS/IPS Monitoring"],
["SNA", "Secure Connectivity"],
["SNA", "Remote Access Security"],
["SNA", "Administrative Access Security"],
["SNA", "Network Traffic Monitoring"],
["SNA", "Network Hardening"],
["SNA", "DMZ Security"],
["SNA", "Load Balancer Security"],
["SNA", "DNS Security"],
["SNA", "NTP Security"],
["SNA", "Proxy Security"],
["SNA", "NAC Security"],
["SNA", "VPN Security"],
["SNA", "High Availability & Redundancy"],
["SNA", "Network Device Management"],
["SNA", "Network Logging & Monitoring"],
["SNA", "East-West Traffic Security"]

]


domain_df = pd.DataFrame(
    domains,
    columns=["Activity", "Domain"]
)
assert len(domain_df) == 94, "Domain count mismatch!"

print(f"Total Applications : {len(app_df)}")
print(f"Total Domains      : {len(domain_df)}")

print("\nDomain Distribution")
print(domain_df.groupby("Activity").size())

print("\nApplication Distribution")
print(app_df["Department"].value_counts())

# ============================================================
# Observation Dataset Skeleton
# ============================================================

observation_df = pd.DataFrame(
    columns=[
        "Observation_ID",
        "Application_Name",
        "Department",
        "Activity",
        "Domain",
        "Observation",
        "Severity",
        "Status"
    ]
)

# ============================================================
# Save Files
# ============================================================

app_df.to_excel(
    DATASET_DIR / "application_master_inventory.xlsx",
    index=False
)

domain_df.to_excel(
    DATASET_DIR / "domain_master.xlsx",
    index=False
)

observation_df.to_excel(
    DATASET_DIR / "master_observation_dataset.xlsx",
    index=False
)

print("All project datasets created successfully.")