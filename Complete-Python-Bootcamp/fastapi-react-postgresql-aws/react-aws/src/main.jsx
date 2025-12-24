// Import React (required for JSX)
import React from "react";

// ReactDOM client API (React 18+)
import ReactDOM from "react-dom/client";

// Root App component
import App from "./App.jsx";

// Global CSS styles
import "./index.css";

// Create a React root and render the application
ReactDOM.createRoot(document.getElementById("root")) // Attach React to <div id="root">
  .render(
    // Render the App component
    <App />
  );
