import "./DepartmentalAnalytics.css";

export default function DepartmentalAnalytics({ departments }) {

    if (!departments || departments.length === 0) {

        return (
            <div className="dashboard-card">
                <h2>Department Analytics</h2>
                <p>No department data available.</p>
            </div>
        );

    }

    return (

        <div className="dashboard-card">

            <h2>Department Analytics</h2>

            <table className="department-table">

                <thead>

                    <tr>

                        <th>Department</th>

                        <th>Applications</th>

                        <th>Observations</th>

                        <th>Risk Score</th>

                        <th>Compliance</th>

                        <th>Risk</th>

                    </tr>

                </thead>

                <tbody>

                    {departments.map((department) => (

                        <tr key={department.Department}>

                            <td>{department.Department}</td>

                            <td>{department.Applications}</td>

                            <td>{department["Total Observations"]}</td>

                            <td>{department["Average Risk Score"]}</td>

                            <td>{department["Average Compliance %"]}%</td>

                            <td>

                                <span
                                    className={`risk-badge ${department["Risk Category"].toLowerCase()}`}
                                >
                                    {department["Risk Category"]}
                                </span>

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}