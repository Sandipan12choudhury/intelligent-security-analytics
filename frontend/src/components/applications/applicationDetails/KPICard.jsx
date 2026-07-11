import "./KPICard.css";

export default function KPICard({

    icon,
    title,
    value,
    subtitle,
    color

}){

    return(

        <div className="application-kpi-card">

            <div className={`application-kpi-icon ${color}`}>

                {icon}

            </div>

            <h4>

                {title}

            </h4>

            <h2 className={color}>

                {value}

            </h2>

            <span>

                {subtitle}

            </span>

        </div>

    );

}