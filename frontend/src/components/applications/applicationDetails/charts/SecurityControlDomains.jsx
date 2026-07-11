import {
    ResponsiveContainer,
    Treemap,
    Tooltip
} from "recharts";

import "./SecurityControlDomains.css";

export default function SecurityControlDomains({ application }) {

    const data = [

        {
            name: "Identity & Governance",
            size: Number(application["ITGC Count"] || 0)
        },

        {
            name: "Database Security",
            size: Number(application["Database Count"] || 0)
        },

        {
            name: "Digital Forensics",
            size: Number(application["DFRA Count"] || 0)
        },

        {
            name: "Data Protection",
            size: Number(application["DFA Count"] || 0)
        },

        {
            name: "Network Security",
            size: Number(application["SNA Count"] || 0)
        }

    ];

    const COLORS = [

        "#2563eb",
        "#16a34a",
        "#7c3aed",
        "#f59e0b",
        "#ef4444"

    ];

    return (

        <div className="analytics-card">

            <h3>

                Security Control Domains

            </h3>

            <ResponsiveContainer
                width="100%"
                height={260}
            >

                <Treemap
                    data={data}
                    dataKey="size"
                    stroke="#ffffff"
                    fill="#2563eb"
                    aspectRatio={4 / 3}
                >

                    <Tooltip />

                </Treemap>

            </ResponsiveContainer>

        </div>

    );

}