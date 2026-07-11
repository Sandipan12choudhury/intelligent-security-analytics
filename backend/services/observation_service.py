"""
==============================================================================
Observation Service

Purpose
-------
Business logic for Enterprise Observations - listing, retrieving,
and creating new user-generated observations.

New observations are appended directly to the source Excel files
(observation_library.xlsx and observation_application_mapping.xlsx)
so they become a permanent part of the dataset, in the same row
order as everything else (new rows always go last, which is also
how their Observation ID is derived - see dataset_manager.py).

After a new observation is appended, the existing ML analytics
builder scripts (under /ml) are re-run so every downstream analytics
table (application/department/activity/enterprise) reflects it.

Author
------
Sandipan Choudhury
==============================================================================
"""

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from backend.dataset_manager import dataset_manager
from backend.models.observation_models import CreateObservationRequest
from backend.services.analytics_pipeline_service import (
    AnalyticsPipelineService,
    AnalyticsPipelineError
)
from backend.logging_config import data_logger

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

DATASET_DIR = PROJECT_ROOT / "dataset"

OBSERVATION_LIBRARY_PATH = DATASET_DIR / "observation_library.xlsx"

OBSERVATION_MAPPING_PATH = DATASET_DIR / "observation_application_mapping.xlsx"

RECENT_LOG_PATH = DATASET_DIR / "user_generated_observations_log.json"

VALID_SEVERITIES = ["High", "Medium", "Low"]


class ObservationService:

    def __init__(self):

        self.pipeline = AnalyticsPipelineService()

    # ============================================================
    # All Observations
    # ============================================================

    def get_observations(self):

        observation_df = dataset_manager.get_observation_library()

        mapping_df = dataset_manager.get_observation_mapping()

        merged = observation_df.merge(

            mapping_df[

                [
                    "Observation ID",
                    "Application ID",
                    "Application Name",
                    "Department"
                ]

            ],

            on="Observation ID",

            how="left"

        )

        return {

            "observations": merged.to_dict(orient="records")

        }

    # ============================================================
    # Single Observation
    # ============================================================

    def get_observation(self, observation_id: str):

        observation_df = dataset_manager.get_observation_library()

        mapping_df = dataset_manager.get_observation_mapping()

        merged = observation_df.merge(

            mapping_df[

                [
                    "Observation ID",
                    "Application ID",
                    "Application Name",
                    "Department"
                ]

            ],

            on="Observation ID",

            how="left"

        )

        record = merged[merged["Observation ID"] == observation_id]

        if record.empty:

            return {

                "success": False,

                "message": "Observation not found"

            }

        return {

            "success": True,

            "observation": record.iloc[0].to_dict()

        }

    # ============================================================
    # Metadata for the "Add Observation" form
    # (departments -> applications, activities -> domains)
    # ============================================================

    def get_meta(self):

        application_df = dataset_manager.get_application_dataset()

        observation_df = dataset_manager.get_observation_library()

        departments = sorted(

            application_df["Department"].dropna().unique().tolist()

        )

        applications = application_df[

            ["Application ID", "Application Name", "Department"]

        ].drop_duplicates().to_dict(orient="records")

        activities = sorted(

            observation_df["Activity"].dropna().unique().tolist()

        )

        domains = observation_df[

            ["Activity", "Domain"]

        ].drop_duplicates().to_dict(orient="records")

        return {

            "departments": departments,

            "applications": applications,

            "activities": activities,

            "domains": domains

        }

    # ============================================================
    # Create a new user-generated observation
    # ============================================================

    def create_observation(self, request: CreateObservationRequest):

        # --------------------------------------------------------
        # Validate
        # --------------------------------------------------------

        if request.severity not in VALID_SEVERITIES:

            return {

                "success": False,

                "message": "Severity must be High, Medium, or Low."

            }

        if not request.observation.strip():

            return {

                "success": False,

                "message": "Observation text cannot be empty."

            }

        application_df = dataset_manager.get_application_dataset()

        application_match = application_df[

            (application_df["Department"] == request.department) &
            (application_df["Application Name"] == request.application_name)

        ]

        if application_match.empty:

            return {

                "success": False,

                "message":
                    "That application was not found under the "
                    "selected department."

            }

        application_id = application_match.iloc[0]["Application ID"]

        observation_df = dataset_manager.get_observation_library()

        valid_domain = observation_df[

            (observation_df["Activity"] == request.activity) &
            (observation_df["Domain"] == request.domain)

        ]

        if valid_domain.empty:

            return {

                "success": False,

                "message":
                    "That domain does not belong to the selected "
                    "activity."

            }

        # --------------------------------------------------------
        # Append to observation_library.xlsx
        # (raw file has no Observation ID column - it is derived
        # purely from row position when the app loads it)
        # --------------------------------------------------------

        library_df = pd.read_excel(OBSERVATION_LIBRARY_PATH)

        new_library_row = {

            "Activity": request.activity,

            "Domain": request.domain,

            "Observation": request.observation.strip(),

            "Severity": request.severity

        }

        library_df = pd.concat(

            [library_df, pd.DataFrame([new_library_row])],

            ignore_index=True

        )

        new_observation_id = f"OBS-{len(library_df):04d}"

        library_df.to_excel(OBSERVATION_LIBRARY_PATH, index=False)

        # --------------------------------------------------------
        # Append to observation_application_mapping.xlsx
        # --------------------------------------------------------

        mapping_df = pd.read_excel(OBSERVATION_MAPPING_PATH)

        new_mapping_row = {

            "Observation ID": new_observation_id,

            "Activity": request.activity,

            "Application ID": application_id,

            "Application Name": request.application_name,

            "Department": request.department

        }

        mapping_df = pd.concat(

            [mapping_df, pd.DataFrame([new_mapping_row])],

            ignore_index=True

        )

        mapping_df.to_excel(OBSERVATION_MAPPING_PATH, index=False)

        # --------------------------------------------------------
        # Recompute every downstream analytics table
        # --------------------------------------------------------

        try:

            self.pipeline.run_pipeline()

        except AnalyticsPipelineError as error:

            return {

                "success": False,

                "message":
                    "Observation was saved, but recalculating "
                    f"analytics failed: {error}"

            }

        # --------------------------------------------------------
        # Reload everything into memory so the new observation
        # (and refreshed analytics) show up without a server
        # restart
        # --------------------------------------------------------

        dataset_manager.load_all_datasets(verbose=False)

        new_observation = {

            "Observation ID": new_observation_id,

            "Activity": request.activity,

            "Domain": request.domain,

            "Observation": request.observation.strip(),

            "Severity": request.severity,

            "Application ID": application_id,

            "Application Name": request.application_name,

            "Department": request.department

        }

        self._record_recent(new_observation)

        data_logger.info(

            "New observation created",

            extra={"extra_data": {

                "observation_id": new_observation_id,

                "application_name": request.application_name,

                "department": request.department,

                "severity": request.severity

            }}

        )

        return {

            "success": True,

            "observation_id": new_observation_id,

            "observation": new_observation

        }

    # ============================================================
    # Recent user-generated observations (Dashboard widget)
    # ============================================================

    def _record_recent(self, observation: dict):

        entries = self._read_recent_log()

        entries.append({

            **observation,

            "created_at": datetime.now(timezone.utc).isoformat()

        })

        with open(RECENT_LOG_PATH, "w", encoding="utf-8") as log_file:

            json.dump(entries, log_file, indent=2)

    def _read_recent_log(self):

        if not RECENT_LOG_PATH.exists():

            return []

        try:

            with open(RECENT_LOG_PATH, "r", encoding="utf-8") as log_file:

                return json.load(log_file)

        except (json.JSONDecodeError, OSError):

            return []

    def get_recent_observations(self, limit: int = 5):

        entries = self._read_recent_log()

        entries_sorted = sorted(

            entries,

            key=lambda entry: entry.get("created_at", ""),

            reverse=True

        )

        return entries_sorted[:limit]

    # ============================================================
    # Delete Observations
    #
    # Observation IDs are POSITIONAL (OBS-0001 is simply "row 1"),
    # not a stored, permanent label - see dataset_manager.py. That
    # means removing a row from the middle shifts the ID of every
    # row after it, exactly like deleting a row in a spreadsheet.
    # This method removes the requested rows from both source files,
    # keeps them in sync, and re-runs the analytics pipeline so every
    # downstream number reflects the deletion.
    # ============================================================

    def delete_observations(self, observation_ids: list):

        if not observation_ids:

            return {

                "success": False,

                "message": "No observations were selected."

            }

        requested_ids = set(observation_ids)

        library_df = pd.read_excel(OBSERVATION_LIBRARY_PATH)

        mapping_df = pd.read_excel(OBSERVATION_MAPPING_PATH)

        total_rows = len(library_df)

        all_ids = [f"OBS-{i:04d}" for i in range(1, total_rows + 1)]

        indices_to_drop = [

            i for i, observation_id in enumerate(all_ids)

            if observation_id in requested_ids

        ]

        if not indices_to_drop:

            return {

                "success": False,

                "message": "None of the selected observations were found."

            }

        library_df = library_df.drop(

            index=indices_to_drop

        ).reset_index(drop=True)

        mapping_df = mapping_df[

            ~mapping_df["Observation ID"].isin(requested_ids)

        ].reset_index(drop=True)

        # Regenerate mapping IDs positionally so they stay in lockstep
        # with the (now shorter) library file - this is the same rule
        # dataset_manager.py already applies on every load.

        mapping_df["Observation ID"] = [

            f"OBS-{i:04d}" for i in range(1, len(mapping_df) + 1)

        ]

        library_df.to_excel(OBSERVATION_LIBRARY_PATH, index=False)

        mapping_df.to_excel(OBSERVATION_MAPPING_PATH, index=False)

        try:

            self.pipeline.run_pipeline()

        except AnalyticsPipelineError as error:

            return {

                "success": False,

                "message":
                    "Observations were deleted, but recalculating "
                    f"analytics failed: {error}"

            }

        dataset_manager.load_all_datasets(verbose=False)

        self._remove_from_recent_log(requested_ids)

        data_logger.warning(

            "Observations deleted",

            extra={"extra_data": {

                "deleted_ids": sorted(requested_ids),

                "count": len(indices_to_drop)

            }}

        )

        return {

            "success": True,

            "deleted_count": len(indices_to_drop)

        }

    def _remove_from_recent_log(self, deleted_ids: set):

        entries = self._read_recent_log()

        remaining = [

            entry for entry in entries

            if entry.get("Observation ID") not in deleted_ids

        ]

        with open(RECENT_LOG_PATH, "w", encoding="utf-8") as log_file:

            json.dump(remaining, log_file, indent=2)
