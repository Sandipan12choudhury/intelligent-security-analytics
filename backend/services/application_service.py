"""
==============================================================================
Application Service

Purpose
-------
Business logic for Enterprise Applications.

Author
------
Sandipan Choudhury
==============================================================================
"""

from backend.dataset_manager import dataset_manager


class ApplicationService:

    # ============================================================
    # All Applications
    # ============================================================

    def get_applications(self):

        return {

            "applications":

                dataset_manager.get_application_analytics().to_dict(

                    orient="records"

                )

        }

    # ============================================================
    # Single Application
    # ============================================================

    def get_application(self, application_id: str):

        dataframe = dataset_manager.get_application_analytics()

        application = dataframe[

            dataframe["Application ID"] == application_id

        ]

        if application.empty:

            return {

                "success": False,

                "message": "Application not found"

            }

        return {

            "success": True,

            "application":

                application.iloc[0].to_dict()

        }