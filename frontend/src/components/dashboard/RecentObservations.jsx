import "./RecentObservations.css";

import { useNavigate } from "react-router-dom";

import {

    FaClipboardList,
    FaArrowRight,
    FaPlusCircle

} from "react-icons/fa";

function timeAgo(isoString) {

    const diffMs = Date.now() - new Date(isoString).getTime();

    const diffMinutes = Math.floor(diffMs / 60000);

    if (diffMinutes < 1) {

        return "just now";

    }

    if (diffMinutes < 60) {

        return `${diffMinutes} min ago`;

    }

    const diffHours = Math.floor(diffMinutes / 60);

    if (diffHours < 24) {

        return `${diffHours} hr ago`;

    }

    const diffDays = Math.floor(diffHours / 24);

    return `${diffDays} day${diffDays > 1 ? "s" : ""} ago`;

}

export default function RecentObservations({ recentObservations = [] }) {

    const navigate = useNavigate();

    const hasRecent = recentObservations && recentObservations.length > 0;

    return (

        <div className="dashboard-card recent-observations">

            <div className="recent-observations-header">

                <h2>Recent Observations</h2>

                {

                    hasRecent && (

                        <button

                            className="add-observation-link"

                            onClick={() => navigate("/observations/add")}

                        >

                            <FaPlusCircle />

                            Add New Observation

                        </button>

                    )

                }

            </div>

            {

                hasRecent ? (

                    <div className="recent-list">

                        {

                            recentObservations.map((item) => (

                                <div

                                    key={item["Observation ID"]}

                                    className="recent-item"

                                    onClick={() =>

                                        navigate("/observations", {

                                            state: {

                                                highlightId: item["Observation ID"]

                                            }

                                        })

                                    }

                                >

                                    <div className="recent-item-main">

                                        <span className="recent-item-id">

                                            {item["Observation ID"]}

                                        </span>

                                        <span

                                            className={

                                                `risk-badge ` +
                                                `${(item["Severity"] || "").toLowerCase()}`

                                            }

                                        >

                                            {item["Severity"]}

                                        </span>

                                        <span className="recent-item-time">

                                            {timeAgo(item["created_at"])}

                                        </span>

                                    </div>

                                    <p className="recent-item-text">

                                        {item["Observation"]}

                                    </p>

                                    <div className="recent-item-meta">

                                        {item["Application Name"]}

                                        {" • "}

                                        {item["Department"]}

                                        {" • "}

                                        {item["Activity"]}

                                    </div>

                                </div>

                            ))

                        }

                    </div>

                ) : (

                    <div className="empty-state">

                        <div className="empty-icon">

                            <FaClipboardList />

                        </div>

                        <h3>No Recent Observations</h3>

                        <p>

                            There are currently no user-generated security observations.

                            Newly submitted observations will automatically appear here
                            in chronological order after they are created by analysts.

                        </p>

                        <button

                            className="observations-btn"

                            onClick={() => navigate("/observations/add")}

                        >

                            Add New Observation

                            <FaArrowRight />

                        </button>

                    </div>

                )

            }

        </div>

    );

}
