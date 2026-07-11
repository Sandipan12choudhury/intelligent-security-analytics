import {
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    Cell
} from "recharts";

import "./ActivityBreakdown.css";

export default function ActivityBreakdown({ application }) {

    const data = [

        {
            activity: "ITGC",
            value: application["ITGC Count"]
        },

        {
            activity: "Database",
            value: application["Database Count"]
        },

        {
            activity: "DFRA",
            value: application["DFRA Count"]
        },

        {
            activity: "DFA",
            value: application["DFA Count"]
        },

        {
            activity: "SNA",
            value: application["SNA Count"]
        }

    ];

    const colors = [

        "#2563eb",
        "#3b82f6",
        "#60a5fa",
        "#93c5fd",
        "#bfdbfe"

    ];

    return (

        <div className="analytics-card">

            <h3>

                Activity Breakdown

            </h3>

            <ResponsiveContainer
                width="100%"
                height={320}
            >

                <BarChart
                    data={data}
                    layout="vertical"
                    margin={{
                        top: 10,
                        right: 20,
                        left: 20,
                        bottom: 10
                    }}
                >

                    <XAxis
                        type="number"
                        allowDecimals={false}
                    />

                    <YAxis
                        dataKey="activity"
                        type="category"
                        width={80}
                    />

                    <Tooltip/>

                    <Bar
                        dataKey="value"
                        radius={[0,8,8,0]}
                    >

                        {

                            data.map((entry,index)=>(

                                <Cell
                                    key={index}
                                    fill={colors[index]}
                                />

                            ))

                        }

                    </Bar>

                </BarChart>

            </ResponsiveContainer>

        </div>

    );

}