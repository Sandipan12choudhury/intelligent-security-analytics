import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import Sidebar from "/src/components/dashboard/Sidebar";

import ApplicationHero from "/src/components/applications/applicationDetails/ApplicationHero";
import KPICards from "/src/components/applications/applicationDetails/KPICards";
import AnalyticsSection
from "/src/components/applications/applicationDetails/AnalyticsSection";
import "./ApplicationDetails.css";

import usePageTitle from "/src/utils/usePageTitle";

import API_BASE from "/src/config/api";

export default function ApplicationDetails() {

    const navigate = useNavigate();

    const { applicationId } = useParams();

    const [application, setApplication] = useState(null);

    const [loading, setLoading] = useState(true);

    usePageTitle(

        application ? application["Application Name"] : "Application"

    );

    useEffect(() => {

        fetch(

            `${API_BASE}/api/v1/applications/${applicationId}`

        )

        .then((response)=>response.json())

        .then((data)=>{

            setApplication(data.application);

            setLoading(false);

        })

        .catch(console.error);

    }, [applicationId]);

    if(loading){

        return (

            <div className="details-loading">

                Loading Application...

            </div>

        );

    }

    return(

        <div className="dashboard-layout">

            <Sidebar/>

            <main className="dashboard-content details-page">

                <div className="details-toolbar">

                    <button

                        className="back-btn"

                        onClick={()=>navigate("/applications")}

                    >

                        ← Back to Applications

                    </button>

                </div>

                <ApplicationHero

                    application={application}

                />

                <KPICards

                    application={application}

                />

                <AnalyticsSection
                    application={application}
                />

            </main>

        </div>

    );

}