"""
==============================================================================
Dashboard Service

Purpose
-------
Business logic for Dashboard Analytics.

Author
------
Sandipan Choudhury
==============================================================================
"""

from backend.dataset_manager import dataset_manager
from backend.services.observation_service import ObservationService


class DashboardService:

    def __init__(self):

        self.observation_service = ObservationService()

    def get_dashboard(self):

        return {

            "enterprise":

                dataset_manager.get_enterprise_analytics().to_dict(
                    orient="records"
                )[0],

            "applications":

                dataset_manager.get_application_analytics().to_dict(
                    orient="records"
                ),

            "departments":

                dataset_manager.get_department_analytics().to_dict(
                    orient="records"
                ),

            "activities":

                dataset_manager.get_activity_analytics().to_dict(
                    orient="records"
                ),

            "recent_observations":

                self.observation_service.get_recent_observations()

        }