import { useState } from "react";

import {

    FaTimes,
    FaRobot,
    FaFileCsv,
    FaFilePdf,
    FaFileWord,
    FaSpinner

} from "react-icons/fa";

import "./ObservationResultsModal.css";

import API_BASE from "/src/config/api";

// Artifact types shown as tabs, in the order they appear.
// "BUSINESS_IMPACT" is displayed to the user as "Likely Impact".

const ARTIFACT_TABS = [

    { type: "BUSINESS_IMPACT", label: "Likely Impact" },

    { type: "RECOMMENDATION", label: "Recommendation" },

    { type: "ROOT_CAUSE", label: "Root Cause" },

    { type: "RISK_JUSTIFICATION", label: "Risk Justification" },

    { type: "PREVENTIVE_CONTROL", label: "Preventive Controls" },

    { type: "EXECUTIVE_SUMMARY", label: "Executive Summary" }

];

export default function ObservationResultsModal({

    observation,

    onClose

}) {

    const [activeTab, setActiveTab] = useState(ARTIFACT_TABS[0].type);

    // results[type] = { loading, text, error }

    const [results, setResults] = useState({});

    const [exporting, setExporting] = useState(null);

    const current = results[activeTab];

    // ========================================================
    // Generate a single artifact
    // ========================================================

    function generateArtifact(artifactType) {

        setResults((prev) => ({

            ...prev,

            [artifactType]: {

                loading: true,

                text: prev[artifactType]?.text || "",

                error: null

            }

        }));

        fetch(`${API_BASE}/api/v1/artifacts/generate`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({

                observation_id: observation["Observation ID"],

                artifact_type: artifactType

            })

        })

            .then((response) => {

                if (!response.ok) {

                    return response.json().then((body) => {

                        throw new Error(

                            body.detail || "Failed to generate artifact."

                        );

                    });

                }

                return response.json();

            })

            .then((data) => {

                setResults((prev) => ({

                    ...prev,

                    [artifactType]: {

                        loading: false,

                        text: data.generated_text,

                        error: null

                    }

                }));

            })

            .catch((error) => {

                setResults((prev) => ({

                    ...prev,

                    [artifactType]: {

                        loading: false,

                        text: "",

                        error: error.message

                    }

                }));

            });

    }

    // ========================================================
    // Export
    // ========================================================

    function exportAs(fileFormat) {

        const artifacts = {};

        Object.keys(results).forEach((type) => {

            if (results[type]?.text) {

                artifacts[type] = results[type].text;

            }

        });

        if (Object.keys(artifacts).length === 0) {

            alert(

                "Generate at least one AI result before exporting."

            );

            return;

        }

        setExporting(fileFormat);

        fetch(`${API_BASE}/api/v1/export/${fileFormat}`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({

                observation_id: observation["Observation ID"],

                observation: observation["Observation"],

                severity: observation["Severity"],

                domain: observation["Domain"],

                activity: observation["Activity"],

                application_name: observation["Application Name"],

                department: observation["Department"],

                artifacts

            })

        })

            .then((response) => {

                if (!response.ok) {

                    throw new Error("Export failed.");

                }

                return response.blob();

            })

            .then((blob) => {

                const url = window.URL.createObjectURL(blob);

                const link = document.createElement("a");

                link.href = url;

                link.download =
                    `${observation["Observation ID"]}_ai_report.${fileFormat}`;

                document.body.appendChild(link);

                link.click();

                link.remove();

                window.URL.revokeObjectURL(url);

            })

            .catch((error) => {

                alert(error.message);

            })

            .finally(() => {

                setExporting(null);

            });

    }

    return (

        <div className="observation-modal-overlay" onClick={onClose}>

            <div

                className="observation-modal"

                onClick={(e) => e.stopPropagation()}

            >

                <div className="observation-modal-header">

                    <div>

                        <span className="observation-modal-id">

                            {observation["Observation ID"]}

                        </span>

                        <span

                            className={

                                `risk-badge ` +
                                `${(observation["Severity"] || "").toLowerCase()}`

                            }

                        >

                            {observation["Severity"]}

                        </span>

                    </div>

                    <button

                        className="observation-modal-close"

                        onClick={onClose}

                    >

                        <FaTimes />

                    </button>

                </div>

                <div className="observation-modal-meta">

                    <div>

                        <label>Application</label>

                        <p>{observation["Application Name"] || "-"}</p>

                    </div>

                    <div>

                        <label>Department</label>

                        <p>{observation["Department"] || "-"}</p>

                    </div>

                    <div>

                        <label>Domain</label>

                        <p>{observation["Domain"]}</p>

                    </div>

                    <div>

                        <label>Activity</label>

                        <p>{observation["Activity"]}</p>

                    </div>

                </div>

                <p className="observation-modal-text">

                    {observation["Observation"]}

                </p>

                <div className="observation-modal-tabs">

                    {

                        ARTIFACT_TABS.map((tab) => (

                            <button

                                key={tab.type}

                                className={

                                    activeTab === tab.type ? "active" : ""

                                }

                                onClick={() => setActiveTab(tab.type)}

                            >

                                {

                                    results[tab.type]?.text &&
                                    <span className="tab-dot" />

                                }

                                {tab.label}

                            </button>

                        ))

                    }

                </div>

                <div className="observation-modal-result">

                    {

                        !current || (!current.text && !current.loading && !current.error) ? (

                            <div className="result-empty">

                                <p>

                                    No AI result generated yet for this

                                    section.

                                </p>

                                <button

                                    className="generate-btn"

                                    onClick={() => generateArtifact(activeTab)}

                                >

                                    <FaRobot />

                                    Generate with AI

                                </button>

                            </div>

                        ) : current.loading ? (

                            <div className="result-loading">

                                <FaSpinner className="spin-icon" />

                                Generating AI response...

                            </div>

                        ) : current.error ? (

                            <div className="result-error">

                                <p>{current.error}</p>

                                <button

                                    className="generate-btn"

                                    onClick={() => generateArtifact(activeTab)}

                                >

                                    Try Again

                                </button>

                            </div>

                        ) : (

                            <>

                                <p className="result-text">

                                    {current.text}

                                </p>

                                <button

                                    className="regenerate-btn"

                                    onClick={() => generateArtifact(activeTab)}

                                >

                                    <FaRobot />

                                    Regenerate

                                </button>

                            </>

                        )

                    }

                </div>

                <div className="observation-modal-export">

                    <span>Export AI Report:</span>

                    <button

                        onClick={() => exportAs("csv")}

                        disabled={exporting !== null}

                    >

                        <FaFileCsv />

                        {exporting === "csv" ? "Exporting..." : "CSV"}

                    </button>

                    <button

                        onClick={() => exportAs("pdf")}

                        disabled={exporting !== null}

                    >

                        <FaFilePdf />

                        {exporting === "pdf" ? "Exporting..." : "PDF"}

                    </button>

                    <button

                        onClick={() => exportAs("docx")}

                        disabled={exporting !== null}

                    >

                        <FaFileWord />

                        {exporting === "docx" ? "Exporting..." : "Word"}

                    </button>

                </div>

            </div>

        </div>

    );

}
