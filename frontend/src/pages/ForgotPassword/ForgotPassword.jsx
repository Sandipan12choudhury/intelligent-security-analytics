import { useState } from "react";

import { useNavigate, Link } from "react-router-dom";

import "/src/pages/Login/Login.css";

import AuthLeftPanel from "/src/components/auth/AuthLeftPanel";

import usePageTitle from "/src/utils/usePageTitle";

import {

    FaShieldAlt,
    FaUser,
    FaArrowRight,
    FaSpinner

} from "react-icons/fa";

import API_BASE from "/src/config/api";

export default function ForgotPassword() {

    usePageTitle("Forgot Password");

    const navigate = useNavigate();

    const [identifier, setIdentifier] = useState("");

    const [submitting, setSubmitting] = useState(false);

    const [error, setError] = useState("");

    function handleSubmit(e) {

        e.preventDefault();

        if (!identifier || submitting) {

            return;

        }

        setSubmitting(true);

        setError("");

        fetch(`${API_BASE}/api/v1/auth/forgot-password`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({ identifier })

        })

            .then(async (response) => {

                const data = await response.json();

                if (!response.ok) {

                    throw new Error(

                        data.detail || "Could not start password reset."

                    );

                }

                return data;

            })

            .then((data) => {

                navigate("/reset-password", {

                    state: {

                        otpSessionId: data.otp_session_id,

                        maskedPhone: data.masked_phone,

                        maskedEmail: data.masked_email

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

                        <h2>Forgot Password</h2>

                        <p>

                            Enter your username or email and we'll
                            send you a verification code

                        </p>

                        <form onSubmit={handleSubmit}>

                            <label>Username or Email</label>

                            <div className="input-box">

                                <FaUser/>

                                <input

                                    type="text"

                                    placeholder="Enter your username or email"

                                    value={identifier}

                                    onChange={(e) => setIdentifier(e.target.value)}

                                />

                            </div>

                            {

                                error && (

                                    <div className="form-error">

                                        {error}

                                    </div>

                                )

                            }

                            <button

                                type="submit"

                                className="login-button"

                                disabled={submitting}

                            >

                                {

                                    submitting ? (

                                        <>
                                            <FaSpinner className="spin-icon"/>
                                            Sending Code...
                                        </>

                                    ) : (

                                        <>
                                            Send Verification Code
                                            <FaArrowRight/>
                                        </>

                                    )

                                }

                            </button>

                        </form>

                        <div className="developer">
                            <Link to="/login" className="back-link">
                                &larr; Back to Sign In
                            </Link>
                        </div>

                    </div>

                </div>

            </div>

        </div>

    );

}
