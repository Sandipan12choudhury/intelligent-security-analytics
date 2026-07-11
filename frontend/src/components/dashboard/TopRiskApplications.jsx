import "./TopRiskApplications.css";

export default function TopRiskApplications({ applications }) {

    if (!applications || applications.length === 0) {

        return (

            <div className="dashboard-card">

                <h2>Top Risk Applications</h2>

                <p>No application analytics available.</p>

            </div>

        );

    }

    const topApplications = [...applications]

        .sort((a, b) => a["Risk Rank"] - b["Risk Rank"])

        .slice(0, 10);

    return (

        <div className="dashboard-card">

            <h2>Top Risk Applications</h2>

            <table className="dashboard-table">

                <thead>

                    <tr>

                        <th>Rank</th>
                        <th>Application</th>
                        <th>Department</th>
                        <th>Risk Score</th>
                        <th>Risk</th>
                        <th>Compliance</th>
                        <th>Observations</th>

                    </tr>

                </thead>

                <tbody>

                    {topApplications.map((application) => (

                        <tr key={application["Application ID"]}>

                            <td>{application["Risk Rank"]}</td>

                            <td>{application["Application Name"]}</td>

                            <td>{application["Department"]}</td>

                            <td>{application["Risk Score"]}</td>

                            <td>

                                <span
                                    className={`risk-badge ${application["Risk Category"].toLowerCase()}`}
                                >

                                    {application["Risk Category"]}

                                </span>

                            </td>

                            <td>

                                {application["Compliance %"]}%

                            </td>

                            <td>

                                {application["Total Observations"]}

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}