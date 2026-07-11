"""
===========================================================================
Application Master Builder

Purpose
-------
Builds the Enterprise Application Master Repository.

Output
------
application_master.xlsx

This repository serves as the master inventory of enterprise applications
used throughout the Intelligent Security Analytics Platform.

All subsequent datasets reference Application ID from this repository.

Author:
Sandipan Choudhury

===========================================================================
"""

import os
import pandas as pd
from pathlib import Path


# =============================================================================
# Project Paths
# =============================================================================

CURRENT_FILE = Path(__file__).resolve()

PROJECT_ROOT = CURRENT_FILE.parent.parent

DATASET_DIR = PROJECT_ROOT / "dataset"

APPLICATION_MASTER_PATH = (
    DATASET_DIR / "application_master.xlsx"
)

os.makedirs(DATASET_DIR, exist_ok=True)

# =============================================================================
# Master Containers
# =============================================================================

APPLICATION_RECORDS = []

APPLICATION_LOOKUP = {}

APPLICATION_COUNTER = 1

# =============================================================================
# Application ID Generator
# =============================================================================

def generate_application_id():
    """
    Generates Application IDs.

    Format
    ------
    APP-0001
    APP-0002
    ...
    """

    global APPLICATION_COUNTER

    application_id = (
        f"APP-{APPLICATION_COUNTER:04d}"
    )

    APPLICATION_COUNTER += 1

    return application_id

# =============================================================================
# Register Enterprise Applications
# =============================================================================

def register_application(
    application_name,
    department,
    application_type,
    technology_domain,
    business_criticality,
    environment,
    status
):
    """
    Registers one enterprise application.
    """

    APPLICATION_RECORDS.append({

        "Application Name":
            application_name,

        "Department":
            department,

        "Application Type":
            application_type,

        "Technology Domain":
            technology_domain,

        "Business Criticality":
            business_criticality,

        "Environment":
            environment,

        "Status":
            status

    })

print("=" * 80)
print("Registering Enterprise Applications...")
print("=" * 80)

# =============================================================================
# Register All Enterprise Applications
# =============================================================================

def register_all_enterprise_applications():

    """
    Registers all enterprise applications.

    Registration order follows the
    enterprise application inventory.

    Every application is assigned
    deterministic metadata.
    """

    # ==============================================================
    # IT-Treasure Support Services
    # ==============================================================

    treasury_apps = [

        "Mercury FX",
        "Murex",
        "E-Forex",
        "IDEA LRS TCS",
        "CXLPM",
        "IRM",
        "CSGL",
        "GMU",
        "Khatabook",
        "Mastercard SMS",
        "NRM",
        "NDTL",
        "ITRP",
        "CMM",
        "NICE NTR",
        "IPC",
        "Cheque Collection",
        "Datametrics Dashboard Application",
        "FX-Out",
        "Branch Portal",
        "Rupee Express",
        "Gulf to Nepal",
        "Rupee Flash",
        "NRI DMS",
        "India to Nepal",
        "PMS & CS",
        "IRC"

    ]

    for app in treasury_apps:

        register_application(

            application_name=app,

            department="IT-Treasure Support Services",

            application_type="Business Application",

            technology_domain="Treasury Support Services",

            business_criticality="Critical",

            environment="Production",

            status="Active"

        )
    # ==============================================================
    # Trade Finance
    # ==============================================================

    trade_finance_apps = [

        "CE",
        "EE",
        "SCF Revamp"

    ]

    for app in trade_finance_apps:

        register_application(

            application_name=app,

            department="Trade Finance",

            application_type="Business Application",

            technology_domain="Trade Finance",

            business_criticality="Critical",

            environment="Production",

            status="Active"

        )

    # ==============================================================
    # IT-Regulatory Applications
    # ==============================================================

    regulatory_apps = [

        "AMLOCK OTSS",
        "AMLOCK TFSS",
        "AMLOCK RMS",
        "AMLOCK ESS",
        "IAP SP&AW",
        "CSIG"

    ]

    for app in regulatory_apps:

        register_application(

            application_name=app,

            department="IT-Regulatory Applications",

            application_type="Business Application",

            technology_domain="Regulatory",

            business_criticality="High",

            environment="Production",

            status="Active"

        )

    # ==============================================================
    # Cloud Solutions
    # ==============================================================

    cloud_apps = [

        "Microsoft Azure",
        "NetApp Storage",
        "VMWare Virtualization",
        "EBS Commvault"

    ]

    for app in cloud_apps:

        register_application(

            application_name=app,

            department="Cloud Solutions",

            application_type="Infrastructure Service",

            technology_domain="Cloud",

            business_criticality="Critical",

            environment="Production",

            status="Active"

        )

    # ==============================================================
    # Network Technology
    # ==============================================================

    network_apps = [

        "DNS",
        "NTP",
        "NSPM",
        "Proxy",
        "NAC",
        "SB-Connect"

    ]

    for app in network_apps:

        register_application(

            application_name=app,

            department="Network Technology",

            application_type="Infrastructure Service",

            technology_domain="Network",

            business_criticality="Critical",

            environment="Production",

            status="Active"

        )

    # ==============================================================
    # NG-Data Warehouse
    # ==============================================================

    datawarehouse_apps = [

        "CP4D",
        "RTC",
        "CDC",
        "CP4I",
        "Cognos",
        "DAS",
        "ESS",
        "ETL",
        "IIAS",
        "Portal",
        "Query Surge",
        "SCAPM",
        "SFG",
        "SKLM",
        "TSM",
        "TWS"

    ]

    for app in datawarehouse_apps:

        register_application(

            application_name=app,

            department="NG-Data Ware House",

            application_type="Technology Platform",

            technology_domain="Data Warehouse",

            business_criticality="High",

            environment="Production",

            status="Active"

        )

# =============================================================================
# Register Enterprise Inventory
# =============================================================================

register_all_enterprise_applications()

# =============================================================================
# Register Enterprise Applications
# =============================================================================

print()

print("=" * 80)
print("Building Application Master...")
print("=" * 80)

MASTER_APPLICATIONS = []

for application in APPLICATION_RECORDS:

    application_id = generate_application_id()

    APPLICATION_LOOKUP[
        application["Application Name"]
    ] = application_id

    MASTER_APPLICATIONS.append({

        "Application ID":
            application_id,

        "Application Name":
            application["Application Name"],

        "Department":
            application["Department"],

        "Application Type":
            application["Application Type"],

        "Technology Domain":
            application["Technology Domain"],

        "Business Criticality":
            application["Business Criticality"],

        "Environment":
            application["Environment"],

        "Status":
            application["Status"]

    })

print(

    f"Registered {len(MASTER_APPLICATIONS)} applications."

)

# =============================================================================
# Build Application Master DataFrame
# =============================================================================

print()

print("=" * 80)
print("Creating Application Master...")
print("=" * 80)

application_master_df = pd.DataFrame(

    MASTER_APPLICATIONS

)

print(

    f"Total Applications : {len(application_master_df)}"

)

# =============================================================================
# Validate Application Master
# =============================================================================

print()

print("=" * 80)
print("Validating Application Master...")
print("=" * 80)


# -------------------------------------------------------------------------
# Check 1 : Duplicate Application IDs
# -------------------------------------------------------------------------

duplicate_ids = application_master_df[
    application_master_df.duplicated(
        subset=["Application ID"],
        keep=False
    )
]

assert duplicate_ids.empty, (
    "Duplicate Application IDs detected."
)


# -------------------------------------------------------------------------
# Check 2 : Duplicate Application Names
# -------------------------------------------------------------------------

duplicate_names = application_master_df[
    application_master_df.duplicated(
        subset=["Application Name"],
        keep=False
    )
]

assert duplicate_names.empty, (
    "Duplicate Application Names detected."
)


# -------------------------------------------------------------------------
# Check 3 : Mandatory Fields
# -------------------------------------------------------------------------

mandatory_columns = [

    "Application ID",
    "Application Name",
    "Department",
    "Application Type",
    "Technology Domain",
    "Business Criticality",
    "Environment",
    "Status"

]

for column in mandatory_columns:

    assert (

        application_master_df[column]
        .isnull()
        .sum()

        == 0

    ), f"Missing values detected in '{column}'."


# -------------------------------------------------------------------------
# Check 4 : Expected Inventory Count
# -------------------------------------------------------------------------

EXPECTED_APPLICATIONS = 62

assert (

    len(application_master_df)

    ==

    EXPECTED_APPLICATIONS

), (

    f"Expected {EXPECTED_APPLICATIONS} applications, "
    f"but found {len(application_master_df)}."

)


print("Application Master validation completed successfully.")

# =============================================================================
# Export Application Master
# =============================================================================

application_master_df.to_excel(

    APPLICATION_MASTER_PATH,

    index=False

)

print()

print("Application Master exported successfully.")

print()

print("=" * 80)
print("BUILD SUMMARY")
print("=" * 80)

print(

    f"Applications Registered : "
    f"{len(application_master_df)}"

)

print(

    f"Departments Covered     : "
    f"{application_master_df['Department'].nunique()}"

)

print(

    f"Technology Domains      : "
    f"{application_master_df['Technology Domain'].nunique()}"

)

print(

    f"Business Applications   : "

    f"{len(application_master_df[application_master_df['Application Type'] == 'Business Application'])}"

)

print(

    f"Infrastructure Services : "

    f"{len(application_master_df[application_master_df['Application Type'] == 'Infrastructure Service'])}"

)

print(

    f"Technology Platforms    : "

    f"{len(application_master_df[application_master_df['Application Type'] == 'Technology Platform'])}"

)

print("=" * 80)