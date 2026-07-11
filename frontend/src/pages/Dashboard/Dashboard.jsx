import { useEffect, useState } from "react";

import Sidebar from "/src/components/dashboard/Sidebar";
import DashboardHeader from "/src/components/dashboard/DashboardHeader";

import KPICards from "/src/components/dashboard/KPICards";
import DepartmentalAnalytics from "/src/components/dashboard/DepartmentalAnalytics";
import ActivityAnalytics from "/src/components/dashboard/ActivityAnalytics";
import TopRiskApplications from "/src/components/dashboard/TopRiskApplications";
import RecentObservations from "/src/components/dashboard/RecentObservations";
import ExecutiveSummary from "/src/components/dashboard/ExecutiveSummary";

import "/src/pages/Dashboard/Dashboard.css";

import usePageTitle from "/src/utils/usePageTitle";

import API_BASE from "/src/config/api";

export default function Dashboard() {

    usePageTitle("Dashboard");

    const [dashboardData, setDashboardData] = useState(null);

    useEffect(() => {

        fetch(`${API_BASE}/api/v1/dashboard/`)

            .then((response) => response.json())

            .then((data) => {

                console.log("Dashboard Data :", data);

                setDashboardData(data);

            })

            .catch(console.error);

    }, []);

    if (!dashboardData) {

        return <div>Loading Dashboard...</div>;

    }

    return (

        <div className="dashboard-layout">

            <Sidebar />

            <main className="dashboard-content">

                <DashboardHeader />

                <KPICards
                    enterprise={dashboardData.enterprise}
                />

                <ExecutiveSummary
                    enterprise={dashboardData.enterprise}
                />

                <DepartmentalAnalytics
                    departments={dashboardData.departments}
                />

                <ActivityAnalytics
                    activities={dashboardData.activities}
                />

                <TopRiskApplications
                    applications={dashboardData.applications}
                />

                <RecentObservations
                    recentObservations={dashboardData.recent_observations}
                />

            </main>

        </div>

    );

}