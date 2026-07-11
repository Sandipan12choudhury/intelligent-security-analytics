import { useEffect, useMemo, useState } from "react";

import { useLocation, useNavigate } from "react-router-dom";

import Sidebar from "/src/components/dashboard/Sidebar";

import ObservationHeader
    from "/src/components/observations/ObservationHeader";
import ObservationFilters
    from "/src/components/observations/ObservationFilters";
import ObservationsTable
    from "/src/components/observations/ObservationsTable";
import ObservationResultsModal
    from "/src/components/observations/ObservationResultsModal";
import DeleteConfirmModal
    from "/src/components/observations/DeleteConfirmModal";

import "./Observations.css";

import usePageTitle from "/src/utils/usePageTitle";

import API_BASE from "/src/config/api";

// Returns true if an observation matches all of the given filters,
// optionally skipping one field (used to build cascading dropdown
// options - e.g. when building the "Application" list, we still
// respect Department/Activity/Severity, but not Application itself).

function matchesFilters(observation, filters, skipField) {

    const {

        severity,
        activity,
        department,
        applicationName

    } = filters;

    if (

        skipField !== "severity" &&
        severity !== "" &&
        observation["Severity"] !== severity

    ) {

        return false;

    }

    if (

        skipField !== "activity" &&
        activity !== "" &&
        observation["Activity"] !== activity

    ) {

        return false;

    }

    if (

        skipField !== "department" &&
        department !== "" &&
        observation["Department"] !== department

    ) {

        return false;

    }

    if (

        skipField !== "applicationName" &&
        applicationName !== "" &&
        observation["Application Name"] !== applicationName

    ) {

        return false;

    }

    return true;

}

function uniqueValues(observations, field, filters, skipField) {

    const values = observations

        .filter((observation) => matchesFilters(observation, filters, skipField))

        .map((observation) => observation[field]);

    return [...new Set(values)].filter(Boolean).sort();

}

export default function Observations() {

    usePageTitle("Observations");

    const location = useLocation();

    const navigate = useNavigate();

    const [observations, setObservations] = useState([]);

    const [loading, setLoading] = useState(true);

    const [search, setSearch] = useState("");

    const [severity, setSeverity] = useState("");

    const [activity, setActivity] = useState("");

    const [department, setDepartment] = useState("");

    const [applicationName, setApplicationName] = useState("");

    const [selectedObservation, setSelectedObservation] = useState(null);

    const [selectedIds, setSelectedIds] = useState(new Set());

    const [confirmingDelete, setConfirmingDelete] = useState(false);

    const [deleting, setDeleting] = useState(false);

    const [highlightId, setHighlightId] = useState(

        location.state?.highlightId || null

    );

    function loadObservations() {

        setLoading(true);

        return fetch(`${API_BASE}/api/v1/observations/`)

            .then((response) => response.json())

            .then((data) => {

                setObservations(data.observations);

                setLoading(false);

            })

            .catch((error) => {

                console.error(error);

                setLoading(false);

            });

    }

    useEffect(() => {

        loadObservations();

    }, []);

    // If we arrived here from the Dashboard's "Recent Observations"
    // widget, clear any active filters (so the target row is
    // guaranteed to be visible) and scroll to / briefly highlight it
    // once the data has loaded.

    useEffect(() => {

        if (!highlightId || loading) {

            return;

        }

        clearFilters();

        const timer = setTimeout(() => {

            document

                .getElementById(`observation-row-${highlightId}`)

                ?.scrollIntoView({ behavior: "smooth", block: "center" });

        }, 150);

        const clearHighlight = setTimeout(() => {

            setHighlightId(null);

            navigate(location.pathname, { replace: true, state: {} });

        }, 4000);

        return () => {

            clearTimeout(timer);

            clearTimeout(clearHighlight);

        };

        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [loading]);

    const activeFilters = {

        severity,
        activity,
        department,
        applicationName

    };

    // Each dropdown's options only reflect the OTHER active filters,
    // so picking a Department narrows the Application list (and
    // vice versa), instead of always showing every value.

    const activities = useMemo(() => {

        return uniqueValues(

            observations, "Activity", activeFilters, "activity"

        );

    }, [observations, severity, activity, department, applicationName]);

    const departments = useMemo(() => {

        return uniqueValues(

            observations, "Department", activeFilters, "department"

        );

    }, [observations, severity, activity, department, applicationName]);

    const applicationNames = useMemo(() => {

        return uniqueValues(

            observations,
            "Application Name",
            activeFilters,
            "applicationName"

        );

    }, [observations, severity, activity, department, applicationName]);

    const filteredObservations = observations.filter((observation) => {

        const searchLower = search.toLowerCase();

        const matchesSearch =

            (observation["Observation"] || "")

                .toLowerCase()

                .includes(searchLower)

            ||

            (observation["Observation ID"] || "")

                .toLowerCase()

                .includes(searchLower);

        return (

            matchesSearch &&

            matchesFilters(observation, activeFilters, null)

        );

    });

    // If the currently selected Department/Activity/Application no
    // longer applies to each other (e.g. Department changed and the
    // previously chosen Application belongs to a different
    // department), clear the now-invalid selection automatically.

    useEffect(() => {

        if (applicationName && !applicationNames.includes(applicationName)) {

            setApplicationName("");

        }

    }, [applicationNames]);

    useEffect(() => {

        if (department && !departments.includes(department)) {

            setDepartment("");

        }

    }, [departments]);

    useEffect(() => {

        if (activity && !activities.includes(activity)) {

            setActivity("");

        }

    }, [activities]);

    function clearFilters() {

        setSearch("");

        setSeverity("");

        setActivity("");

        setDepartment("");

        setApplicationName("");

    }

    // ============================================================
    // Selection & Delete
    // ============================================================

    function toggleSelect(observationId) {

        setSelectedIds((prev) => {

            const next = new Set(prev);

            if (next.has(observationId)) {

                next.delete(observationId);

            } else {

                next.add(observationId);

            }

            return next;

        });

    }

    function toggleSelectAll(visibleObservations) {

        const visibleIds = visibleObservations.map(

            (observation) => observation["Observation ID"]

        );

        const allSelected = visibleIds.every(

            (id) => selectedIds.has(id)

        );

        setSelectedIds((prev) => {

            const next = new Set(prev);

            if (allSelected) {

                visibleIds.forEach((id) => next.delete(id));

            } else {

                visibleIds.forEach((id) => next.add(id));

            }

            return next;

        });

    }

    function handleDeleteSelected() {

        setConfirmingDelete(true);

    }

    function confirmDelete() {

        setDeleting(true);

        fetch(`${API_BASE}/api/v1/observations/delete`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({

                observation_ids: Array.from(selectedIds)

            })

        })

            .then((response) => response.json())

            .then((data) => {

                if (!data.success) {

                    alert(data.message || "Failed to delete observations.");

                    return;

                }

                setSelectedIds(new Set());

                setConfirmingDelete(false);

                return loadObservations();

            })

            .catch(() => {

                alert("Something went wrong while deleting.");

            })

            .finally(() => {

                setDeleting(false);

            });

    }

    return (

        <div className="dashboard-layout">

            <Sidebar />

            <main className="dashboard-content">

                <ObservationHeader />

                <ObservationFilters

                    search={search}
                    setSearch={setSearch}

                    severity={severity}
                    setSeverity={setSeverity}

                    activity={activity}
                    setActivity={setActivity}

                    department={department}
                    setDepartment={setDepartment}

                    applicationName={applicationName}
                    setApplicationName={setApplicationName}

                    activities={activities}

                    departments={departments}

                    applicationNames={applicationNames}

                />

                {

                    loading ? (

                        <div className="observations-loading">

                            Loading Observations...

                        </div>

                    ) : (

                        <ObservationsTable

                            observations={filteredObservations}

                            totalObservations={observations.length}

                            clearFilters={clearFilters}

                            onSelectObservation={setSelectedObservation}

                            selectedIds={selectedIds}

                            onToggleSelect={toggleSelect}

                            onToggleSelectAll={toggleSelectAll}

                            onDeleteSelected={handleDeleteSelected}

                            highlightId={highlightId}

                        />

                    )

                }

            </main>

            {

                selectedObservation && (

                    <ObservationResultsModal

                        observation={selectedObservation}

                        onClose={() => setSelectedObservation(null)}

                    />

                )

            }

            {

                confirmingDelete && (

                    <DeleteConfirmModal

                        count={selectedIds.size}

                        deleting={deleting}

                        onConfirm={confirmDelete}

                        onCancel={() => setConfirmingDelete(false)}

                    />

                )

            }

        </div>

    );

}
