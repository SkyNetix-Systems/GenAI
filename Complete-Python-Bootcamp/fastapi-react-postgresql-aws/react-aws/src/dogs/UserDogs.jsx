// React hooks for state management, lifecycle, and memoization
import React, { useState, useEffect, useCallback } from "react";

// Axios for making HTTP requests
import axios from "axios";

// Custom authentication hook (for logout handling)
import { useAuth } from "../auth/AuthContext";

// Hook to read route parameters (e.g. /dogs/:user_id)
import { useParams } from "react-router-dom";

// Global styles
import "../App.css";

function UserDogs() {
  // Read JWT token from localStorage
  const token = localStorage.getItem("token");

  // Extract logout function from AuthContext
  const { logout } = useAuth();

  // Extract user_id from URL params
  const { user_id } = useParams();

  // State to store dogs of a specific user
  const [dogs, setDogs] = useState([]);

  // Fetch dogs for the given user_id
  // useCallback prevents function recreation on every render
  const fetchDogs = useCallback(async () => {
    try {
      const response = await axios.get(
        `${import.meta.env.VITE_API_URL}/dogs/${user_id}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      // Update state with fetched dogs
      setDogs(response.data);
    } catch (error) {
      // If token is invalid/expired → logout
      if (error.response && error.response.status === 401) {
        logout();
      }
      console.error("Error fetching dogs:", error);
    }
  }, [token, logout, user_id]);

  // Fetch dogs when component mounts or when user_id changes
  useEffect(() => {
    fetchDogs();
  }, [fetchDogs]);

  // Render list of dogs
  return (
    <div className="dog-list">
      {dogs.map((dog) => (
        <div key={dog.id} className="dog-item">
          <p>Name: {dog.name}</p>
          <p>Breed: {dog.breed}</p>
          <p>Age: {dog.age}</p>
        </div>
      ))}
    </div>
  );
}

export default UserDogs;
