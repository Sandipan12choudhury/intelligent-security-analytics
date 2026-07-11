"""
========================================================
DEPRECATED SCRIPT

This script was used during the initial experimentation
phase.

DO NOT USE FOR GENERATING THE PRODUCTION
OBSERVATION REPOSITORY.

Current production scripts:

- build_user_management_library.py
- build_password_management_library.py
- ...

========================================================
"""
import random
from pathlib import Path

import pandas as pd

from observation_templates import (
    USER_MANAGEMENT_ADVANCED_SCENARIOS
)

# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "dataset"

OUTPUT_FILE = DATASET_DIR / "observation_library.xlsx"

# ============================================================
# CONFIGURATION
# ============================================================

TOTAL_OBSERVATIONS = 120

# ============================================================
# OBSERVATION WRITING STYLES
# ============================================================

OBSERVATION_STYLES = [

    lambda s:
        f"Review of {s['review']} {s['scope']} indicates that {s['gap']}. {s['impact']}.",

    lambda s:
        f"During review of {s['review']} {s['scope']}, it was observed that {s['gap']}. {s['impact']}.",

    lambda s:
        f"Assessment of {s['review']} {s['scope']} identified that {s['gap']}. {s['impact']}.",

    lambda s:
        f"Validation of {s['review']} {s['scope']} revealed that {s['gap']}. {s['impact']}."
]

# ============================================================
# GENERATE OBSERVATION
# ============================================================

def generate_observation():

    scenario = random.choice(
        USER_MANAGEMENT_ADVANCED_SCENARIOS
    )

    style = random.choice(
        OBSERVATION_STYLES
    )

    observation = style(
        scenario
    )

    return {
        "Activity": "ITGC",
        "Domain": "User Management",
        "Observation": observation,
        "Severity": scenario["severity"]
    }

# ============================================================
# GENERATE DATASET
# ============================================================

records = []

generated = set()

attempts = 0

MAX_ATTEMPTS = 10000

while (
    len(records) < TOTAL_OBSERVATIONS
    and attempts < MAX_ATTEMPTS
):

    attempts += 1

    record = generate_observation()

    if record["Observation"] in generated:
        continue

    generated.add(
        record["Observation"]
    )

    records.append(
        record
    )

# ============================================================
# DATAFRAME
# ============================================================

df = pd.DataFrame(records)

# ============================================================
# SORT
# ============================================================

severity_order = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}

df["Sort_Order"] = (
    df["Severity"]
    .map(severity_order)
)

df = (
    df.sort_values("Sort_Order")
      .drop(columns=["Sort_Order"])
      .reset_index(drop=True)
)

# ============================================================
# SAVE
# ============================================================

df.to_excel(
    OUTPUT_FILE,
    index=False
)

# ============================================================
# REPORTING
# ============================================================

print("\n======================================")
print("Observation Library Generated")
print("======================================")

print(
    f"\nTotal Observations : {len(df)}"
)

print("\nSeverity Distribution")
print(
    df["Severity"]
    .value_counts()
)

print(
    f"\nOutput File:\n{OUTPUT_FILE}"
)

print("\nGeneration Completed Successfully.")