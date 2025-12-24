// Import React core hooks:
// createContext → create a global auth context
// useContext → consume context easily
// useState → manage local state
// useEffect → run side effects (on load)
import React, { createContext, useContext, useState, useEffect } from "react";

// Hook used for programmatic navigation
import { useNavigate } from "react-router-dom";

// Axios for HTTP requests
import axios from "axios";

// Create an authentication context
// Default value is null (will be provided by AuthProvider)
const AuthContext = createContext(null);

// AuthProvider component wraps the app and provides auth state
export const AuthProvider = ({ children }) => {
  // Track whether user is logged in
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Used to redirect users after login/logout
  const navigate = useNavigate();

  // Runs once when component mounts
  // Checks if JWT token already exists in localStorage
  useEffect(() => {
    const token = localStorage.getItem("token");

    // Convert token existence to boolean
    setIsLoggedIn(!!token);
  }, []);

  // Login function (called from login form)
  const login = async (username, password) => {
    // Create form data required by OAuth2PasswordRequestForm
    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);

    try {
      // Send login request to FastAPI auth endpoint
      const response = await axios.post(
        `${import.meta.env.VITE_API_URL}/auth/token/`,
        formData,
        {
          headers: {
            // OAuth2 requires this content type
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      );

      // If response is not OK, treat as failure
      if (response.status !== 200) {
        throw new Error("Login failed");
      }

      // Store JWT token in localStorage
      localStorage.setItem("token", response.data.access_token);

      // Store user image separately for UI usage
      localStorage.setItem("user_image", response.data.image);

      // Navigate to posts page after successful login
      navigate("/posts");

      // Update auth state
      setIsLoggedIn(true);
    } catch (error) {
      // Log error for debugging
      console.error("Login failed:", error);

      // If unauthorized, redirect back to login
      if (error.response?.status === 401) {
        navigate("/login");
      }
    }
  };

  // Logout function
  const logout = () => {
    // Remove JWT token
    localStorage.removeItem("token");

    // Remove cached user image
    localStorage.removeItem("user_image");

    // Update auth state
    setIsLoggedIn(false);
  };

  // Provide auth state and actions to all child components
  return (
    <AuthContext.Provider value={{ isLoggedIn, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook for consuming auth context
// eslint-disable-next-line react-refresh/only-export-components
export const useAuth = () => useContext(AuthContext);
