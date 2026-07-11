import "./ObservationFilters.css";

export default function ObservationFilters({

    search,
    setSearch,

    severity,
    setSeverity,

    activity,
    setActivity,

    department,
    setDepartment,

    applicationName,
    setApplicationName,

    activities,

    departments,

    applicationNames

}) {

    return (

        <div className="observation-filters">

            <input

                type="text"

                placeholder="Search Observation or ID..."

                value={search}

                onChange={(e) => setSearch(e.target.value)}

            />

            <select

                value={department}

                onChange={(e) => setDepartment(e.target.value)}

            >

                <option value="">

                    Department

                </option>

                {

                    departments.map((item) => (

                        <option

                            key={item}

                            value={item}

                        >

                            {item}

                        </option>

                    ))

                }

            </select>

            <select

                value={applicationName}

                onChange={(e) => setApplicationName(e.target.value)}

            >

                <option value="">

                    Application

                </option>

                {

                    applicationNames.map((item) => (

                        <option

                            key={item}

                            value={item}

                        >

                            {item}

                        </option>

                    ))

                }

            </select>

            <select

                value={activity}

                onChange={(e) => setActivity(e.target.value)}

            >

                <option value="">

                    Activity

                </option>

                {

                    activities.map((item) => (

                        <option

                            key={item}

                            value={item}

                        >

                            {item}

                        </option>

                    ))

                }

            </select>

            <select

                value={severity}

                onChange={(e) => setSeverity(e.target.value)}

            >

                <option value="">

                    Severity

                </option>

                <option value="High">

                    High

                </option>

                <option value="Medium">

                    Medium

                </option>

                <option value="Low">

                    Low

                </option>

            </select>

            

            

        </div>

    );

}