import { Routes, Route, Navigate } from "react-router-dom";

import Login from "/src/pages/Login/Login";
import Register from "/src/pages/Register/Register";
import VerifyOtp from "/src/pages/VerifyOtp/VerifyOtp";
import ForgotPassword from "/src/pages/ForgotPassword/ForgotPassword";
import ResetPassword from "/src/pages/ResetPassword/ResetPassword";
import Dashboard from "/src/pages/Dashboard/Dashboard";
import Applications from "/src/pages/Applications/Applications";
import ApplicationDetails from "/src/pages/ApplicationDetails/ApplicationDetails";
import Observations from "/src/pages/Observations/Observations";
import AddObservation from "/src/pages/AddObservation/AddObservation";
import Reports from "/src/pages/Reports/Reports";
import Profile from "/src/pages/Profile/Profile";
import Settings from "/src/pages/Settings/Settings";
import Logs from "/src/pages/Logs/Logs";

import ProtectedRoute from "/src/components/auth/ProtectedRoute";
import { isAuthenticated } from "/src/utils/auth";

function App() {

    return (

        <Routes>

            <Route
                path="/"
                element={

                    <Navigate

                        to={isAuthenticated() ? "/dashboard" : "/login"}

                        replace

                    />

                }
            />

            <Route
                path="/login"
                element={

                    isAuthenticated()
                        ? <Navigate to="/dashboard" replace />
                        : <Login />

                }
            />

            <Route
                path="/register"
                element={

                    isAuthenticated()
                        ? <Navigate to="/dashboard" replace />
                        : <Register />

                }
            />

            <Route
                path="/verify-otp"
                element={<VerifyOtp />}
            />

            <Route
                path="/forgot-password"
                element={

                    isAuthenticated()
                        ? <Navigate to="/dashboard" replace />
                        : <ForgotPassword />

                }
            />

            <Route
                path="/reset-password"
                element={<ResetPassword />}
            />

            <Route
                path="/dashboard"
                element={

                    <ProtectedRoute>
                        <Dashboard />
                    </ProtectedRoute>

                }
            />

            <Route
                path="/applications"
                element={

                    <ProtectedRoute>
                        <Applications />
                    </ProtectedRoute>

                }
            />

            <Route
                path="/applications/:applicationId"
                element={

                    <ProtectedRoute>
                        <ApplicationDetails />
                    </ProtectedRoute>

                }
            />

            <Route
                path="/observations"
                element={

                    <ProtectedRoute>
                        <Observations />
                    </ProtectedRoute>

                }
            />

            <Route
                path="/observations/add"
                element={

                    <ProtectedRoute>
                        <AddObservation />
                    </ProtectedRoute>

                }
            />

            <Route
                path="/reports"
                element={

                    <ProtectedRoute>
                        <Reports />
                    </ProtectedRoute>

                }
            />

            <Route
                path="/profile"
                element={

                    <ProtectedRoute>
                        <Profile />
                    </ProtectedRoute>

                }
            />

            <Route
                path="/settings"
                element={

                    <ProtectedRoute>
                        <Settings />
                    </ProtectedRoute>

                }
            />

            <Route
                path="/logs"
                element={

                    <ProtectedRoute>
                        <Logs />
                    </ProtectedRoute>

                }
            />

            <Route
                path="*"
                element={

                    <Navigate

                        to={isAuthenticated() ? "/dashboard" : "/login"}

                        replace

                    />

                }
            />

        </Routes>

    );

}

export default App;
