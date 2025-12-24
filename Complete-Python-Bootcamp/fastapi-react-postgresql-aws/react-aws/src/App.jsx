// Core React import
import React from "react";

// React Router components for SPA routing
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// Posts (feed + details)
import PostsList from "./posts/PostsList";
import PostDetails from "./posts/PostDetails";

// Navigation bar
import Navbar from "./nav/Navbar";

// Authentication pages
import LoginPage from "./auth/LoginPage";
import RegisterPage from "./register/RegisterPage";

// Route guard for protected pages
import ProtectedRoute from "./auth/ProtectedRoute";

// 404 page
import NotFound from "./auth/NotFound";

// Authentication context provider
import { AuthProvider } from "./auth/AuthContext";

// Dog-related pages
import UserDogs from "./dogs/UserDogs";
import DogsAccount from "./dogs/DogsAccount";

function App() {
  // Root component defining routing and global providers
  return (
    // BrowserRouter enables client-side routing
    <Router>
      {/* AuthProvider wraps the entire app to provide auth state */}
      <AuthProvider>
        {/* Navigation bar visible on all pages */}
        <Navbar />

        {/* Main page container */}
        <div className="custom-container">
          {/* Route definitions */}
          <Routes>
            {/* Public routes */}
            <Route path="/" element={<LoginPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />

            {/* Protected posts feed */}
            <Route
              path="/posts"
              element={
                <ProtectedRoute>
                  <PostsList />
                </ProtectedRoute>
              }
            />

            {/* Protected single post view */}
            <Route
              path="/posts/:postId"
              element={
                <ProtectedRoute>
                  <PostDetails />
                </ProtectedRoute>
              }
            />

            {/* Protected dogs account (current user) */}
            <Route
              path="/account"
              element={
                <ProtectedRoute>
                  <DogsAccount />
                </ProtectedRoute>
              }
            />

            {/* Protected view of another user's dogs */}
            <Route
              path="/dogs/:user_id"
              element={
                <ProtectedRoute>
                  <UserDogs />
                </ProtectedRoute>
              }
            />

            {/* Catch-all route for unknown URLs */}
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
      </AuthProvider>
    </Router>
  );
}

export default App;
