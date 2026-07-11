import "./Sidebar.css";

import {
    FaShieldAlt,
    FaThLarge,
    FaSearch,
    FaPlusCircle,
    FaFileAlt,
    FaUserCircle,
    FaClipboardList,
    FaCog,
    FaSignOutAlt
} from "react-icons/fa";

import { NavLink, useNavigate } from "react-router-dom";

import { clearToken } from "/src/utils/auth";

export default function Sidebar() {

    const navigate = useNavigate();

    function handleLogout() {

        clearToken();

        navigate("/login", { replace: true });

    }

    return (

        <aside className="sidebar">

            <div className="sidebar-logo">

                <FaShieldAlt className="logo-icon" />

                <div>

                    <h2>Intelligent</h2>

                    <span>Security Analytics</span>

                </div>

            </div>

            <nav>

                <NavLink
                    to="/dashboard"
                    className={({ isActive }) => isActive ? "active" : ""}
                >
                    <FaThLarge />
                    Dashboard
                </NavLink>

                <NavLink
                    to="/applications"
                    className={({ isActive }) => isActive ? "active" : ""}
                >
                    <FaSearch />
                    Applications
                </NavLink>

                <NavLink
                    to="/observations"
                    end
                    className={({ isActive }) => isActive ? "active" : ""}
                >
                    <FaSearch />
                    Observations
                </NavLink>

                <NavLink
                    to="/observations/add"
                    className={({ isActive }) => isActive ? "active" : ""}
                >
                    <FaPlusCircle />
                    Add New Observation
                </NavLink>

                <NavLink
                    to="/reports"
                    className={({ isActive }) => isActive ? "active" : ""}
                >
                    <FaFileAlt />
                    Reports
                </NavLink>

                <NavLink
                    to="/profile"
                    className={({ isActive }) => isActive ? "active" : ""}
                >
                    <FaUserCircle />
                    Profile
                </NavLink>

                <NavLink
                    to="/logs"
                    className={({ isActive }) => isActive ? "active" : ""}
                >
                    <FaClipboardList />
                    Logs
                </NavLink>

                <NavLink
                    to="/settings"
                    className={({ isActive }) => isActive ? "active" : ""}
                >
                    <FaCog />
                    Settings
                </NavLink>

            </nav>

            <button className="logout-button" onClick={handleLogout}>

                <FaSignOutAlt />

                Logout

            </button>

        </aside>

    );

}
