import "./ActivityAnalytics.css";

import {
    FaShieldAlt,
    FaDatabase,
    FaSearch,
    FaFingerprint,
    FaNetworkWired,
    FaClipboardCheck
} from "react-icons/fa";

const icons = {

    ITGC: <FaShieldAlt />,
    Database: <FaDatabase />,
    DFRA: <FaSearch />,
    "DFA / DFD": <FaClipboardCheck />,
    SNA: <FaNetworkWired />

};

export default function ActivityAnalytics({ activities }) {

    if (!activities || activities.length === 0) {

        return (

            <div className="dashboard-card">

                <h2>Activity Analytics</h2>

                <p>No activity data available.</p>

            </div>

        );

    }

    return (

        <div className="dashboard-card">

            <h2>Activity Analytics</h2>

            <div className="activity-grid">

                {activities.map((activity) => (

                    <div
                        className="activity-card"
                        key={activity.Activity}
                    >

                        <div className="activity-icon">

                            {icons[activity.Activity]}

                        </div>

                        <h3>{activity.Activity}</h3>

                        <h1>{activity["Total Observations"]}</h1>

                        <span>Observations</span>

                    </div>

                ))}

            </div>

        </div>

    );

}