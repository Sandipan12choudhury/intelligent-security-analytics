import { useEffect, useRef, useState } from "react";

import { useNavigate, useLocation, Link } from "react-router-dom";

import "/src/pages/Login/Login.css";

import "/src/pages/VerifyOtp/VerifyOtp.css";

import AuthLeftPanel from "/src/components/auth/AuthLeftPanel";

import usePageTitle from "/src/utils/usePageTitle";

import {

    FaShieldAlt,
    FaLock,
    FaMobileAlt,
    FaArrowRight,
    FaEye,
    FaEyeSlash,
    FaSpinner

} from "react-icons/fa";

import API_BASE from "/src/config/api";

export default function ResetPassword() {

    usePageTitle("Reset Password");

    const navigate = useNavigate();

    const location = useLocation();

    const state = location.state || {};

    const { otpSessionId, maskedPhone, maskedEmail } = state;

    const [digits, setDigits] = useState(["", "", "", "", "", ""]);

    const [newPassword, setNewPassword] = useState("");

    const [confirmPassword, setConfirmPassword] = useState("");

    const [showPassword, setShowPassword] = useState(false);

    const [submitting, setSubmitting] = useState(false);

    const [error, setError] = useState("");

    const [success, setSuccess] = useState(false);

    const inputRefs = useRef([]);

    useEffect(() => {

        if (!otpSessionId) {

            navigate("/forgot-password", { replace: true });

        }

    }, [otpSessionId, navigate]);

    function handleDigitChange(index, value) {

        const clean = value.replace(/[^0-9]/g, "").slice(-1);

        const next = [...digits];

        next[index] = clean;

        setDigits(next);

        if (clean && index < 5) {

            inputRefs.current[index + 1]?.focus();

        }

    }

    function handleKeyDown(index, e) {

        if (e.key === "Backspace" && !digits[index] && index > 0) {

            inputRefs.current[index - 1]?.focus();

        }

    }

    function handleSubmit(e) {

        e.preventDefault();

        const code = digits.join("");

        if (code.length !== 6 || submitting) {

            return;

        }

        if (newPassword.length < 8) {

            setError("Password must be at least 8 characters long.");

            return;

        }

        if (newPassword !== confirmPassword) {

            setError("Passwords do not match.");

            return;

        }

        setSubmitting(true);

        setError("");

        fetch(`${API_BASE}/api/v1/auth/reset-password`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({

                otp_session_id: otpSessionId,

                code,

                new_password: newPassword

            })

        })

            .then(async (response) => {

                const data = await response.json();

                if (!response.ok) {

                    throw new Error(data.detail || "Reset failed.");

                }

                return data;

            })

            .then(() => {

                setSuccess(true);

                setTimeout(() => {

                    navigate("/login", { replace: true });

                }, 2000);

            })

            .catch((err) => {

                setError(err.message);

                setDigits(["", "", "", "", "", ""]);

                inputRefs.current[0]?.focus();

            })

            .finally(() => {

                setSubmitting(false);

            });

    }

    if (!otpSessionId) {

        return null;

    }

    return (

        <div className="login-page">

            <div className="login-container">

                <AuthLeftPanel />

                <div className="right-panel">

                    <div className="login-card">

                        <FaShieldAlt className="top-icon"/>

                        <h2>Reset Password</h2>

                        <p>

                            <FaMobileAlt style={{ marginRight: 8 }} />

                            Enter the code sent to {maskedEmail}

                        </p>

                        {

                            success ? (

                                <div className="form-success">

                                    Password reset successfully.
                                    Redirecting to sign in...

                                </div>

                            ) : (

                                <form onSubmit={handleSubmit}>

                                    <div className="otp-input-row">

                                        {

                                            digits.map((digit, index) => (

                                                <input

                                                    key={index}

                                                    ref={(el) =>
                                                        (inputRefs.current[index] = el)
                                                    }

                                                    type="text"

                                                    inputMode="numeric"

                                                    maxLength={1}

                                                    value={digit}

                                                    onChange={(e) =>
                                                        handleDigitChange(
                                                            index, e.target.value
                                                        )
                                                    }

                                                    onKeyDown={(e) =>
                                                        handleKeyDown(index, e)
                                                    }

                                                    autoFocus={index === 0}

                                                />

                                            ))

                                        }

                                    </div>

                                    <label>New Password</label>

                                    <div className="input-box">

                                        <FaLock/>

                                        <input

                                            type={showPassword ? "text" : "password"}

                                            placeholder="At least 8 characters"

                                            value={newPassword}

                                            onChange={(e) =>
                                                setNewPassword(e.target.value)
                                            }

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

                                    <label>Confirm New Password</label>

                                    <div className="input-box">

                                        <FaLock/>

                                        <input

                                            type={showPassword ? "text" : "password"}

                                            placeholder="Re-enter new password"

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

                                    <button

                                        type="submit"

                                        className="login-button"

                                        disabled={

                                            submitting ||
                                            digits.join("").length !== 6

                                        }

                                    >

                                        {

                                            submitting ? (

                                                <>
                                                    <FaSpinner className="spin-icon"/>
                                                    Resetting...
                                                </>

                                            ) : (

                                                <>
                                                    Reset Password
                                                    <FaArrowRight/>
                                                </>

                                            )

                                        }

                                    </button>

                                </form>

                            )

                        }

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
