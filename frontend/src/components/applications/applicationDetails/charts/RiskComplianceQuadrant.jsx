import "./RiskComplianceQuadrant.css";
import { useState } from "react";

export default function RiskComplianceQuadrant({ application }) {

    const compliance = Number(application["Compliance %"]);
    const risk = Number(application["Risk Score"]);
    const [showCard, setShowCard] = useState(false);

    const status =
        risk >= 50
            ? compliance >= 50
                ? "Needs Improvement"
                : "Critical"
            : compliance >= 50
                ? "Optimized"
                : "Stable";

    const pointX = 70 + (compliance / 100) * 630;
    const pointY = 330 - (risk / 100) * 260;

    return (

        <div className="quadrant-card">

            <h3>

                Risk vs Compliance Matrix

                <span className="info-icon">

                    ⓘ

                </span>

            </h3>

            <svg
                className="quadrant-chart"
                viewBox="0 0 760 390"
            >

                {/* ---------- Background Quadrants ---------- */}

                <rect
                    x="70"
                    y="20"
                    width="315"
                    height="130"
                    className="quad-critical"
                />

                <rect
                    x="385"
                    y="20"
                    width="315"
                    height="130"
                    className="quad-improve"
                />

                <rect
                    x="70"
                    y="150"
                    width="315"
                    height="180"
                    className="quad-stable"
                />

                <rect
                    x="385"
                    y="150"
                    width="315"
                    height="180"
                    className="quad-optimized"
                />

                {/* ---------- Grid ---------- */}

                {

                    [0, 25, 50, 75, 100].map((v) => (

                        <g key={v}>

                            <line

                                x1={70}

                                y1={330 - v * 2.6}

                                x2={700}

                                y2={330 - v * 2.6}

                                className="grid"

                            />

                            <line

                                x1={70 + v * 6.3}

                                y1={20}

                                x2={70 + v * 6.3}

                                y2={330}

                                className="grid"

                            />

                        </g>

                    ))

                }

                {/* Mid Lines */}

                <line
                    x1="385"
                    y1="20"
                    x2="385"
                    y2="330"
                    className="mid-line"
                />

                <line
                    x1="70"
                    y1="150"
                    x2="700"
                    y2="150"
                    className="mid-line"
                />

                {/* ---------- Axis ---------- */}

                <line
                    x1="70"
                    y1="330"
                    x2="705"
                    y2="330"
                    className="axis"
                />

                <line
                    x1="70"
                    y1="330"
                    x2="70"
                    y2="15"
                    className="axis"
                />

                {/* ---------- Arrow Heads ---------- */}

                <polygon
                    points="705,330 695,325 695,335"
                    className="axis-arrow"
                />

                <polygon
                    points="70,15 65,25 75,25"
                    className="axis-arrow"
                />

                {/* ---------- Axis Labels ---------- */}

                {

                    [0,25,50,75,100].map((v)=>(

                        <text

                            key={v}

                            x={40}

                            y={335-v*2.6}

                            className="tick"

                        >

                            {v}

                        </text>

                    ))

                }

                {

                    [0,25,50,75,100].map((v)=>(

                        <text

                            key={v}

                            x={65+v*6.3}

                            y="355"

                            className="tick"

                        >

                            {v}

                        </text>

                    ))

                }

                {/* ---------- Axis Titles ---------- */}

                <text

                    x="15"

                    y="185"

                    transform="rotate(-90 15 185)"

                    className="axis-title"

                >

                    Risk Score

                </text>

                <text

                    x="330"

                    y="382"

                    className="axis-title"

                >

                    Compliance %

                </text>

                {/* ---------- Quadrant Badges ---------- */}

                <g>

                    <rect
                        x="95"
                        y="40"
                        width="80"
                        height="28"
                        rx="8"
                        className="badge critical"
                    />

                    <text
                        x="135"
                        y="59"
                        textAnchor="middle"
                        className="badge-text critical-text"
                    >

                        Critical

                    </text>

                </g>

                <g>

                    <rect
                        x="520"
                        y="40"
                        width="150"
                        height="30"
                        rx="8"
                        className="badge improve"
                    />

                    <text
                        x="600"
                        y="60"
                        textAnchor="middle"
                        className="badge-text improve-text"
                    >

                        Needs Improvement

                    </text>

                </g>

                <g>

                    <rect
                        x="95"
                        y="285"
                        width="70"
                        height="28"
                        rx="8"
                        className="badge stable"
                    />

                    <text
                        x="130"
                        y="304"
                        textAnchor="middle"
                        className="badge-text stable-text"
                    >

                        Stable

                    </text>

                </g>

                <g>

                    <rect
                        x="590"
                        y="285"
                        width="90"
                        height="28"
                        rx="8"
                        className="badge optimized"
                    />

                    <text
                        x="635"
                        y="304"
                        textAnchor="middle"
                        className="badge-text optimized-text"
                    >

                        Optimized

                    </text>

                </g>

                {/* ---------- Point Glow ---------- */}

                <circle

                    cx={pointX}

                    cy={pointY}

                    r="12"

                    className="point-glow"

                />

                <circle

                    cx={pointX}

                    cy={pointY}

                    r="6"

                    className="point"

                    className="point"

                    onMouseEnter={() => setShowCard(true)}

                    onMouseLeave={() => setShowCard(false)}

                />

            </svg>

            {
    showCard && (

        <div
            className="info-card"
            style={{
                left: `${Math.min(compliance + 14, 62)}%`,
                top: `${Math.max(12, 100 - risk - 8)}%`
            }}
        >

            <h4>
                {application["Application ID"]}
            </h4>

            <p>
                Risk Score : <b>{risk}</b>
            </p>

            <p>
                Compliance : <b>{compliance}%</b>
            </p>

        </div>

    )
}

            <div className="quadrant-footer">

                <span>

                    🔵 {application["Application ID"]}

                </span>

                <span>

                    Risk : <b>{risk}</b>

                </span>

                <span>

                    Compliance : <b>{compliance}%</b>

                </span>

                <span>

                    Status :

                    <b className={`status ${status.toLowerCase().replace(/\s/g,"-")}`}>

                        {" "}{status}

                    </b>

                </span>

            </div>

        </div>

    );

}