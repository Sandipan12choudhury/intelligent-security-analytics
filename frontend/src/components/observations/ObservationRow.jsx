import "./ObservationRow.css";

import { FaRobot } from "react-icons/fa";

export default function ObservationRow({

    observation,

    onSelectObservation,

    selected,

    onToggleSelect,

    highlighted

}) {

    const observationText = observation["Observation"] || "";

    const shortText =

        observationText.length > 110

            ? observationText.slice(0, 110) + "..."

            : observationText;

    const rowId = observation["Observation ID"];

    return (

        <tr

            id={`observation-row-${rowId}`}

            className={

                `observation-row ${highlighted ? "highlighted" : ""}`

            }

            onClick={() => onSelectObservation(observation)}

        >

            <td className="select-cell">

                <input

                    type="checkbox"

                    checked={selected}

                    onClick={(e) => e.stopPropagation()}

                    onChange={() => onToggleSelect(rowId)}

                />

            </td>

            <td>

                {rowId}

            </td>

            <td className="observation-text-cell">

                {shortText}

            </td>

            <td>

                {observation["Application Name"] || "-"}

            </td>

            <td>

                {observation["Activity"]}

            </td>

            <td>

                <span

                    className={

                        `risk-badge ${(observation["Severity"] || "").toLowerCase()}`

                    }

                >

                    {observation["Severity"]}

                </span>

            </td>

            <td>

                <button

                    className="view-btn"

                    onClick={(e) => {

                        e.stopPropagation();

                        onSelectObservation(observation);

                    }}

                >

                    <FaRobot />

                    Analyze

                </button>

            </td>

        </tr>

    );

}
