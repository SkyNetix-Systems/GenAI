// React hooks:
// useState → component state
// useEffect → lifecycle effects
// useCallback → memoize functions (avoid re-creation)
import React, { useState, useEffect, useCallback } from "react";

// Axios for HTTP requests
import axios from "axios";

// Custom auth hook (login/logout handling)
import { useAuth } from "../auth/AuthContext";

// Global styles
import "../App.css";

function DogsAccount() {
  // Read JWT token from localStorage
  const token = localStorage.getItem("token");

  // Extract logout function from AuthContext
  const { logout } = useAuth();

  // State to store list of user's dogs
  const [dogs, setDogs] = useState([]);

  // State to store dog registration form data
  const [formData, setFormData] = useState({
    name: "",
    breed: "",
    age: "",
  });

  // Fetch all dogs belonging to the logged-in user
  // useCallback prevents unnecessary re-creation
  const fetchDogs = useCallback(async () => {
    try {
      const response = await axios.get(
        `${import.meta.env.VITE_API_URL}/dogs/userdogs/`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      // Update dogs state with API response
      setDogs(response.data);
    } catch (error) {
      // If token is invalid or expired → logout
      if (error.response && error.response.status === 401) {
        logout();
      }
      console.error("Error fetching dogs:", error);
    }
  }, [token, logout]);

  // Fetch dogs when component mounts
  useEffect(() => {
    fetchDogs();
  }, [fetchDogs]);

  // Handle input changes for the form
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  // Handle dog creation
  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      // Send POST request to create new dog
      await axios.post(`${import.meta.env.VITE_API_URL}/dogs/`, formData, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      // Refresh dog list after successful creation
      fetchDogs();

      // Clear form fields
      setFormData({ name: "", breed: "", age: "" });
    } catch (error) {
      if (error.response?.status === 401) {
        logout();
      }
      console.error("Error creating new dog:", error);
    }
  };

  // Handle dog deletion
  const handleDelete = async (dogId) => {
    try {
      // Send DELETE request for selected dog
      await axios.delete(`${import.meta.env.VITE_API_URL}/dogs/${dogId}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      // Refresh dog list after deletion
      fetchDogs();
    } catch (error) {
      if (error.response?.status === 401) {
        logout();
      }
      console.error("Error deleting dog:", error);
    }
  };

  // Render UI
  return (
    <div className="account-container">
      {/* Dog registration form */}
      <form onSubmit={handleSubmit} className="dog-form">
        <h2>Register a New Dog</h2>

        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Name"
          required
        />

        <input
          type="text"
          name="breed"
          value={formData.breed}
          onChange={handleChange}
          placeholder="Breed"
          required
        />

        <input
          type="text"
          name="age"
          value={formData.age}
          onChange={handleChange}
          placeholder="Age"
          required
        />

        <button type="submit">Complete Registration</button>
      </form>

      {/* Separator line */}
      <hr className="separator" />

      {/* List of user's dogs */}
      <div className="dog-list">
        {dogs.map((dog) => (
          <div key={dog.id} className="dog-item">
            <p>Name: {dog.name}</p>
            <p>Breed: {dog.breed}</p>
            <p>Age: {dog.age}</p>

            {/* Delete dog button */}
            <button
              onClick={() => handleDelete(dog.id)}
              className="delete-button"
            >
              X
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default DogsAccount;
