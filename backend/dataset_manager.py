"""
==============================================================================
Dataset Manager

Purpose
-------
Centralized data access layer for the Intelligent Security Analytics Platform.

Responsibilities
----------------
• Load all enterprise datasets
• Validate dataset availability
• Cache datasets in memory
• Provide controlled dataset access

This module does NOT:

    • Perform analytics
    • Generate AI responses
    • Modify datasets
    • Execute business logic

Author
------
Sandipan Choudhury

==============================================================================
"""

from pathlib import Path

import pandas as pd

# =============================================================================
# Dataset Manager
# =============================================================================

class DatasetManager:

    """
    Centralized enterprise dataset manager.
    """

    def __init__(self):

        project_root = Path(__file__).resolve().parent.parent

        self.dataset_folder = project_root / "dataset"

        self.datasets = {}

        self.load_all_datasets(verbose=False)

# =============================================================================
# Load All Datasets
# =============================================================================

    def load_all_datasets(self, verbose: bool = True):
        if verbose:
            print()
            print("=" * 80)
            print("Loading Enterprise Datasets...")
            print("=" * 80)

        dataset_files = {
            "observation_library":
                "observation_library.xlsx",

            "observation_mapping":
                "observation_application_mapping.xlsx",
            
            "application_dataset":
                "application_dataset.xlsx",

            "application_analytics":
                "application_analytics_dataset.xlsx",

            "department_analytics":
                "department_analytics_dataset.xlsx",

            "activity_analytics":
                "activity_analytics_dataset.xlsx",

            "enterprise_analytics":
                "enterprise_analytics_dataset.xlsx",

            "ai_repository":
                "ai_repository_dataset.xlsx"
        }

        for key, filename in dataset_files.items():
            path = self.dataset_folder / filename
            try:
                dataframe = pd.read_excel(path)
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"\nRequired dataset not found:\n{path}\n"
                )       
            # ==========================================================
            # Dataset Preprocessing
            # ==========================================================

            if key == "observation_library":
                if "Observation ID" not in dataframe.columns:
                    dataframe.insert(
                        0,
                        "Observation ID",
                        [
                            f"OBS-{i:04d}"
                            for i in range(1, len(dataframe) + 1)
                        ]
                    )
            
            self.datasets[key] = dataframe
            if verbose:
                print(f"{key:<25}: {len(dataframe)} records")

        if verbose:
            print()
            print(f"Datasets Loaded          : {len(self.datasets)}")
            print("All enterprise datasets loaded successfully.")

# =============================================================================
# Getter Methods
# =============================================================================

    def get_dataset(self, dataset_name: str):

        """
        Returns a dataset by name.
        """

        if dataset_name not in self.datasets:

            raise ValueError(
                f"Unknown dataset: {dataset_name}"
            )

        return self.datasets[dataset_name]

    def get_observation_library(self):
        return self.get_dataset("observation_library")

    def get_observation_mapping(self):
        return self.get_dataset("observation_mapping")

    def get_application_dataset(self):
        return self.get_dataset("application_dataset")

    def get_application_analytics(self):
        return self.get_dataset("application_analytics")

    def get_department_analytics(self):
        return self.get_dataset("department_analytics")

    def get_activity_analytics(self):
        return self.get_dataset("activity_analytics")

    def get_enterprise_analytics(self):
        return self.get_dataset("enterprise_analytics")

    def get_ai_repository(self):
        return self.get_dataset("ai_repository")
    
# =============================================================================
# Validation
# =============================================================================

    def validate(self):

        """
        Validates that all enterprise datasets
        have been loaded successfully.
        """

        required_datasets = [

            "observation_library",

            "observation_mapping",

            "application_dataset",

            "application_analytics",

            "department_analytics",

            "activity_analytics",

            "enterprise_analytics",

            "ai_repository"

        ]

        for dataset in required_datasets:

            if dataset not in self.datasets:

                raise RuntimeError(
                    f"Missing dataset: {dataset}"
                )

            if self.datasets[dataset].empty:

                raise RuntimeError(
                    f"Dataset is empty: {dataset}"
                )

        return True
    
# =============================================================================
# Shared Dataset Manager Instance
# =============================================================================

dataset_manager = DatasetManager()

# =============================================================================
# Validation
# =============================================================================

def validate_dataset_manager():

    print()

    print("=" * 80)
    print("Validating Dataset Manager...")
    print("=" * 80)

    for name, dataframe in dataset_manager.datasets.items():
        print(f"{name:<25}: {len(dataframe)} records")
    dataset_manager.validate()
    print()
    print("Dataset Manager validation completed successfully.")
    return dataset_manager


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    manager = validate_dataset_manager()

    print()

    print("=" * 80)
    print("DATASET SUMMARY")
    print("=" * 80)

    for name, dataframe in manager.datasets.items():

        print(f"{name:<25}: {len(dataframe)} records")

    print()

    print("=" * 80)
    print("BUILD SUMMARY")
    print("=" * 80)

    print(f"Datasets Loaded      : {len(manager.datasets)}")
    print("Caching Status       : Ready")
    print("Validation Status    : Passed")
    print("Dataset Manager      : Ready")

    print("=" * 80)