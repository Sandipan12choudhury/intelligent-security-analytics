import "./ApplicationFilters.css";

export default function ApplicationFilters({

    search,
    setSearch,

    department,
    setDepartment,

    risk,
    setRisk,

    priority,
    setPriority,

    departments

}) {

    return (

        <div className="application-filters">

            <input

                type="text"

                placeholder="Search Application..."

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

                value={risk}

                onChange={(e) => setRisk(e.target.value)}

            >

                <option value="">

                    Risk

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

            <select

                value={priority}

                onChange={(e) => setPriority(e.target.value)}

            >

                <option value="">

                    Priority

                </option>

                <option value="Critical">

                    Critical

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