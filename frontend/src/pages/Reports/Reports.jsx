import { useEffect, useMemo, useState } from "react";

import Sidebar from "/src/components/dashboard/Sidebar";

import {

    FaFileAlt,
    FaDownload,
    FaSpinner,
    FaBuilding,
    FaSearch,
    FaGlobe,
    FaHistory,
    FaTrashAlt

} from "react-icons/fa";

import "./Reports.css";

import usePageTitle from "/src/utils/usePageTitle";

import API_BASE from "/src/config/api";

const REPORT_TYPES = [

    { type: "enterprise", label: "Enterprise-Wide", icon: FaGlobe },

    { type: "department", label: "Department", icon: FaBuilding },

    { type: "application", label: "Application", icon: FaSearch }

];

function formatDate(isoString) {

    return new Date(isoString).toLocaleString("en-IN", {

        day: "2-digit",

        month: "short",

        year: "numeric",

        hour: "2-digit",

        minute: "2-digit"

    });

}

function slugify(text) {

    return String(text)

        .trim()

        .replace(/[^a-zA-Z0-9]+/g, "_")

        .replace(/^_+|_+$/g, "");

}

export default function Reports() {

    usePageTitle("Reports");

    const [meta, setMeta] = useState(null);

    const [history, setHistory] = useState([]);

    const [loadingHistory, setLoadingHistory] = useState(true);

    const [reportType, setReportType] = useState("enterprise");

    const [department, setDepartment] = useState("");

    const [applicationId, setApplicationId] = useState("");

    const [generating, setGenerating] = useState(false);

    const [downloadingId, setDownloadingId] = useState(null);

    const [deletingId, setDeletingId] = useState(null);

    useEffect(() => {

        fetch(`${API_BASE}/api/v1/observations/meta`)

            .then((response) => response.json())

            .then(setMeta)

            .catch(console.error);

        loadHistory();

    }, []);

    function loadHistory() {

        setLoadingHistory(true);

        fetch(`${API_BASE}/api/v1/reports/`)

            .then((response) => response.json())

            .then((data) => {

                setHistory(data.reports);

                setLoadingHistory(false);

            })

            .catch((error) => {

                console.error(error);

                setLoadingHistory(false);

            });

    }

    const applicationsForDepartment = useMemo(() => {

        if (!meta || !department) {

            return [];

        }

        return meta.applications.filter(

            (app) => app["Department"] === department

        );

    }, [meta, department]);

    const selectedApplicationName = useMemo(() => {

        const match = applicationsForDepartment.find(

            (app) => app["Application ID"] === applicationId

        );

        return match ? match["Application Name"] : "";

    }, [applicationsForDepartment, applicationId]);

    function handleTypeChange(type) {

        setReportType(type);

        setDepartment("");

        setApplicationId("");

    }

    const isReady =

        reportType === "enterprise" ||
        (reportType === "department" && department) ||
        (reportType === "application" && department && applicationId);

    function buildDownloadFilename() {

        if (reportType === "enterprise") {

            return "Enterprise_Wide_Security_Report.pdf";

        }

        if (reportType === "department") {

            return `Department_Report_${slugify(department)}.pdf`;

        }

        return `Application_Report_${slugify(selectedApplicationName)}.pdf`;

    }

    function handleGenerate() {

        if (!isReady || generating) {

            return;

        }

        setGenerating(true);

        const scope =

            reportType === "application"
                ? applicationId
                : reportType === "department"
                    ? department
                    : null;

        const downloadFilename = buildDownloadFilename();

        fetch(`${API_BASE}/api/v1/reports/generate`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({

                report_type: reportType,

                scope

            })

        })

            .then((response) => {

                if (!response.ok) {

                    throw new Error("Failed to generate report.");

                }

                return response.blob();

            })

            .then((blob) => {

                const url = window.URL.createObjectURL(blob);

                const link = document.createElement("a");

                link.href = url;

                link.download = downloadFilename;

                document.body.appendChild(link);

                link.click();

                link.remove();

                window.URL.revokeObjectURL(url);

                loadHistory();

            })

            .catch((error) => {

                alert(error.message);

            })

            .finally(() => {

                setGenerating(false);

            });

    }

    function handleRedownload(report) {

        setDownloadingId(report.report_id);

        fetch(`${API_BASE}/api/v1/reports/download/${report.report_id}`)

            .then((response) => {

                if (!response.ok) {

                    throw new Error("Report file is no longer available.");

                }

                return response.blob();

            })

            .then((blob) => {

                const url = window.URL.createObjectURL(blob);

                const link = document.createElement("a");

                link.href = url;

                const scopeLabel = report.scope_name

                    ? slugify(report.scope_name)

                    : "Report";

                link.download =

                    `${report.report_type}_Report_${scopeLabel}.pdf`;

                document.body.appendChild(link);

                link.click();

                link.remove();

                window.URL.revokeObjectURL(url);

            })

            .catch((error) => {

                alert(error.message);

            })

            .finally(() => {

                setDownloadingId(null);

            });

    }

    function handleDelete(reportId) {

        if (!window.confirm(

            "Delete this report? This cannot be undone."

        )) {

            return;

        }

        setDeletingId(reportId);

        fetch(`${API_BASE}/api/v1/reports/${reportId}`, {

            method: "DELETE"

        })

            .then((response) => {

                if (!response.ok) {

                    throw new Error("Failed to delete report.");

                }

                setHistory((prev) =>

                    prev.filter((r) => r.report_id !== reportId)

                );

            })

            .catch((error) => {

                alert(error.message);

            })

            .finally(() => {

                setDeletingId(null);

            });

    }

    return (

        <div className="dashboard-layout">

            <Sidebar />

            <main className="dashboard-content">

                <div className="reports-header">

                    <h1>

                        <FaFileAlt />

                        Reports

                    </h1>

                    <p>

                        Generate a PDF security report for the whole
                        enterprise, a department, or a single
                        application - and revisit any report you have
                        generated before.

                    </p>

                </div>

                <div className="dashboard-card generate-report-card">

                    <h2>Generate New Report</h2>

                    <div className="report-type-tabs">

                        {

                            REPORT_TYPES.map(({ type, label, icon: Icon }) => (

                                <button

                                    key={type}

                                    className={

                                        reportType === type ? "active" : ""

                                    }

                                    onClick={() => handleTypeChange(type)}

                                >

                                    <Icon />

                                    {label}

                                </button>

                            ))

                        }

                    </div>

                    {

                        (reportType === "department" ||
                            reportType === "application") &&
                        meta && (

                            <div className="report-scope-row">

                                <div className="form-field">

                                    <label>Department</label>

                                    <select

                                        value={department}

                                        onChange={(e) => {

                                            setDepartment(e.target.value);

                                            setApplicationId("");

                                        }}

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

                                {

                                    reportType === "application" && (

                                        <div className="form-field">

                                            <label>Application</label>

                                            <select

                                                value={applicationId}

                                                onChange={(e) =>
                                                    setApplicationId(e.target.value)
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

                                                                value={app["Application ID"]}

                                                            >

                                                                {app["Application Name"]}

                                                            </option>

                                                        )

                                                    )

                                                }

                                            </select>

                                        </div>

                                    )

                                }

                            </div>

                        )

                    }

                    <button

                        className="generate-btn"

                        onClick={handleGenerate}

                        disabled={!isReady || generating}

                    >

                        {

                            generating ? (

                                <>
                                    <FaSpinner className="spin-icon" />
                                    Generating Report...
                                </>

                            ) : (

                                <>
                                    <FaDownload />
                                    Generate PDF Report
                                </>

                            )

                        }

                    </button>

                </div>

                <div className="dashboard-card report-history-card">

                    <h2>

                        <FaHistory />

                        Report History

                    </h2>

                    {

                        loadingHistory ? (

                            <div className="observations-loading">

                                Loading report history...

                            </div>

                        ) : history.length === 0 ? (

                            <p className="history-empty">

                                No reports generated yet. Reports you
                                create above will appear here.

                            </p>

                        ) : (

                            <div className="history-list">

                                {

                                    history.map((report) => (

                                        <div

                                            key={report.report_id}

                                            className="history-item"

                                        >

                                            <div className="history-item-info">

                                                <span

                                                    className={

                                                        `report-type-badge ` +
                                                        report.report_type

                                                    }

                                                >

                                                    {report.report_type}

                                                </span>

                                                <div>

                                                    <p className="history-label">

                                                        {report.label}

                                                    </p>

                                                    <p className="history-date">

                                                        {formatDate(report.generated_at)}

                                                    </p>

                                                </div>

                                            </div>

                                            <div className="history-item-actions">

                                                <button

                                                    className="redownload-btn"

                                                    onClick={() =>
                                                        handleRedownload(report)
                                                    }

                                                    disabled={
                                                        downloadingId === report.report_id
                                                    }

                                                >

                                                    {

                                                        downloadingId === report.report_id ? (

                                                            <FaSpinner className="spin-icon" />

                                                        ) : (

                                                            <FaDownload />

                                                        )

                                                    }

                                                    Download

                                                </button>

                                                <button

                                                    className="delete-btn"

                                                    onClick={() =>
                                                        handleDelete(report.report_id)
                                                    }

                                                    disabled={
                                                        deletingId === report.report_id
                                                    }

                                                    title="Delete report"

                                                >

                                                    {

                                                        deletingId === report.report_id ? (

                                                            <FaSpinner className="spin-icon" />

                                                        ) : (

                                                            <FaTrashAlt />

                                                        )

                                                    }

                                                </button>

                                            </div>

                                        </div>

                                    ))

                                }

                            </div>

                        )

                    }

                </div>

            </main>

        </div>

    );

}
