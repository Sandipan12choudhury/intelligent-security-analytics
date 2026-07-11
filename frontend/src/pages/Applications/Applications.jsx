import { useEffect, useMemo, useState } from "react";

import Sidebar from "/src/components/dashboard/Sidebar";

import ApplicationHeader from "/src/components/applications/ApplicationHeader";
import ApplicationFilters from "/src/components/applications/ApplicationFilters";
import ApplicationsTable from "/src/components/applications/ApplicationsTable";

import "./Applications.css";

import usePageTitle from "/src/utils/usePageTitle";

import API_BASE from "/src/config/api";

export default function Applications() {

    usePageTitle("Applications");

    const [applications, setApplications] = useState([]);

    const [search, setSearch] = useState("");

    const [department, setDepartment] = useState("");

    const [risk, setRisk] = useState("");

    const [priority, setPriority] = useState("");

    useEffect(() => {

        fetch(`${API_BASE}/api/v1/applications/`)

            .then((response) => response.json())

            .then((data) => {

                setApplications(data.applications);

            })

            .catch(console.error);

    }, []);

    const departments = useMemo(() => {

        return [

            ...new Set(

                applications.map(

                    (application) => application.Department

                )

            )

        ];

    }, [applications]);

    const filteredApplications = applications.filter((application) => {

        const matchesSearch =

            application["Application Name"]

                .toLowerCase()

                .includes(search.toLowerCase())

            ||

            application["Application ID"]

                .toLowerCase()

                .includes(search.toLowerCase());

        const matchesDepartment =

            department === ""

            ||

            application.Department === department;

        const matchesRisk =

            risk === ""

            ||

            application["Risk Category"] === risk;

        const matchesPriority =

            priority === ""

            ||

            application["Executive Priority"] === priority;

        return (

            matchesSearch

            &&

            matchesDepartment

            &&

            matchesRisk

            &&

            matchesPriority

        );

    });

    // ===========================================================
    // Clear Filters
    // ===========================================================

    function clearFilters() {

        setSearch("");

        setDepartment("");

        setRisk("");

        setPriority("");

    }

    return (

        <div className="dashboard-layout">

            <Sidebar />

            <main className="dashboard-content">

                <ApplicationHeader />

                <ApplicationFilters

                    search={search}
                    setSearch={setSearch}

                    department={department}
                    setDepartment={setDepartment}

                    risk={risk}
                    setRisk={setRisk}

                    priority={priority}
                    setPriority={setPriority}

                    departments={departments}

                />

                <ApplicationsTable

                    applications={filteredApplications}

                    totalApplications={applications.length}

                    clearFilters={clearFilters}

                />

            </main>

        </div>

    );

}