import { useEffect, useMemo, useState } from "react";

import { useNavigate } from "react-router-dom";

import Sidebar from "/src/components/dashboard/Sidebar";

import {

    FaPlusCircle,
    FaSpinner,
    FaCheckCircle,
    FaExclamationTriangle

} from "react-icons/fa";

import "./AddObservation.css";

import usePageTitle from "/src/utils/usePageTitle";

import API_BASE from "/src/config/api";

export default function AddObservation() {

    usePageTitle("Add Observation");

    const navigate = useNavigate();

    const [meta, setMeta] = useState(null);

    const [loadingMeta, setLoadingMeta] = useState(true);

    const [department, setDepartment] = useState("");

    const [applicationName, setApplicationName] = useState("");

    const [activity, setActivity] = useState("");

    const [domain, setDomain] = useState("");

    const [observationText, setObservationText] = useState("");

    const [severity, setSeverity] = useState("");

    const [submitting, setSubmitting] = useState(false);

    const [result, setResult] = useState(null);

    useEffect(() => {

        fetch(`${API_BASE}/api/v1/observations/meta`)

            .then((response) => response.json())

            .then((data) => {

                setMeta(data);

                setLoadingMeta(false);

            })

            .catch((error) => {

                console.error(error);

                setLoadingMeta(false);

            });

    }, []);

    const applicationsForDepartment = useMemo(() => {

        if (!meta || !department) {

            return [];

        }

        return meta.applications.filter(

            (app) => app["Department"] === department

        );

    }, [meta, department]);

    const domainsForActivity = useMemo(() => {

        if (!meta || !activity) {

            return [];

        }

        return meta.domains.filter(

            (item) => item["Activity"] === activity

        );

    }, [meta, activity]);

    function handleDepartmentChange(value) {

        setDepartment(value);

        setApplicationName("");

    }

    function handleActivityChange(value) {

        setActivity(value);

        setDomain("");

    }

    const isFormValid =

        department &&
        applicationName &&
        activity &&
        domain &&
        observationText.trim().length > 0 &&
        severity;

    function handleSubmit(e) {

        e.preventDefault();

        if (!isFormValid || submitting) {

            return;

        }

        setSubmitting(true);

        setResult(null);

        fetch(`${API_BASE}/api/v1/observations/`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({

                department,

                application_name: applicationName,

                activity,

                domain,

                observation: observationText.trim(),

                severity

            })

        })

            .then((response) => response.json())

            .then((data) => {

                setResult(data);

                if (data.success) {

                    setDepartment("");

                    setApplicationName("");

                    setActivity("");

                    setDomain("");

                    setObservationText("");

                    setSeverity("");

                }

            })

            .catch(() => {

                setResult({

                    success: false,

                    message: "Something went wrong. Please try again."

                });

            })

            .finally(() => {

                setSubmitting(false);

            });

    }

    return (

        <div className="dashboard-layout">

            <Sidebar />

            <main className="dashboard-content">

                <div className="add-observation-header">

                    <h1>

                        <FaPlusCircle />

                        Add New Observation

                    </h1>

                    <p>

                        Submit a new security observation. It will be
                        added to the enterprise dataset and every
                        analytics table (application, department,
                        activity, and enterprise) will be recalculated
                        automatically.

                    </p>

                </div>

                {

                    loadingMeta ? (

                        <div className="observations-loading">

                            Loading form options...

                        </div>

                    ) : (

                        <form

                            className="dashboard-card add-observation-form"

                            onSubmit={handleSubmit}

                        >

                            <div className="form-row">

                                <div className="form-field">

                                    <label>Department</label>

                                    <select

                                        value={department}

                                        onChange={(e) =>
                                            handleDepartmentChange(e.target.value)
                                        }

                                    >

                                        <option value="">
                                            Select Department
                                        </option>

                                        {

                                            meta.departments.map((item) => (

                                                <option key={item} value={item}>
                                                    {item}
                                                </option>

                                            ))

                                        }

                                    </select>

                                </div>

                                <div className="form-field">

                                    <label>Application</label>

                                    <select

                                        value={applicationName}

                                        onChange={(e) =>
                                            setApplicationName(e.target.value)
                                        }

                                        disabled={!department}

                                    >

                                        <option value="">
                                            {

                                                department
                                                    ? "Select Application"
                                                    : "Select Department First"

                                            }
                                        </option>

                                        {

                                            applicationsForDepartment.map(

                                                (app) => (

                                                    <option

                                                        key={app["Application ID"]}

                                                        value={app["Application Name"]}

                                                    >

                                                        {app["Application Name"]}

                                                    </option>

                                                )

                                            )

                                        }

                                    </select>

                                </div>

                            </div>

                            <div className="form-row">

                                <div className="form-field">

                                    <label>Activity</label>

                                    <select

                                        value={activity}

                                        onChange={(e) =>
                                            handleActivityChange(e.target.value)
                                        }

                                    >

                                        <option value="">
                                            Select Activity
                                        </option>

                                        {

                                            meta.activities.map((item) => (

                                                <option key={item} value={item}>
                                                    {item}
                                                </option>

                                            ))

                                        }

                                    </select>

                                </div>

                                <div className="form-field">

                                    <label>Domain</label>

                                    <select

                                        value={domain}

                                        onChange={(e) =>
                                            setDomain(e.target.value)
                                        }

                                        disabled={!activity}

                                    >

                                        <option value="">
                                            {

                                                activity
                                                    ? "Select Domain"
                                                    : "Select Activity First"

                                            }
                                        </option>

                                        {

                                            domainsForActivity.map((item) => (

                                                <option

                                                    key={item["Domain"]}

                                                    value={item["Domain"]}

                                                >

                                                    {item["Domain"]}

                                                </option>

                                            ))

                                        }

                                    </select>

                                </div>

                            </div>

                            <div className="form-field">

                                <label>Observation</label>

                                <textarea

                                    rows={5}

                                    placeholder="Describe the security observation in detail..."

                                    value={observationText}

                                    onChange={(e) =>
                                        setObservationText(e.target.value)
                                    }

                                />

                            </div>

                            <div className="form-field severity-field">

                                <label>Severity</label>

                                <div className="severity-options">

                                    {

                                        ["High", "Medium", "Low"].map(

                                            (level) => (

                                                <button

                                                    type="button"

                                                    key={level}

                                                    className={

                                                        `severity-option ` +
                                                        `${level.toLowerCase()} ` +
                                                        `${severity === level ? "selected" : ""}`

                                                    }

                                                    onClick={() =>
                                                        setSeverity(level)
                                                    }

                                                >

                                                    {level}

                                                </button>

                                            )

                                        )

                                    }

                                </div>

                            </div>

                            {

                                result && !result.success && (

                                    <div className="form-message error">

                                        <FaExclamationTriangle />

                                        {result.message}

                                    </div>

                                )

                            }

                            {

                                result && result.success && (

                                    <div className="form-message success">

                                        <FaCheckCircle />

                                        Observation {result.observation_id}

                                        {" "}created successfully and

                                        analytics have been updated.

                                        <button

                                            type="button"

                                            className="view-link"

                                            onClick={() =>
                                                navigate("/observations")
                                            }

                                        >

                                            View in Observations

                                        </button>

                                    </div>

                                )

                            }

                            <button

                                type="submit"

                                className="submit-btn"

                                disabled={!isFormValid || submitting}

                            >

                                {

                                    submitting ? (

                                        <>

                                            <FaSpinner className="spin-icon" />

                                            Adding Observation &

                                            Recalculating Analytics...

                                        </>

                                    ) : (

                                        <>

                                            <FaPlusCircle />

                                            Add Observation

                                        </>

                                    )

                                }

                            </button>

                        </form>

                    )

                }

            </main>

        </div>

    );

}
