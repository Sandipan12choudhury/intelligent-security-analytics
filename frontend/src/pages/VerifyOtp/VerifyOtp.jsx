import { useEffect, useRef, useState } from "react";

import { useNavigate, useLocation, Link } from "react-router-dom";

import "/src/pages/Login/Login.css";

import "./VerifyOtp.css";

import AuthLeftPanel from "/src/components/auth/AuthLeftPanel";

import { setToken } from "/src/utils/auth";

import usePageTitle from "/src/utils/usePageTitle";

import {

    FaShieldAlt,
    FaEnvelope,
    FaArrowRight,
    FaSpinner

} from "react-icons/fa";

import API_BASE from "/src/config/api";

const RESEND_COOLDOWN_SECONDS = 30;

export default function VerifyOtp() {

    usePageTitle("Verify Identity");

    const navigate = useNavigate();

    const location = useLocation();

    const state = location.state || {};

    const { otpSessionId, maskedPhone, maskedEmail, purpose } = state;

    const [digits, setDigits] = useState(["", "", "", "", "", ""]);

    const [submitting, setSubmitting] = useState(false);

    const [error, setError] = useState("");

    const [resending, setResending] = useState(false);

    const [cooldown, setCooldown] = useState(RESEND_COOLDOWN_SECONDS);

    const inputRefs = useRef([]);

    useEffect(() => {

        if (!otpSessionId) {

            navigate("/login", { replace: true });

        }

    }, [otpSessionId, navigate]);

    useEffect(() => {

        if (cooldown <= 0) {

            return;

        }

        const timer = setTimeout(() => setCooldown(cooldown - 1), 1000);

        return () => clearTimeout(timer);

    }, [cooldown]);

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

    function handlePaste(e) {

        const pasted = e.clipboardData.getData("text").replace(/[^0-9]/g, "");

        if (pasted.length === 6) {

            setDigits(pasted.split(""));

            inputRefs.current[5]?.focus();

        }

    }

    function handleVerify(e) {

        e.preventDefault();

        const code = digits.join("");

        if (code.length !== 6 || submitting) {

            return;

        }

        setSubmitting(true);

        setError("");

        fetch(`${API_BASE}/api/v1/auth/verify-otp`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({ otp_session_id: otpSessionId, code })

        })

            .then(async (response) => {

                const data = await response.json();

                if (!response.ok) {

                    throw new Error(data.detail || "Verification failed.");

                }

                return data;

            })

            .then((data) => {

                setToken(data.token);

                navigate("/dashboard", { replace: true });

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

    function handleResend() {

        if (cooldown > 0 || resending) {

            return;

        }

        setResending(true);

        setError("");

        fetch(`${API_BASE}/api/v1/auth/resend-otp`, {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({ otp_session_id: otpSessionId })

        })

            .then(async (response) => {

                const data = await response.json();

                if (!response.ok) {

                    throw new Error(data.detail || "Could not resend code.");

                }

                setCooldown(RESEND_COOLDOWN_SECONDS);

                setDigits(["", "", "", "", "", ""]);

                inputRefs.current[0]?.focus();

            })

            .catch((err) => {

                setError(err.message);

            })

            .finally(() => {

                setResending(false);

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

                        <h2>Verify Your Identity</h2>

                        <p>

                            <FaEnvelope style={{ marginRight: 8 }} />

                            We've sent a 6-digit code to {maskedEmail}

                            {

                                purpose === "register" &&
                                " to confirm your new account"

                            }

                        </p>

                        <form onSubmit={handleVerify}>

                            <div

                                className="otp-input-row"

                                onPaste={handlePaste}

                            >

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

                            {

                                error && (

                                    <div className="form-error">

                                        {error}

                                    </div>

                                )

                            }

                            <div className="options">

                                <span></span>

                                <button

                                    type="button"

                                    className="resend-link"

                                    onClick={handleResend}

                                    disabled={cooldown > 0 || resending}

                                >

                                    {

                                        resending
                                            ? "Sending..."
                                            : cooldown > 0
                                                ? `Resend code in ${cooldown}s`
                                                : "Resend code"

                                    }

                                </button>

                            </div>

                            <button

                                type="submit"

                                className="login-button"

                                disabled={submitting || digits.join("").length !== 6}

                            >

                                {

                                    submitting ? (

                                        <>
                                            <FaSpinner className="spin-icon"/>
                                            Verifying...
                                        </>

                                    ) : (

                                        <>
                                            Verify & Continue
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
