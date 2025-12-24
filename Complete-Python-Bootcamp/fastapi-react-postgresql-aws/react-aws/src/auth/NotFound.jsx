// Import React (required for JSX)
import React from "react";

// 404 Not Found page component
function NotFound() {
  // Render a simple centered message
  return (
    <div
      style={{
        textAlign: "center", // Center text horizontally
        marginTop: "50px", // Push content down from the top
      }}
    >
      {/* Main error heading */}
      <h1>404 Not Found</h1>

      {/* Description message */}
      <p>The page you are looking for does not exist.</p>
    </div>
  );
}

// Export component for use in routing
export default NotFound;
