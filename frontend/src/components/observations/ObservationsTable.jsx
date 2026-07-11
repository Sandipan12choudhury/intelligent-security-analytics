import "./ObservationsTable.css";

import ObservationRow from "./ObservationRow";

import { FaTrashAlt } from "react-icons/fa";

export default function ObservationsTable({

    observations,

    totalObservations,

    clearFilters,

    onSelectObservation,

    selectedIds,

    onToggleSelect,

    onToggleSelectAll,

    onDeleteSelected,

    highlightId

}) {

    if (!observations || observations.length === 0) {

        return (

            <div className="dashboard-card">

                <h2>No Observations Found</h2>

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

    const allVisibleSelected =

        observations.length > 0 &&

        observations.every(

            (observation) => selectedIds.has(observation["Observation ID"])

        );

    return (

        <div className="dashboard-card">

            {

                selectedIds.size > 0 && (

                    <div className="bulk-delete-bar">

                        <span>

                            {selectedIds.size} observation
                            {selectedIds.size > 1 ? "s" : ""} selected

                        </span>

                        <button

                            className="bulk-delete-btn"

                            onClick={onDeleteSelected}

                        >

                            <FaTrashAlt />
                            Delete Selected

                        </button>

                    </div>

                )

            }

            <table className="observations-table">

                <thead>

                    <tr>

                        <th className="select-cell">

                            <input

                                type="checkbox"

                                checked={allVisibleSelected}

                                onChange={() =>
                                    onToggleSelectAll(observations)
                                }

                            />

                        </th>
                        <th>ID</th>
                        <th>Observation</th>
                        <th>Application</th>
                        <th>Activity</th>
                        <th>Severity</th>
                        <th></th>

                    </tr>

                </thead>

                <tbody>

                    {

                        observations.map((observation) => (

                            <ObservationRow

                                key={observation["Observation ID"]}

                                observation={observation}

                                onSelectObservation={onSelectObservation}

                                selected={

                                    selectedIds.has(observation["Observation ID"])

                                }

                                onToggleSelect={onToggleSelect}

                                highlighted={

                                    highlightId === observation["Observation ID"]

                                }

                            />

                        ))

                    }

                </tbody>

            </table>

            <div className="observations-footer">

                <p>

                    Showing

                    <strong> {observations.length} </strong>

                    of

                    <strong> {totalObservations} </strong>

                    Observations

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
