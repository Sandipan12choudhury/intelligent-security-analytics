import "./ApplicationHeader.css";

import {

    FaLayerGroup

} from "react-icons/fa";

export default function ApplicationHeader(){

    return(

        <div className="application-header">

            <div>

                <h1>

                    <FaLayerGroup />

                    Enterprise Applications

                </h1>

                <p>

                    Monitor enterprise applications,

                    assess cybersecurity posture,

                    review compliance,

                    and identify high-risk systems.

                </p>

            </div>

        </div>

    );

}