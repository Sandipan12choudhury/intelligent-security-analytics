import "./AnalyticsSection.css";

import SeverityDonut from "./charts/SeverityDonut";
import ActivityBreakdown from "./charts/ActivityBreakdown";
import RiskComplianceQuadrant from "./charts/RiskComplianceQuadrant";
import BusinessCriticality from "./charts/BusinessCriticality";

export default function AnalyticsSection({ application }) {

    return (

        <section className="analytics-section">

            <h2>

                Security Analytics

            </h2>

            <p>

                Visual representation of the application's security posture.

            </p>

            <div className="analytics-grid">

                <SeverityDonut
                    application={application}
                />

                <ActivityBreakdown
                    application={application}
                />

                <RiskComplianceQuadrant
                    application={application}
                />

                <BusinessCriticality
                    application={application}
                />

            </div>

        </section>

    );

}