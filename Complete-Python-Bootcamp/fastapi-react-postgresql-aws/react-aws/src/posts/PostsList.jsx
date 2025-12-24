// React hooks:
// useState → manage component state
// useEffect → lifecycle side effects
// useCallback → memoize functions
// useRef → persist mutable values across renders
import React, { useEffect, useState, useCallback, useRef } from "react";

// Axios for HTTP requests
import axios from "axios";

// Navigation hook for programmatic routing
import { useNavigate } from "react-router-dom";

// Global styles
import "../App.css";

// Auth context for logout handling
import { useAuth } from "../auth/AuthContext";

// SPA-safe links
import { Link } from "react-router-dom";

function PostsList() {
  // Store list of posts (paginated)
  const [posts, setPosts] = useState([]);

  // New post input content
  const [newPostContent, setNewPostContent] = useState("");

  // Router navigation hook
  const navigate = useNavigate();

  // Logout function from AuthContext
  const { logout } = useAuth();

  // Pagination state
  const [page, setPage] = useState(1);

  // Whether more posts exist (for infinite scroll)
  const [hasMore, setHasMore] = useState(true);

  // Fallback image handler
  const handleImageError = (e) => {
    e.target.onerror = null; // Prevent infinite error loop
    e.target.src = "./Images/example.png"; // Default placeholder image
  };

  // Fetch posts from backend (paginated)
  const fetchPosts = useCallback(() => {
    // Read JWT token
    const token = localStorage.getItem("token");

    // Redirect to login if not authenticated
    if (!token) {
      navigate("/login");
      return;
    }

    // Backend API URL with page query param
    const url = `${import.meta.env.VITE_API_URL}/posts/?page=${page}`;

    // GET request to fetch posts
    axios
      .get(url, {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((response) => {
        // Append new posts to existing list
        setPosts((posts) => [...posts, ...response.data]);

        // If response has items → there may be more pages
        setHasMore(response.data.length > 0);
      })
      .catch((error) => {
        console.error("Failed to fetch posts:", error);

        // Logout on auth failure
        if (error.response.status === 401) {
          logout();
        }
      });
  }, [page, navigate, logout]);

  // Fetch posts whenever page changes
  useEffect(() => {
    fetchPosts();
  }, [page, fetchPosts]);

  // Navigate to post detail page
  const handlePostClick = (postId) => {
    navigate(`/posts/${postId}`);
  };

  // Handle new post creation
  const handleNewPostSubmit = async (e) => {
    e.preventDefault();

    const token = localStorage.getItem("token");

    // New post payload
    const postData = {
      content: newPostContent,
    };

    try {
      // POST request to create new post
      const response = await axios.post(
        `${import.meta.env.VITE_API_URL}/posts/`,
        postData,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        }
      );

      // Reset input and reload feed
      setNewPostContent("");
      setPage(1);
      setHasMore(true);
      setPosts([]);

      // Reload first page
      fetchPosts();
    } catch (error) {
      if (error.response.status === 401) {
        logout();
      }
      console.error("Error creating new post:", error);
    }
  };

  // Reference for IntersectionObserver
  const observer = useRef();

  // Callback ref for last post element (infinite scroll trigger)
  const lastPostElementRef = useCallback(
    (node) => {
      // Disconnect previous observer
      if (observer.current) observer.current.disconnect();

      // Create new observer
      observer.current = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting && hasMore) {
          // Load next page
          setPage((page) => page + 1);
        }
      });

      // Observe last post element
      if (node) observer.current.observe(node);
    },
    [hasMore]
  );

  // Render UI
  return (
    <div>
      {/* New post input */}
      <form onSubmit={handleNewPostSubmit}>
        <div className="new-post-container">
          {/* Logged-in user profile image */}
          <img
            className="profile-image"
            src={`${localStorage.getItem("user_image")}`}
            alt="Profile"
            onError={handleImageError}
          />

          {/* New post text input */}
          <input
            value={newPostContent}
            onChange={(e) => setNewPostContent(e.target.value)}
            placeholder="What's on your mind?"
            type="text"
            className="new-post-input"
          />

          {/* Submit post */}
          <button type="submit" className="btn btn-primary">
            Post
          </button>
        </div>
      </form>

      <hr className="separator" />

      {/* Posts feed */}
      {posts.map((post, index) => {
        // Attach observer to last post for infinite scrolling
        if (posts.length === index + 1) {
          return (
            <div ref={lastPostElementRef} key={post.id} className="post-card">
              <div className="post-header">
                <p className="post-subtitle">
                  <img
                    className="profile-image"
                    style={{ verticalAlign: "middle" }}
                    src={`${post.image}`}
                    alt="Profile"
                    onError={handleImageError}
                  />
                  <span className="author-name">
                    {post.first_name} {post.last_name}
                  </span>
                  <span className="post-metadata"> | {post.time_ago} |</span>
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
              <p
                onClick={() => handlePostClick(post.id)}
                className="post-content"
              >
                {post.content}
              </p>

              {/* Footer */}
              <div
                className="post-footer"
                onClick={() => handlePostClick(post.id)}
              >
                {post.comments_count === 0
                  ? "Be the first to comment"
                  : `${post.comments_count} comments, show more`}
              </div>
            </div>
          );
        }

        // Normal post card (non-last)
        return (
          <div key={post.id} className="post-card">
            <div className="post-header">
              <p className="post-subtitle">
                <img
                  className="profile-image"
                  style={{ verticalAlign: "middle" }}
                  src={`${post.image}`}
                  alt="Profile"
                  onError={handleImageError}
                />
                <span className="author-name">
                  {post.first_name} {post.last_name}
                </span>
                <span className="post-metadata"> | {post.time_ago}</span>
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

            <p
              onClick={() => handlePostClick(post.id)}
              className="post-content"
            >
              {post.content}
            </p>

            <div
              className="post-footer"
              onClick={() => handlePostClick(post.id)}
            >
              {post.comments_count === 0
                ? "Be the first to comment"
                : `${post.comments_count} comments, show more`}
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default PostsList;
