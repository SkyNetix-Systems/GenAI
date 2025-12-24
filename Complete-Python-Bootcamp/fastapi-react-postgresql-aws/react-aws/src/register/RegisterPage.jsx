// React hook for managing component state
import React, { useState } from "react";

// Hook for programmatic navigation
import { useNavigate } from "react-router-dom";

// Axios for HTTP requests
import axios from "axios";

// Global styles
import "../App.css";

function RegisterPage() {
  // State to store registration form data
  const [formData, setFormData] = useState({
    username: "",
    password: "",
    first_name: "",
    last_name: "",
    image: null, // Base64 encoded profile image
  });

  // Router navigation hook
  const navigate = useNavigate();

  // Generic handler for text input changes
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  // Handle form submission for registration
  const handleRegister = async (event) => {
    event.preventDefault(); // Prevent page reload

    try {
      // Send registration data to backend
      await axios.post(`${import.meta.env.VITE_API_URL}/auth/`, formData);

      // Redirect to login page on success
      navigate("/login");
    } catch (error) {
      // Log error details if registration fails
      console.error(
        "Failed to create user:",
        error.response ? error.response.data : error.message
      );
    }
  };

  // Navigate back to login page
  const handleBack = () => {
    navigate("/login");
  };

  // Convert uploaded image file to Base64
  async function base64ConversionForImages(e) {
    if (e.target.files[0]) {
      getBase64(e.target.files[0]);
    }
  }

  // Read file and convert it to Base64 string
  function getBase64(file) {
    let reader = new FileReader();

    // Start reading file
    reader.readAsDataURL(file);

    // On successful read
    reader.onload = function () {
      setFormData((prevFormData) => ({
        ...prevFormData,
        image: reader.result, // Base64 encoded image
      }));
    };

    // On error
    reader.onerror = function (error) {
      console.log("Error", error);
    };
  }

  // Render UI
  return (
    <div className="register-container">
      {/* Registration form */}
      <form onSubmit={handleRegister} className="register-form">
        <h1>Register</h1>

        {/* First name */}
        <div className="input-group">
          <label htmlFor="first_name">First name</label>
          <input
            type="text"
            name="first_name"
            value={formData.first_name}
            onChange={handleChange}
            required
          />
        </div>

        {/* Last name */}
        <div className="input-group">
          <label htmlFor="last_name">Last name</label>
          <input
            type="text"
            name="last_name"
            value={formData.last_name}
            onChange={handleChange}
            required
          />
        </div>

        {/* Username */}
        <div className="input-group">
          <label htmlFor="username">Username</label>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>

        {/* Password */}
        <div className="input-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>

        {/* Profile image upload */}
        <div className="input-group">
          <label htmlFor="profileImage">Profile Image</label>
          <input type="file" onChange={(e) => base64ConversionForImages(e)} />
        </div>

        {/* Submit button */}
        <button type="submit" className="register-button">
          Register
        </button>

        {/* Back to login */}
        <button onClick={handleBack} className="btn btn-back">
          <span className="arrow">&#8592;</span> Login
        </button>
      </form>
    </div>
  );
}

export default RegisterPage;
