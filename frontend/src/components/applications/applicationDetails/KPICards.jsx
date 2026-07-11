import {

    FaShieldAlt,
    FaCheckCircle,
    FaExclamationTriangle,
    FaUserShield,
    FaClipboardList

}

from "react-icons/fa";

import KPICard from "./KPICard";

import "./KPICards.css";

export default function KPICards({

    application

}){

    return(

        <div className="application-kpi-grid">

            <KPICard

                icon={<FaShieldAlt/>}

                title="Risk Score"

                value={`${application["Risk Score"]}/100`}

                subtitle="Overall Risk"

                color="red"

            />

            <KPICard

                icon={<FaCheckCircle/>}

                title="Compliance"

                value={`${application["Compliance %"]}%`}

                subtitle="Current Compliance"

                color="green"

            />

            <KPICard

                icon={<FaExclamationTriangle/>}

                title="Risk Category"

                value={application["Risk Category"]}

                subtitle="Enterprise Risk"

                color="orange"

            />

            <KPICard

                icon={<FaUserShield/>}

                title="Executive Priority"

                value={application["Executive Priority"]}

                subtitle="Business Priority"

                color="purple"

            />

            <KPICard

                icon={<FaClipboardList/>}

                title="Total Observations"

                value={application["Total Observations"]}

                subtitle="Across Activities"

                color="blue"

            />

        </div>

    );

}