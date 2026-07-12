import { useEffect, useRef, useState } from "react";

import {

    FaTimes,
    FaMobileAlt,
    FaSpinner

} from "react-icons/fa";

import "./SettingsOtpModal.css";

import API_BASE from "/src/config/api";

const RESEND_COOLDOWN_SECONDS = 30;

export default function SettingsOtpModal({

    title,

    otpSessionId,

    maskedPhone,

    maskedEmail,

    onConfirm,

    onClose

}) {

    const [digits, setDigits] = useState(["", "", "", "", "", ""]);

    const [submitting, setSubmitting] = useState(false);

    const [error, setError] = useState("");

    const [resending, setResending] = useState(false);

    const [cooldown, setCooldown] = useState(RESEND_COOLDOWN_SECONDS);

    const inputRefs = useRef([]);

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

    function handleSubmit(e) {

        e.preventDefault();

        const code = digits.join("");

        if (code.length !== 6 || submitting) {

            return;

        }

        setSubmitting(true);

        setError("");

        onConfirm(code)

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

    return (

        <div className="settings-otp-overlay" onClick={onClose}>

            <div

                className="settings-otp-modal"

                onClick={(e) => e.stopPropagation()}

            >

                <div className="settings-otp-header">

                    <h3>{title}</h3>

                    <button onClick={onClose}>

                        <FaTimes />

                    </button>

                </div>

                <p className="settings-otp-subtext">

                    <FaMobileAlt style={{ marginRight: 8 }} />

                    Enter the code sent to {maskedEmail}

                </p>

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
                                        handleDigitChange(index, e.target.value)
                                    }

                                    onKeyDown={(e) => handleKeyDown(index, e)}

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

                    <div className="settings-otp-resend">

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

                        className="settings-otp-confirm-btn"

                        disabled={submitting || digits.join("").length !== 6}

                    >

                        {

                            submitting ? (

                                <>
                                    <FaSpinner className="spin-icon" />
                                    Confirming...
                                </>

                            ) : (

                                "Confirm"

                            )

                        }

                    </button>

                </form>

            </div>

        </div>

    );

}
