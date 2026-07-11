import "./ObservationHeader.css";

import {

    FaClipboardList

} from "react-icons/fa";

export default function ObservationHeader() {

    return (

        <div className="observation-header">

            <div>

                <h1>

                    <FaClipboardList />

                    Security Observations

                </h1>

                <p>

                    Browse enterprise security observations and use
                    AI to generate the likely impact, recommendation,
                    and supporting analysis for any observation.

                </p>

            </div>

        </div>

    );

}
