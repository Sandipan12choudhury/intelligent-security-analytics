import {
    ResponsiveContainer,
    PieChart,
    Pie,
    Cell,
    Tooltip
} from "recharts";

import "./SeverityDonut.css";

export default function SeverityDonut({ application }) {

    const data = [

        {
            name: "High",
            value: application["High Count"],
            color: "#ef4444"
        },

        {
            name: "Medium",
            value: application["Medium Count"],
            color: "#f59e0b"
        },

        {
            name: "Low",
            value: application["Low Count"],
            color: "#22c55e"
        }

    ];

    return (

        <div className="analytics-card">

            <h3>Severity Distribution</h3>

            <div className="severity-layout">

                <div className="severity-chart">

                    <ResponsiveContainer
                        width="100%"
                        height={260}
                    >

                        <PieChart>

                            <Pie
                                data={data}
                                innerRadius={60}
                                outerRadius={88}
                                paddingAngle={3}
                                dataKey="value"
                            >

                                {

                                    data.map((entry,index)=>(

                                        <Cell
                                            key={index}
                                            fill={entry.color}
                                        />

                                    ))

                                }

                            </Pie>

                            <Tooltip/>

                        </PieChart>

                    </ResponsiveContainer>

                    <div className="donut-center">

                        <h2>

                            {application["Total Observations"]}

                        </h2>

                        <span>Total</span>

                    </div>

                </div>

                <div className="severity-legend">

                    {

                        data.map((item)=>(

                            <div
                                key={item.name}
                                className="legend-row"
                            >

                                <div
                                    className="legend-color"
                                    style={{
                                        background:item.color
                                    }}
                                />

                                <div>

                                    <strong>

                                        {item.name}

                                    </strong>

                                    <p>

                                        {item.value}

                                        {" "}Observations

                                    </p>

                                </div>

                            </div>

                        ))

                    }

                </div>

            </div>

        </div>

    );

}