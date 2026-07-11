import heroImage from "/src/assets/images/hero.png";

import {

    FaShieldAlt,
    FaChartLine,
    FaClipboardList,
    FaSearch,
    FaChartPie,
    FaFileAlt,
    FaUniversity

} from "react-icons/fa";

export default function AuthLeftPanel() {

    return (

        <div

            className="left-panel"

            style={{

                backgroundImage: `
                    linear-gradient(
                        rgba(7,20,45,.58),
                        rgba(7,20,45,.74)
                    ),
                    url(${heroImage})
                `,

                backgroundSize: "cover",

                backgroundPosition: "center",

                backgroundRepeat: "no-repeat"

            }}

        >

            <div className="overlay"></div>

            <div className="left-content">

                <div className="logo-row">

                    <FaShieldAlt className="shield"/>

                    <h1>

                        Intelligent Security
                        <br/>
                        Analytics Platform

                    </h1>

                </div>

                <p className="subtitle">

                    Enterprise Platform for Security Assessment,
                    Risk Intelligence & Compliance Analytics

                </p>

                <div className="feature-grid">

                    <div className="feature-card">
                        <FaChartLine/>
                        <span>Risk Analytics</span>
                    </div>

                    <div className="feature-card">
                        <FaShieldAlt/>
                        <span>Compliance Monitoring</span>
                    </div>

                    <div className="feature-card">
                        <FaSearch/>
                        <span>Observation Explorer</span>
                    </div>

                    <div className="feature-card">
                        <FaChartPie/>
                        <span>Interactive Dashboards</span>
                    </div>

                    <div className="feature-card">
                        <FaFileAlt/>
                        <span>Automated Reports</span>
                    </div>

                    <div className="feature-card">
                        <FaClipboardList/>
                        <span>Enterprise Intelligence</span>
                    </div>

                </div>

                <div className="footer-note">

                    <FaUniversity/>

                    <span>

                        Security Assessment • Compliance Analytics • Risk Intelligence

                    </span>

                </div>

                <div className="analytics-tag">
                    Transforming Data into Insights.
                </div>

            </div>

        </div>

    );

}
