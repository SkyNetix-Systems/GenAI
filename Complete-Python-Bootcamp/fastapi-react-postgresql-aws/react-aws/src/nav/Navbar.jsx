// Import React
import React from "react";

// Custom authentication hook to access auth state and actions
import { useAuth } from "../auth/AuthContext";

// Global styles
import "../App.css";

function Navbar() {
  // Destructure authentication state and logout function
  const { isLoggedIn, logout } = useAuth();

  // Render navigation bar
  return (
    <nav className="navbar">
      {/* App / Brand name */}
      <div className="navbar-brand">Petowners</div>

      {/* Links visible ONLY when user is logged in */}
      {isLoggedIn && (
        <div className="navbar-links">
          {/* Navigate to posts feed */}
          <a href="/posts" className="navbar-item">
            Home
          </a>

          {/* Navigate to dog's account page */}
          <a href="/account" className="navbar-item">
            Dogs Account
          </a>

          {/* Logout link:
              - Calls logout()
              - Redirects to login page */}
          <a href="/login" onClick={logout} className="navbar-item">
            Logout
          </a>

          {/* Placeholder for future links */}
        </div>
      )}

      {/* Links visible ONLY when user is NOT logged in */}
      {!isLoggedIn && (
        <div className="navbar-links">
          {/* Navigate to login page */}
          <a href="/login" className="navbar-item">
            Sign in
          </a>

          {/* Placeholder for future links */}
        </div>
      )}
    </nav>
  );
}

export default Navbar;
