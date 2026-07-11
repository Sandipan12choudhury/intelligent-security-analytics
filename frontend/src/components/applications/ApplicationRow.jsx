import "./ApplicationRow.css";

import { FaArrowRight } from "react-icons/fa";

import { useNavigate } from "react-router-dom";

export default function ApplicationRow({ application }) {

    const navigate = useNavigate();

    return (

        <tr>

            <td>

                {application["Application ID"]}

            </td>

            <td>

                <strong>

                    {application["Application Name"]}

                </strong>

            </td>

            <td>

                {application.Department}

            </td>

            <td>

                <span
                    className={`risk-badge ${application["Risk Category"].toLowerCase()}`}
                >

                    {application["Risk Category"]}

                </span>

            </td>

            <td>

                <div className="progress">

                    <div
                        className="progress-fill"
                        style={{
                            width: `${application["Compliance %"]}%`
                        }}
                    />

                </div>

                <span>

                    {application["Compliance %"]}%

                </span>

            </td>

            <td>

                {application["Executive Priority"]}

            </td>

            <td>

                {application["Total Observations"]}

            </td>

            <td>

                <button

                    className="view-btn"

                    onClick={() =>

                        navigate(

                            `/applications/${application["Application ID"]}`

                        )

                    }

                >

                    View

                    <FaArrowRight />

                </button>

            </td>

        </tr>

    );

}