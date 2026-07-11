import { useState } from "react";

import { useNavigate, Link } from "react-router-dom";

import "/src/pages/Login/Login.css";

import AuthLeftPanel from "/src/components/auth/AuthLeftPanel";

import {

    FaShieldAlt,
    FaUser,
    FaIdCard,
    FaEnvelope,
    FaPhone,
    FaLock,
    FaArrowRight,
    FaEye,
    FaEyeSlash,
    FaSpinner

} from "react-icons/fa";

import usePageTitle from "/src/utils/usePageTitle";

import API_BASE from "/src/config/api";

export default function Register() {

    usePageTitle("Create Account");

    const navigate = useNavigate();

    const [fullName, setFullName] = useState("");

    const [username, setUsername] = useState("");

    const [email, setEmail] = useState("");

    const [phone, setPhone] = useState("");

    const [password, setPassword] = useState("");

    const [confirmPassword, setConfirmPassword] = useState("");

    const [showPassword, setShowPassword] = useState(false);

    const [submitting, setSubmitting] = useState(false);

    const [error, setError] = useState("");

    function handleSubmit(e) {

        e.preventDefault();

        if (submitting) {

            return;

        }

        if (password.length < 8) {

            setError("Password must be at least 8 characters long.");

            return;

        }

        if (password !== confirmPassword) {

            setError("Passwords do not match.");

            return;

        }

        setSubmitting(true);

        setError("");

        fetch(`${API_BASE}/api/v1/auth/register`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({

                full_name: fullName,

                username,

                email,

                phone,

                password

            })

        })

            .then(async (response) => {

                const data = await response.json();

                if (!response.ok) {

                    throw new Error(data.detail || "Registration failed.");

                }

                return data;

            })

            .then((data) => {

                navigate("/verify-otp", {

                    state: {

                        otpSessionId: data.otp_session_id,

                        maskedPhone: data.masked_phone,

                        purpose: "register"

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

                        <h2>Create Account</h2>

                        <p>

                            Register to access the platform

                        </p>

                        <form onSubmit={handleSubmit}>

                            <label>Full Name</label>

                            <div className="input-box">

                                <FaIdCard/>

                                <input

                                    type="text"

                                    placeholder="Enter your full name"

                                    value={fullName}

                                    onChange={(e) => setFullName(e.target.value)}

                                />

                            </div>

                            <label>Username</label>

                            <div className="input-box">

                                <FaUser/>

                                <input

                                    type="text"

                                    placeholder="Choose a username"

                                    value={username}

                                    onChange={(e) => setUsername(e.target.value)}

                                />

                            </div>

                            <label>Email</label>

                            <div className="input-box">

                                <FaEnvelope/>

                                <input

                                    type="email"

                                    placeholder="Enter your email"

                                    value={email}

                                    onChange={(e) => setEmail(e.target.value)}

                                />

                            </div>

                            <label>Mobile Number</label>

                            <div className="input-box">

                                <FaPhone/>

                                <input

                                    type="tel"

                                    placeholder="e.g. +91 9876543210"

                                    value={phone}

                                    onChange={(e) => setPhone(e.target.value)}

                                />

                            </div>

                            <label>Password</label>

                            <div className="input-box">

                                <FaLock/>

                                <input

                                    type={showPassword ? "text" : "password"}

                                    placeholder="At least 8 characters"

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

                            <label>Confirm Password</label>

                            <div className="input-box">

                                <FaLock/>

                                <input

                                    type={showPassword ? "text" : "password"}

                                    placeholder="Re-enter your password"

                                    value={confirmPassword}

                                    onChange={(e) =>
                                        setConfirmPassword(e.target.value)
                                    }

                                />

                            </div>

                            {

                                error && (

                                    <div className="form-error">

                                        {error}

                                    </div>

                                )

                            }

                            <div className="options">

                                <span></span>

                                <Link to="/login">

                                    Already have an account? Sign in

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
                                            Creating Account...
                                        </>

                                    ) : (

                                        <>
                                            Create Account
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
