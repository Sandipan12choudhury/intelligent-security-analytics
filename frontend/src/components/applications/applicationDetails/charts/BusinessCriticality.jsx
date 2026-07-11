// BusinessCriticality.jsx
import "./BusinessCriticality.css";

const RADIUS = 90;
const CIRCUMFERENCE = 2 * Math.PI * RADIUS; // ≈ 565.48

const BANDS = [
    { label: "Low", max: 40, color: "#22c55e" },
    { label: "Medium", max: 60, color: "#f59e0b" },
    { label: "High", max: 80, color: "#f97316" },
    { label: "Critical", max: 100, color: "#ef4444" },
];

function getBand(score) {
    return BANDS.find((b) => score <= b.max) || BANDS[BANDS.length - 1];
}

export default function BusinessCriticality({ application }) {
    const riskScore = Number(application["Risk Score"] || 0);
    const totalObservations = Number(application["Total Observations"] || 0);
    const highCount = Number(application["High Count"] || 0);
    const priority = application["Executive Priority"] || "Medium";

    const priorityScore = { Critical: 100, High: 80, Medium: 60, Low: 40 }[priority] || 60;

    const highSeverityPercentage =
        totalObservations > 0 ? (highCount / totalObservations) * 100 : 0;

    // Normalize observations assuming ~25 is a busy application
    const observationDensity = Math.min((totalObservations / 25) * 100, 100);

    const rawScore = Math.round(
        riskScore * 0.4 +
            priorityScore * 0.25 +
            highSeverityPercentage * 0.2 +
            observationDensity * 0.15
    );

    const value = Math.min(Math.max(rawScore, 0), 100);
    const band = getBand(value);
    const offset = CIRCUMFERENCE - (CIRCUMFERENCE * value) / 100;

    return (
        <div className="business-criticality-card">
            <h3>Business Criticality</h3>

            <div className="criticality-circle">
                <svg viewBox="0 0 260 260">
                    <circle className="track" cx="130" cy="130" r={RADIUS} />
                    <circle
                        className="progress"
                        cx="130"
                        cy="130"
                        r={RADIUS}
                        style={{
                            stroke: band.color,
                            strokeDasharray: CIRCUMFERENCE,
                            strokeDashoffset: offset,
                        }}
                    />
                </svg>

                <div className="score-wrap">
                    <div className="score" style={{ color: band.color }}>
                        {value}
                    </div>
                    <div className="score-band" style={{ color: band.color }}>
                        {band.label}
                    </div>
                </div>
            </div>

            <p className="subtitle">Enterprise Criticality Score</p>

            <div className="legend">
                {BANDS.map((b) => (
                    <div className="legend-item" key={b.label}>
                        <span className="dot" style={{ background: b.color }} />
                        {b.label}
                    </div>
                ))}
            </div>

            <div className="footer-row">
                <span>
                    Priority: <strong>{priority}</strong>
                </span>
                <span>
                    Observations: <strong>{totalObservations}</strong>
                </span>
            </div>
        </div>
    );
}