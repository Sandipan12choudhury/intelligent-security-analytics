import "./ApplicationsTable.css";

import ApplicationRow from "./ApplicationRow";

export default function ApplicationsTable({

    applications,

    totalApplications,

    clearFilters

}) {

    if (!applications || applications.length === 0) {

        return (

            <div className="dashboard-card">

                <h2>No Applications Found</h2>

                <p className="empty-results-message">
                

                    Try changing or clearing the applied filters.

                </p>

                <button

                    className="clear-filters-btn"

                    onClick={clearFilters}

                >

                    Clear All Filters

                </button>

            </div>

        );

    }

    return (

        <div className="dashboard-card">

            <table className="applications-table">

                <thead>

                    <tr>

                        <th>ID</th>
                        <th>Application</th>
                        <th>Department</th>
                        <th>Risk</th>
                        <th>Compliance</th>
                        <th>Priority</th>
                        <th>Observations</th>
                        <th></th>

                    </tr>

                </thead>

                <tbody>

                    {

                        applications.map((application) => (

                            <ApplicationRow

                                key={application["Application ID"]}

                                application={application}

                            />

                        ))

                    }

                </tbody>

            </table>

            {/* ===================================================== */}

            <div className="applications-footer">

                <p>

                    Showing

                    <strong> {applications.length} </strong>

                    of

                    <strong> {totalApplications} </strong>

                    Applications

                </p>

                <button

                    className="clear-filters-btn"

                    onClick={clearFilters}

                >

                    Clear All Filters

                </button>

            </div>

        </div>

    );

}