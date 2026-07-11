"""
==============================================================================
Analytics Pipeline Service

Purpose
-------
Re-runs the project's existing ML dataset-builder scripts (under /ml)
in the correct dependency order, so that every downstream analytics
table stays consistent after a new observation is appended.

This module does NOT re-implement any scoring/ranking logic itself -
it simply invokes the same scripts that originally produced these
datasets, so the numbers stay exactly consistent with how the rest
of the project was built.

Pipeline order (dependency-driven):

    1. build_application_dataset.py
       reads observation_library + observation_application_mapping
       writes application_dataset.xlsx

    2. build_application_analytics_dataset.py
       reads application_dataset.xlsx
       writes application_analytics_dataset.xlsx

    3. build_department_analytics_dataset.py
       reads application_analytics_dataset.xlsx
       writes department_analytics_dataset.xlsx

    4. build_activity_analytics_dataset.py
       reads observation_library + observation_application_mapping
       writes activity_analytics_dataset.xlsx

    5. build_enterprise_analytics_dataset.py
       reads department_analytics_dataset.xlsx
       writes enterprise_analytics_dataset.xlsx

Author
------
Sandipan Choudhury
==============================================================================
"""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

ML_DIR = PROJECT_ROOT / "ml"

PIPELINE_SCRIPTS = [

    "build_application_dataset.py",

    "build_application_analytics_dataset.py",

    "build_department_analytics_dataset.py",

    "build_activity_analytics_dataset.py",

    "build_enterprise_analytics_dataset.py"

]


class AnalyticsPipelineError(Exception):

    pass


class AnalyticsPipelineService:

    def run_pipeline(self):

        for script_name in PIPELINE_SCRIPTS:

            script_path = ML_DIR / script_name

            result = subprocess.run(

                [sys.executable, str(script_path)],

                cwd=str(PROJECT_ROOT),

                capture_output=True,

                text=True

            )

            if result.returncode != 0:

                raise AnalyticsPipelineError(

                    f"Analytics pipeline failed at {script_name}:\n"
                    f"{result.stderr}"

                )

        return True
