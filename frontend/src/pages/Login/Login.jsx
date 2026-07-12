import { useState } from "react";

import { useNavigate, Link } from "react-router-dom";

import "./Login.css";

import AuthLeftPanel from "/src/components/auth/AuthLeftPanel";

import {

    FaShieldAlt,
    FaUser,
    FaLock,
    FaArrowRight,
    FaEye,
    FaEyeSlash,
    FaSpinner

} from "react-icons/fa";

import usePageTitle from "/src/utils/usePageTitle";

import API_BASE from "/src/config/api";

export default function Login() {

    usePageTitle("Sign In");

    const navigate = useNavigate();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    const [showPassword, setShowPassword] = useState(false);

    const [submitting, setSubmitting] = useState(false);

    const [error, setError] = useState("");

    function handleSubmit(e) {

        e.preventDefault();

        if (!username || !password || submitting) {

            return;

        }

        setSubmitting(true);

        setError("");

        fetch(`${API_BASE}/api/v1/auth/login`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({ username, password })

        })

            .then(async (response) => {

                const data = await response.json();

                if (!response.ok) {

                    throw new Error(data.detail || "Login failed.");

                }

                return data;

            })

            .then((data) => {

                navigate("/verify-otp", {

                    state: {

                        otpSessionId: data.otp_session_id,

                        maskedPhone: data.masked_phone,
                        maskedEmail: data.masked_email,

                        purpose: "login"

                    }

                });

            })

            .catch((err) => {

                setError(err.message);

            })

            .finally(() => {

                setSubmitting(false);

            });

    }

    return (

        <div className="login-page">

            <div className="login-container">

                <AuthLeftPanel />

                <div className="right-panel">

                    <div className="login-card">

                        <FaShieldAlt className="top-icon"/>

                        <h2>Welcome Back</h2>

                        <p>

                            Sign in to continue to your dashboard

                        </p>

                        <form onSubmit={handleSubmit}>

                            <label>

                                Username

                            </label>

                            <div className="input-box">

                                <FaUser/>

                                <input

                                    type="text"

                                    placeholder="Enter your username"

                                    value={username}

                                    onChange={(e) => setUsername(e.target.value)}

                                />

                            </div>

                            <label>

                                Password

                            </label>

                            <div className="input-box">

                                <FaLock/>

                                <input

                                    type={showPassword ? "text" : "password"}

                                    placeholder="Enter your password"

                                    value={password}

                                    onChange={(e) => setPassword(e.target.value)}

                                />

                                {

                                    showPassword ? (

                                        <FaEyeSlash

                                            onClick={() => setShowPassword(false)}

                                            style={{ cursor: "pointer" }}

                                        />

                                    ) : (

                                        <FaEye

                                            onClick={() => setShowPassword(true)}

                                            style={{ cursor: "pointer" }}

                                        />

                                    )

                                }

                            </div>

                            {

                                error && (

                                    <div className="form-error">

                                        {error}

                                    </div>

                                )

                            }

                            <div className="options">

                                <Link to="/forgot-password">

                                    Forgot Password?

                                </Link>

                                <Link to="/register">

                                    New here? Create an account

                                </Link>

                            </div>

                            <button

                                type="submit"

                                className="login-button"

                                disabled={submitting}

                            >

                                {

                                    submitting ? (

                                        <>
                                            <FaSpinner className="spin-icon"/>
                                            Signing In...
                                        </>

                                    ) : (

                                        <>
                                            Sign In
                                            <FaArrowRight/>
                                        </>

                                    )

                                }

                            </button>

                        </form>

                        <div className="developer">
                            <div className="inspired-text">
                                Inspired by SBI Global IT Centre CSR 2025–26 Project
                            </div>
                            <div className="developed-by">
                                Developed by <strong>Sandipan Choudhury</strong>
                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    );

}
