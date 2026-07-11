import { useEffect, useState, useCallback } from "react";

import Sidebar from "/src/components/dashboard/Sidebar";

import usePageTitle from "/src/utils/usePageTitle";

import { authHeaders } from "/src/utils/auth";

import API_BASE from "/src/config/api";

import {

    FaClipboardList,
    FaSync,
    FaServer,
    FaShieldAlt,
    FaDatabase,
    FaDownload

} from "react-icons/fa";

import "./Logs.css";

const CATEGORIES = [

    { key: "app", label: "Application", icon: FaServer },

    { key: "auth", label: "Security", icon: FaShieldAlt },

    { key: "data", label: "Data Events", icon: FaDatabase }

];

const LIVE_POLL_INTERVAL_MS = 5000;

function formatTimestamp(isoString) {

    return new Date(isoString).toLocaleString("en-IN", {

        day: "2-digit",

        month: "short",

        hour: "2-digit",

        minute: "2-digit",

        second: "2-digit"

    });

}

function levelClass(level) {

    const normalized = (level || "").toLowerCase();

    if (normalized === "warning") {

        return "log-level warning";

    }

    if (normalized === "error") {

        return "log-level error";

    }

    return "log-level info";

}

function entryMetaFields(entry) {

    return Object.entries(entry).filter(

        ([key]) => !["timestamp", "level", "message"].includes(key)

    );

}

export default function Logs() {

    usePageTitle("Logs");

    const [category, setCategory] = useState("app");

    const [entries, setEntries] = useState([]);

    const [loading, setLoading] = useState(true);

    const [live, setLive] = useState(false);

    const loadLogs = useCallback((selectedCategory) => {

        setLoading(true);

        fetch(`${API_BASE}/api/v1/logs/${selectedCategory}`, {

            headers: authHeaders()

        })

            .then((response) => response.json())

            .then((data) => {

                setEntries(data.entries || []);

                setLoading(false);

            })

            .catch(() => {

                setLoading(false);

            });

    }, []);

    useEffect(() => {

        loadLogs(category);

    }, [category, loadLogs]);

    useEffect(() => {

        if (!live) {

            return;

        }

        const interval = setInterval(() => {

            loadLogs(category);

        }, LIVE_POLL_INTERVAL_MS);

        return () => clearInterval(interval);

    }, [live, category, loadLogs]);

    function handleExport() {

        const categoryLabel =

            CATEGORIES.find((item) => item.key === category)?.label ||
            category;

        const header =

            `Intelligent Security Analytics Platform\n` +
            `${categoryLabel} Logs\n` +
            `Exported: ${new Date().toLocaleString()}\n` +
            `Total Entries: ${entries.length}\n` +
            `${"=".repeat(70)}\n\n`;

        const lines = entries.map((entry) => {

            const meta = entryMetaFields(entry)

                .map(([key, value]) => `${key}=${value}`)

                .join("  ");

            const timestamp = entry.timestamp
                ? formatTimestamp(entry.timestamp)
                : "";

            return (

                `[${timestamp}] ${entry.level || "INFO"}  ${entry.message}` +
                (meta ? `\n    ${meta}` : "")

            );

        });

        const content = header + lines.join("\n\n");

        const blob = new Blob([content], { type: "text/plain" });

        const url = window.URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        const dateStamp = new Date().toISOString().slice(0, 10);

        link.download = `${category}_logs_${dateStamp}.txt`;

        document.body.appendChild(link);

        link.click();

        link.remove();

        window.URL.revokeObjectURL(url);

    }

    return (

        <div className="dashboard-layout">

            <Sidebar />

            <main className="dashboard-content">

                <div className="logs-header">

                    <h1>

                        <FaClipboardList />

                        Logs

                    </h1>

                    <p>

                        Monitor application requests, security events,
                        and data changes as they happen.

                    </p>

                </div>

                <div className="dashboard-card logs-card">

                    <div className="logs-toolbar">

                        <div className="log-category-tabs">

                            {

                                CATEGORIES.map(({ key, label, icon: Icon }) => (

                                    <button

                                        key={key}

                                        className={category === key ? "active" : ""}

                                        onClick={() => setCategory(key)}

                                    >

                                        <Icon />
                                        {label}

                                    </button>

                                ))

                            }

                        </div>

                        <div className="logs-toolbar-actions">

                            <button

                                className={`live-toggle ${live ? "on" : ""}`}

                                onClick={() => setLive(!live)}

                                type="button"

                            >

                                <span className="live-toggle-track">

                                    <span className="live-toggle-thumb" />

                                </span>

                                Live

                            </button>

                            <button

                                className="toolbar-btn"

                                onClick={handleExport}

                                disabled={entries.length === 0}

                            >

                                <FaDownload />
                                Export .txt

                            </button>

                            <button

                                className="toolbar-btn primary"

                                onClick={() => loadLogs(category)}

                            >

                                <FaSync className={loading ? "spin-icon" : ""} />
                                Refresh

                            </button>

                        </div>

                    </div>

                    {

                        loading && entries.length === 0 ? (

                            <div className="observations-loading">

                                Loading logs...

                            </div>

                        ) : entries.length === 0 ? (

                            <p className="logs-empty">

                                No log entries yet. They'll appear
                                here as the application is used.

                            </p>

                        ) : (

                            <div className="log-list">

                                {

                                    entries.map((entry, index) => (

                                        <div key={index} className="log-entry">

                                            <div className="log-entry-top">

                                                <span className={levelClass(entry.level)}>

                                                    {entry.level || "INFO"}

                                                </span>

                                                <span className="log-timestamp">

                                                    {

                                                        entry.timestamp
                                                            ? formatTimestamp(entry.timestamp)
                                                            : ""

                                                    }

                                                </span>

                                            </div>

                                            <p className="log-message">

                                                {entry.message}

                                            </p>

                                            {

                                                entryMetaFields(entry).length > 0 && (

                                                    <div className="log-meta">

                                                        {

                                                            entryMetaFields(entry).map(

                                                                ([key, value]) => (

                                                                    <span key={key} className="log-meta-item">

                                                                        <strong>{key}:</strong> {String(value)}

                                                                    </span>

                                                                )

                                                            )

                                                        }

                                                    </div>

                                                )

                                            }

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
