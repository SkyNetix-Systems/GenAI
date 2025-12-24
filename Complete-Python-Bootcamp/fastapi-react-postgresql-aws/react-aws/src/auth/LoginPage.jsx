// React hooks for state and lifecycle handling
import React, { useState, useEffect } from "react";

// Hook for programmatic navigation between routes
import { useNavigate } from "react-router-dom";

// Custom authentication context hook
import { useAuth } from "./AuthContext";

// Global / page-level styles
import "../App.css";

// Login page component
function LoginPage() {
  // Local state for username input
  const [username, setUsername] = useState("");

  // Local state for password input
  const [password, setPassword] = useState("");

  // Router navigation hook
  const navigate = useNavigate();

  // Extract login function from auth context
  const { login } = useAuth();

  // Run once on component mount
  // If token exists, redirect user to posts page
  useEffect(() => {
    const token = localStorage.getItem("token");

    if (token) {
      navigate("/posts");
    }
  }, [navigate]);

  // Handle login form submission
  const handleLogin = async (event) => {
    // Prevent page reload on form submit
    event.preventDefault();

    // Call login function from AuthContext
    login(username, password);
  };

  // Navigate to register page
  const handleBack = () => {
    navigate("/register");
  };

  // JSX rendering
  return (
    <div className="login-container">
      {/* Login form */}
      <form onSubmit={handleLogin} className="login-form">
        {/* Page heading */}
        <h1>Login</h1>

        {/* Username input */}
        <div className="input-group">
          <label htmlFor="username">Username</label>
          <input
            id="username"
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            autoComplete="username"
          />
        </div>

        {/* Password input */}
        <div className="input-group">
          <label htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            autoComplete="password"
          />
        </div>

        {/* Submit login button */}
        <button type="submit" className="login-button">
          Log In
        </button>

        {/* Redirect to register page */}
        <button onClick={handleBack} className="btn btn-back">
          <span>Register</span>
        </button>
      </form>
    </div>
  );
}

export default LoginPage;
