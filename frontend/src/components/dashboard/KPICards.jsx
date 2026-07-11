import "./KPICards.css";

import {
    FaThLarge,
    FaBuilding,
    FaClipboardList,
    FaExclamationTriangle,
    FaShieldAlt,
    FaChartLine
} from "react-icons/fa";

export default function KPICards({ enterprise }) {

    const cards = [

        {
            title: "Applications",
            value: enterprise["Applications"],
            icon: <FaThLarge />,
            color: "#2563eb"
        },

        {
            title: "Departments",
            value: enterprise["Departments"],
            icon: <FaBuilding />,
            color: "#0891b2"
        },

        {
            title: "Observations",
            value: enterprise["Total Observations"],
            icon: <FaClipboardList />,
            color: "#7c3aed"
        },

        {
            title: "High Findings",
            value: enterprise["High Count"],
            icon: <FaExclamationTriangle />,
            color: "#dc2626"
        },

        {
            title: "Enterprise Risk",
            value: enterprise["Average Risk Score"],
            icon: <FaChartLine />,
            color: "#ea580c"
        },

        {
            title: "Compliance",
            value: enterprise["Average Compliance %"] + "%",
            icon: <FaShieldAlt />,
            color: "#16a34a"
        }

    ];

    return (

        <div className="kpi-grid">

            {

                cards.map((card, index) => (

                    <div
                        className="kpi-card"
                        key={index}
                    >

                        <div
                            className="kpi-icon"
                            style={{ background: card.color }}
                        >

                            {card.icon}

                        </div>

                        <div className="kpi-info">

                            <h3>{card.value}</h3>

                            <p>{card.title}</p>

                        </div>

                    </div>

                ))

            }

        </div>

    );

}