import { useEffect, useState } from "react";

import { useNavigate } from "react-router-dom";

import Sidebar from "/src/components/dashboard/Sidebar";

import SettingsOtpModal from "/src/components/auth/SettingsOtpModal";

import usePageTitle from "/src/utils/usePageTitle";

import { authHeaders, clearToken } from "/src/utils/auth";

import {

    FaCog,
    FaUserCircle,
    FaClock,
    FaCalendarAlt,
    FaCheckCircle,
    FaUser,
    FaLock,
    FaExclamationTriangle

} from "react-icons/fa";

import "./Settings.css";

import API_BASE from "/src/config/api";

function jsonFetch(url, options = {}) {

    return fetch(url, {

        ...options,

        headers: {

            "Content-Type": "application/json",

            ...authHeaders(),

            ...(options.headers || {})

        }

    }).then(async (response) => {

        const data = await response.json();

        if (!response.ok) {

            throw new Error(data.detail || "Something went wrong.");

        }

        return data;

    });

}

function formatDateTime(isoString) {

    if (!isoString) {

        return "Never";

    }

    return new Date(isoString).toLocaleString("en-IN", {

        day: "2-digit",

        month: "short",

        year: "numeric",

        hour: "2-digit",

        minute: "2-digit"

    });

}

export default function Settings() {

    usePageTitle("Settings");

    const navigate = useNavigate();

    const [profile, setProfile] = useState(null);

    // Change Username

    const [newUsername, setNewUsername] = useState("");

    const [usernameMessage, setUsernameMessage] = useState(null);

    const [usernameModal, setUsernameModal] = useState(null);

    // Change Password

    const [currentPassword, setCurrentPassword] = useState("");

    const [newPassword, setNewPassword] = useState("");

    const [confirmNewPassword, setConfirmNewPassword] = useState("");

    const [passwordMessage, setPasswordMessage] = useState(null);

    const [passwordModal, setPasswordModal] = useState(null);

    // Delete Account

    const [deletePassword, setDeletePassword] = useState("");

    const [deleteMessage, setDeleteMessage] = useState(null);

    const [deleteModal, setDeleteModal] = useState(null);

    useEffect(() => {

        jsonFetch(`${API_BASE}/api/v1/auth/me`)

            .then(setProfile)

            .catch((err) => console.error(err));

    }, []);

    // ============================================================
    // Change Username
    // ============================================================

    function handleRequestUsernameChange(e) {

        e.preventDefault();

        setUsernameMessage(null);

        if (!newUsername || newUsername.length < 3) {

            setUsernameMessage({

                type: "error",

                text: "Username must be at least 3 characters."

            });

            return;

        }

        jsonFetch(`${API_BASE}/api/v1/auth/request-username-change`, {

            method: "POST",

            body: JSON.stringify({ new_username: newUsername })

        })

            .then((data) => {

                setUsernameModal(data);

            })

            .catch((err) => {

                setUsernameMessage({ type: "error", text: err.message });

            });

    }

    function confirmUsernameChange(code) {

        return jsonFetch(`${API_BASE}/api/v1/auth/confirm-username-change`, {

            method: "POST",

            body: JSON.stringify({

                otp_session_id: usernameModal.otp_session_id,

                code

            })

        }).then((updatedProfile) => {

            setProfile(updatedProfile);

            setUsernameModal(null);

            setNewUsername("");

            setUsernameMessage({

                type: "success",

                text: "Username updated successfully."

            });

        });

    }

    // ============================================================
    // Change Password
    // ============================================================

    function handleRequestPasswordChange(e) {

        e.preventDefault();

        setPasswordMessage(null);

        if (newPassword.length < 8) {

            setPasswordMessage({

                type: "error",

                text: "New password must be at least 8 characters."

            });

            return;

        }

        if (newPassword !== confirmNewPassword) {

            setPasswordMessage({

                type: "error",

                text: "New passwords do not match."

            });

            return;

        }

        jsonFetch(`${API_BASE}/api/v1/auth/request-password-change`, {

            method: "POST",

            body: JSON.stringify({

                current_password: currentPassword,

                new_password: newPassword

            })

        })

            .then((data) => {

                setPasswordModal(data);

            })

            .catch((err) => {

                setPasswordMessage({ type: "error", text: err.message });

            });

    }

    function confirmPasswordChange(code) {

        return jsonFetch(`${API_BASE}/api/v1/auth/confirm-password-change`, {

            method: "POST",

            body: JSON.stringify({

                otp_session_id: passwordModal.otp_session_id,

                code

            })

        }).then(() => {

            setPasswordModal(null);

            setCurrentPassword("");

            setNewPassword("");

            setConfirmNewPassword("");

            setPasswordMessage({

                type: "success",

                text: "Password updated successfully."

            });

        });

    }

    // ============================================================
    // Delete Account
    // ============================================================

    function handleRequestAccountDeletion(e) {

        e.preventDefault();

        setDeleteMessage(null);

        if (!deletePassword) {

            setDeleteMessage({

                type: "error",

                text: "Enter your password to continue."

            });

            return;

        }

        jsonFetch(`${API_BASE}/api/v1/auth/request-account-deletion`, {

            method: "POST",

            body: JSON.stringify({ current_password: deletePassword })

        })

            .then((data) => {

                setDeleteModal(data);

            })

            .catch((err) => {

                setDeleteMessage({ type: "error", text: err.message });

            });

    }

    function confirmAccountDeletion(code) {

        return jsonFetch(`${API_BASE}/api/v1/auth/confirm-account-deletion`, {

            method: "POST",

            body: JSON.stringify({

                otp_session_id: deleteModal.otp_session_id,

                code

            })

        }).then(() => {

            clearToken();

            navigate("/login", { replace: true });

        });

    }

    return (

        <div className="dashboard-layout">

            <Sidebar />

            <main className="dashboard-content">

                <div className="settings-header">

                    <h1>

                        <FaCog />

                        Settings

                    </h1>

                    <p>

                        Manage your account details and security.

                    </p>

                </div>

                <div className="dashboard-card settings-card">

                    <h2>

                        <FaUserCircle style={{ marginRight: 10 }} />
                        Account Overview

                    </h2>

                    {

                        profile && (

                            <div className="account-overview-grid">

                                <div className="account-overview-item">

                                    <div className="account-overview-icon">

                                        <FaCalendarAlt />

                                    </div>

                                    <div>

                                        <label>Member Since</label>

                                        <p>{formatDateTime(profile.member_since)}</p>

                                    </div>

                                </div>

                                <div className="account-overview-item">

                                    <div className="account-overview-icon">

                                        <FaClock />

                                    </div>

                                    <div>

                                        <label>Last Login</label>

                                        <p>{formatDateTime(profile.last_login)}</p>

                                    </div>

                                </div>

                                <div className="account-overview-item">

                                    <div className="account-overview-icon success">

                                        <FaCheckCircle />

                                    </div>

                                    <div>

                                        <label>Account Status</label>

                                        <p>

                                            {

                                                profile.is_verified
                                                    ? "Verified"
                                                    : "Unverified"

                                            }

                                        </p>

                                    </div>

                                </div>

                            </div>

                        )

                    }

                </div>

                <div className="dashboard-card settings-card">

                    <h2>

                        <FaUser style={{ marginRight: 10 }} />
                        Change Username

                    </h2>

                    {

                        profile && (

                            <p className="settings-hint">

                                Current username: <strong>{profile.username}</strong>

                            </p>

                        )

                    }

                    <form onSubmit={handleRequestUsernameChange}>

                        <div className="settings-form-row">

                            <input

                                type="text"

                                placeholder="New username"

                                value={newUsername}

                                onChange={(e) => setNewUsername(e.target.value)}

                            />

                            <button type="submit" className="settings-action-btn">

                                Send Verification Code

                            </button>

                        </div>

                    </form>

                    {

                        usernameMessage && (

                            <div className={`settings-message ${usernameMessage.type}`}>

                                {

                                    usernameMessage.type === "success"
                                        ? <FaCheckCircle />
                                        : <FaExclamationTriangle />

                                }

                                {usernameMessage.text}

                            </div>

                        )

                    }

                </div>

                <div className="dashboard-card settings-card">

                    <h2>

                        <FaLock style={{ marginRight: 10 }} />
                        Change Password

                    </h2>

                    <form

                        onSubmit={handleRequestPasswordChange}

                        className="settings-password-form"

                    >

                        <input

                            type="password"

                            placeholder="Current password"

                            value={currentPassword}

                            onChange={(e) => setCurrentPassword(e.target.value)}

                        />

                        <input

                            type="password"

                            placeholder="New password (min. 8 characters)"

                            value={newPassword}

                            onChange={(e) => setNewPassword(e.target.value)}

                        />

                        <input

                            type="password"

                            placeholder="Confirm new password"

                            value={confirmNewPassword}

                            onChange={(e) => setConfirmNewPassword(e.target.value)}

                        />

                        <button type="submit" className="settings-action-btn">

                            Send Verification Code

                        </button>

                    </form>

                    {

                        passwordMessage && (

                            <div className={`settings-message ${passwordMessage.type}`}>

                                {

                                    passwordMessage.type === "success"
                                        ? <FaCheckCircle />
                                        : <FaExclamationTriangle />

                                }

                                {passwordMessage.text}

                            </div>

                        )

                    }

                </div>

                <div className="dashboard-card settings-card danger-zone">

                    <h2>

                        <FaExclamationTriangle style={{ marginRight: 10 }} />
                        Delete Account

                    </h2>

                    <p className="settings-hint">

                        This permanently deletes your account and
                        cannot be undone.

                    </p>

                    <form

                        onSubmit={handleRequestAccountDeletion}

                        className="settings-form-row"

                    >

                        <input

                            type="password"

                            placeholder="Enter your password to confirm"

                            value={deletePassword}

                            onChange={(e) => setDeletePassword(e.target.value)}

                        />

                        <button type="submit" className="settings-delete-btn">

                            Delete My Account

                        </button>

                    </form>

                    {

                        deleteMessage && (

                            <div className={`settings-message ${deleteMessage.type}`}>

                                <FaExclamationTriangle />
                                {deleteMessage.text}

                            </div>

                        )

                    }

                </div>

            </main>

            {

                usernameModal && (

                    <SettingsOtpModal

                        title="Confirm Username Change"

                        otpSessionId={usernameModal.otp_session_id}

                        maskedPhone={usernameModal.masked_phone}

                        maskedEmail={usernameModal.masked_email}

                        onConfirm={confirmUsernameChange}

                        onClose={() => setUsernameModal(null)}

                    />

                )

            }

            {

                passwordModal && (

                    <SettingsOtpModal

                        title="Confirm Password Change"

                        otpSessionId={passwordModal.otp_session_id}

                        maskedPhone={passwordModal.masked_phone}

                        maskedEmail={passwordModal.masked_email}

                        onConfirm={confirmPasswordChange}

                        onClose={() => setPasswordModal(null)}

                    />

                )

            }

            {

                deleteModal && (

                    <SettingsOtpModal

                        title="Confirm Account Deletion"

                        otpSessionId={deleteModal.otp_session_id}

                        maskedPhone={deleteModal.masked_phone}

                        maskedEmail={deleteModal.masked_email}

                        onConfirm={confirmAccountDeletion}

                        onClose={() => setDeleteModal(null)}

                    />

                )

            }

        </div>

    );

}
