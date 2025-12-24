// React hooks for state, lifecycle, and memoized callbacks
import React, { useEffect, useState, useCallback } from "react";

// Axios for HTTP requests
import axios from "axios";

// Hooks for route params and navigation
import { useParams, useNavigate } from "react-router-dom";

// Link component for SPA navigation
import { Link } from "react-router-dom";

// Auth context for logout handling
import { useAuth } from "../auth/AuthContext";

// Global styles
import "../App.css";

function PostDetails() {
  // Read postId from URL (e.g. /posts/:postId)
  const { postId } = useParams();

  // State to store post details (including user + comments)
  const [post, setPost] = useState(null);

  // Local comments state (used briefly during updates)
  const [comments, setComments] = useState([]);

  // State for new comment input
  const [newComment, setNewComment] = useState("");

  // Router navigation hook
  const navigate = useNavigate();

  // Extract logout function from AuthContext
  const { logout } = useAuth();

  // Fallback if profile image fails to load
  const handleImageError = (e) => {
    e.target.onerror = null; // Prevent infinite error loop
    e.target.src = "../Images/example.png"; // Default placeholder image
  };

  // Fetch post and its comments from backend
  // useCallback avoids re-creation unless dependencies change
  const fetchPostAndComments = useCallback(() => {
    // Read JWT token
    const token = localStorage.getItem("token");

    // If no token → redirect to login
    if (!token) {
      navigate("/login");
      return;
    }

    // Construct API URL
    const url = `${import.meta.env.VITE_API_URL}/posts/${postId}`;

    // Fetch post details
    axios
      .get(url, {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((response) => {
        // Store post (includes user + comments)
        setPost(response.data);
      })
      .catch((error) => {
        console.error(`Error fetching post with id ${postId}:`, error);
        logout(); // Logout on auth failure
      });
  }, [navigate, postId, logout]);

  // Fetch post when component mounts or postId changes
  useEffect(() => {
    fetchPostAndComments();
  }, [fetchPostAndComments]);

  // Navigate back to posts feed
  const handleBack = () => {
    navigate("/posts");
  };

  // Handle adding a new comment
  const handleAddComment = (e) => {
    e.preventDefault();

    const token = localStorage.getItem("token");

    // Send POST request to create a comment
    axios
      .post(
        `${import.meta.env.VITE_API_URL}/comments/`,
        {
          content: newComment,
          post_id: postId,
        },
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      )
      .then((response) => {
        // Optimistically update comments (temporary)
        setComments([...comments, response.data]);

        // Clear input
        setNewComment("");

        // Re-fetch post to get updated comments list
        fetchPostAndComments();
      })
      .catch((error) => {
        console.error("Error adding comment:", error);
        logout();
      });
  };

  // Render UI
  return (
    <div className="card">
      {post && (
        <>
          {/* Back button */}
          <button onClick={handleBack} className="btn btn-back">
            <span className="arrow">&#8592;</span>
          </button>

          {/* Post header */}
          <div className="post-header">
            <p className="post-subtitle">
              <img
                className="profile-image"
                style={{ verticalAlign: "middle" }}
                src={`${post.user.image}`}
                alt="Profile"
                onError={handleImageError}
              />

              <span className="author-name">
                {post.user.first_name} {post.user.last_name}
              </span>

              <span className="post-metadata"> | {post.time_ago} | </span>

              {/* Link to view author's dogs */}
              <span className="view-dogs-metadata">
                <Link
                  to={`/dogs/${post.user_id}`}
                  className="view-dogs-metadata"
                >
                  view dogs
                </Link>
              </span>
            </p>
          </div>

          {/* Post content */}
          <p className="post-content">{post.content}</p>

          {/* Add comment form */}
          <form onSubmit={handleAddComment}>
            <input
              type="text"
              value={newComment}
              onChange={(e) => setNewComment(e.target.value)}
              placeholder="Write a comment..."
              className="new-comment-input"
            />
            <button type="submit" className="btn btn-primary">
              Add Comment
            </button>
          </form>

          {/* Comments list */}
          <div className="comments-section">
            {post.comments.map((comment) => (
              <div key={comment.id} className="comment">
                <div className="comment-header">
                  <p className="comment-subtitle">
                    <img
                      className="profile-image"
                      style={{ verticalAlign: "middle" }}
                      src={`${comment.user.image}`}
                      alt="Profile"
                      onError={handleImageError}
                    />

                    <span className="author-name">
                      {comment.user.first_name} {comment.user.last_name}
                    </span>

                    <span className="post-metadata">
                      {" "}
                      | {comment.time_ago} |{" "}
                    </span>

                    {/* Link to comment author's dogs */}
                    <span className="view-dogs-metadata">
                      <Link
                        to={`/dogs/${comment.user.id}`}
                        className="view-dogs-metadata"
                      >
                        view dogs
                      </Link>
                    </span>
                  </p>

                  {/* Comment content */}
                  <p className="comment-content">{comment.content}</p>
                </div>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
}

export default PostDetails;
