import "./ExecutiveSummary.css";
import {

    FaChartLine,
    FaShieldAlt,
    FaExclamationTriangle,
    FaBuilding,
    FaProjectDiagram,
    FaFire,
    FaLightbulb

} from "react-icons/fa";
export default function ExecutiveSummary({ enterprise }) {

    if (!enterprise) {

        return (

            <div className="dashboard-card">

                <h2>Executive Summary</h2>

                <p>No enterprise analytics available.</p>

            </div>

        );

    }

    // =========================================================================
    // Dynamic Activity Observation Count
    // =========================================================================

    const activityCountMap = {

        "ITGC": enterprise["ITGC Count"],
        "Database": enterprise["Database Count"],
        "DFRA": enterprise["DFRA Count"],
        "DFA / DFD": enterprise["DFA Count"],
        "SNA": enterprise["SNA Count"]

    };

    const topActivityCount =
        activityCountMap[enterprise["Top Activity"]] ?? 0;

    return (

        <div className="dashboard-card executive-summary">

            <h2>Executive Summary</h2>

            {/* =============================================================== */}
            {/* Enterprise Health */}
            {/* =============================================================== */}

            <section className="summary-section">

                <h3>
                    <FaShieldAlt />
                    Enterprise Health
                </h3>

                <div className="summary-list">

                    <div className="summary-row">

                        <div className="summary-label">
                            <FaChartLine />
                            <span>Risk Score</span>
                        </div>

                        <strong>{enterprise["Average Risk Score"]}</strong>

                    </div>

                    <div className="summary-row">

                        <div className="summary-label">
                            <FaShieldAlt />
                            <span>Compliance</span>
                        </div>

                        <strong>

                            {enterprise["Average Compliance %"]}%

                        </strong>

                    </div>

                    <div className="summary-row">

                        <div className="summary-label">
                            <FaExclamationTriangle />
                            <span>Risk Category</span>
                        </div>

                        <span className="risk-pill">

                            {enterprise["Risk Category"]}

                        </span>

                    </div>

                </div>

            </section>

            {/* =============================================================== */}
            {/* Key Insights */}
            {/* =============================================================== */}

            <section className="summary-section">

                <h3>
                    <FaExclamationTriangle />
                    Key Insights
                </h3>

                <ul className="insight-list">

    <li>

        <div className="insight-title">

            <FaBuilding />

            <strong>Highest Risk Department</strong>

        </div>

        <span>

            {enterprise["Highest Risk Department"]}

        </span>

    </li>

    <li>

        <div className="insight-title">

            <FaProjectDiagram />

            <strong>Highest Risk Activity</strong>

        </div>

        <span>

            {enterprise["Top Activity"]} ({topActivityCount} Observations)

        </span>

    </li>

    <li>

        <div className="insight-title">

            <FaFire />

            <strong>Highest Severity</strong>

        </div>

        <span>

            {enterprise["Dominant Severity"]} ({enterprise["Medium Count"]} Observations)

        </span>

    </li>

</ul>

            </section>

            {/* =============================================================== */}
            {/* Priority Action */}
            {/* =============================================================== */}

            <section className="summary-section priority-section">

                <h3>
                    <FaLightbulb />
                    Priority Action
                </h3>

                <p>

                    Prioritize remediation of
                    <strong> {enterprise["Top Activity"]}</strong>
                    {" "}findings within
                    <strong> {enterprise["Highest Risk Department"]}</strong>.
                    Focus on reducing high-severity observations to improve the
                    enterprise risk posture and increase overall compliance
                    across business-critical applications.

                </p>

            </section>

        </div>

    );

}