import { useState } from "react";

import "./ApplicationHero.css";

import {

    FaLayerGroup,
    FaDownload,
    FaSpinner

}

from "react-icons/fa";

import API_BASE from "/src/config/api";

export default function ApplicationHero({

    application

}){

    const [generating, setGenerating] = useState(false);

    function handleGenerateReport() {

        if (generating) {

            return;

        }

        setGenerating(true);

        fetch(`${API_BASE}/api/v1/reports/generate`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({

                report_type: "application",

                scope: application["Application ID"]

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

                const safeName = application["Application Name"]

                    .trim()

                    .replace(/[^a-zA-Z0-9]+/g, "_")

                    .replace(/^_+|_+$/g, "");

                link.download =
                    `${application["Application ID"]}_${safeName}_Report.pdf`;

                document.body.appendChild(link);

                link.click();

                link.remove();

                window.URL.revokeObjectURL(url);

            })

            .catch((error) => {

                alert(error.message);

            })

            .finally(() => {

                setGenerating(false);

            });

    }

    return(

        <div className="hero-card">

            <div className="hero-left">

                <div className="hero-icon">

                    <FaLayerGroup/>

                </div>

                <div>

                    <h1>

                        {application["Application ID"]}

                    </h1>

                    <h2>

                        {application["Application Name"]}

                    </h2>

                    <p>

                        {application.Department}

                    </p>

                </div>

            </div>

            <button

                className="report-btn"

                onClick={handleGenerateReport}

                disabled={generating}

            >

                {

                    generating ? (

                        <>
                            <FaSpinner className="spin-icon"/>
                            Generating...
                        </>

                    ) : (

                        <>
                            <FaDownload/>
                            Generate Report
                        </>

                    )

                }

            </button>

        </div>

    );

}
