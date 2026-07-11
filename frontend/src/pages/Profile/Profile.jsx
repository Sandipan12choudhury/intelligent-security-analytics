import { useEffect, useState } from "react";

import { useNavigate } from "react-router-dom";

import Sidebar from "/src/components/dashboard/Sidebar";

import { authHeaders, clearToken } from "/src/utils/auth";

import {

    FaUserCircle,
    FaEnvelope,
    FaPhone,
    FaUser,
    FaCalendarAlt,
    FaSignOutAlt

} from "react-icons/fa";

import "./Profile.css";

import usePageTitle from "/src/utils/usePageTitle";

import API_BASE from "/src/config/api";

function getInitials(fullName) {

    if (!fullName) {

        return "?";

    }

    const parts = fullName.trim().split(/\s+/);

    const initials = parts.slice(0, 2).map((p) => p[0].toUpperCase());

    return initials.join("");

}

function formatDate(isoString) {

    return new Date(isoString).toLocaleDateString("en-IN", {

        day: "2-digit",

        month: "long",

        year: "numeric"

    });

}

export default function Profile() {

    usePageTitle("My Profile");

    const navigate = useNavigate();

    const [profile, setProfile] = useState(null);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    useEffect(() => {

        fetch(`${API_BASE}/api/v1/auth/me`, {

            headers: authHeaders()

        })

            .then(async (response) => {

                if (response.status === 401) {

                    clearToken();

                    navigate("/login", { replace: true });

                    return null;

                }

                const data = await response.json();

                if (!response.ok) {

                    throw new Error(data.detail || "Could not load profile.");

                }

                return data;

            })

            .then((data) => {

                if (data) {

                    setProfile(data);

                }

                setLoading(false);

            })

            .catch((err) => {

                setError(err.message);

                setLoading(false);

            });

    }, [navigate]);

    function handleLogout() {

        clearToken();

        navigate("/login", { replace: true });

    }

    return (

        <div className="dashboard-layout">

            <Sidebar />

            <main className="dashboard-content">

                <div className="profile-header">

                    <h1>

                        <FaUserCircle />

                        My Profile

                    </h1>

                    <p>

                        Your account details for the Intelligent
                        Security Analytics Platform.

                    </p>

                </div>

                {

                    loading ? (

                        <div className="observations-loading">

                            Loading profile...

                        </div>

                    ) : error ? (

                        <div className="dashboard-card">

                            <p className="profile-error">{error}</p>

                        </div>

                    ) : (

                        <div className="dashboard-card profile-card">

                            <div className="profile-avatar-row">

                                <div className="profile-avatar">

                                    {getInitials(profile.full_name)}

                                </div>

                                <div>

                                    <h2>{profile.full_name}</h2>

                                    <p className="profile-username">

                                        @{profile.username}

                                    </p>

                                </div>

                            </div>

                            <div className="profile-details-grid">

                                <div className="profile-detail">

                                    <div className="profile-detail-icon">

                                        <FaUser />

                                    </div>

                                    <div>

                                        <label>Username</label>

                                        <p>{profile.username}</p>

                                    </div>

                                </div>

                                <div className="profile-detail">

                                    <div className="profile-detail-icon">

                                        <FaEnvelope />

                                    </div>

                                    <div>

                                        <label>Email Address</label>

                                        <p>{profile.email}</p>

                                    </div>

                                </div>

                                <div className="profile-detail">

                                    <div className="profile-detail-icon">

                                        <FaPhone />

                                    </div>

                                    <div>

                                        <label>Mobile Number</label>

                                        <p>{profile.phone}</p>

                                    </div>

                                </div>

                                <div className="profile-detail">

                                    <div className="profile-detail-icon">

                                        <FaCalendarAlt />

                                    </div>

                                    <div>

                                        <label>Member Since</label>

                                        <p>{formatDate(profile.member_since)}</p>

                                    </div>

                                </div>

                            </div>

                            <button

                                className="profile-logout-btn"

                                onClick={handleLogout}

                            >

                                <FaSignOutAlt />

                                Logout

                            </button>

                        </div>

                    )

                }

            </main>

        </div>

    );

}
