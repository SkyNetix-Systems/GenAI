// React hooks for state and lifecycle
import React, { useEffect, useState } from "react";

// Navigate is used to redirect unauthenticated users
import { Navigate } from "react-router-dom";

// Component that protects routes from unauthenticated access
function ProtectedRoute({ children }) {
  // Tracks whether the user is authenticated
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Tracks whether auth check is still running
  const [isLoading, setIsLoading] = useState(true);

  // Runs once when component mounts
  useEffect(() => {
    // Function to verify authentication token
    const verifyToken = async () => {
      // Read JWT token from localStorage
      const token = localStorage.getItem("token");

      // If token does not exist → user is not authenticated
      if (!token) {
        setIsAuthenticated(false);
      } else {
        // Token exists (not validated server-side here)
        setIsAuthenticated(true);
      }

      // Mark loading as complete
      setIsLoading(false);
    };

    verifyToken();
  }, []);

  // Show loading state while checking auth
  if (isLoading) {
    return <div>Loading...</div>;
  }

  // If authenticated → render protected content
  // Else → redirect to login page
  return isAuthenticated ? children : <Navigate to="/login" />;
}

export default ProtectedRoute;
