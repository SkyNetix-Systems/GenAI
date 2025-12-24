# Core FastAPI app class and HTTPException for error handling
from fastapi import FastAPI, HTTPException

# Middleware to handle CORS (React ↔ FastAPI communication)
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file
from dotenv import load_dotenv

# OS module for accessing environment variables
import os

# Datetime utilities for timestamps (UTC-safe)
from datetime import datetime, timezone

# Used to generate random demo data
import random

# Import routers (modular API structure)
from .routers import dogs, comments, posts, auth

# Import SQLAlchemy models and DB session factory
from .models import Dog, Comment, Post, Image, User, SessionLocal


# Load environment variables into the app
load_dotenv()


# Create FastAPI application instance
app = FastAPI()


# -------------------------
# CORS Configuration
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("API_URL")],  # Allow frontend URL (e.g. React app)
    allow_credentials=True,                # Allow cookies / auth headers
    allow_methods=["*"],                   # Allow all HTTP methods
    allow_headers=["*"],                   # Allow all headers
)


# -------------------------
# Populate Database (Dev/Test only)
# -------------------------
@app.post("/populate/")
def populate_db():
    # Create a new DB session
    session = SessionLocal()

    try:
        # -------------------------
        # Create Users
        # -------------------------
        users = [
            User(
                username=f'user{i}',
                hashed_password=f'hash{i}',
                first_name=f'First{i}',
                last_name=f'Last{i}'
            )
            for i in range(1, 31)   # 30 users
        ]

        session.add_all(users)
        session.commit()

        # Refresh users to get generated IDs
        for user in users:
            session.refresh(user)

        # -------------------------
        # Create Dogs, Posts & Images
        # -------------------------
        for user in users:
            # Create 5 dogs per user
            dogs = [
                Dog(
                    name=f'Dog{j}',
                    breed=f'Breed{j % 5}',
                    age=random.randint(1, 10),
                    user_id=user.id
                )
                for j in range(1, 6)
            ]
            session.add_all(dogs)

            # Create 10 posts per user
            posts = [
                Post(
                    content=f'Content{k}',
                    timestamp=datetime.now(timezone.utc),
                    user_id=user.id
                )
                for k in range(1, 11)
            ]
            session.add_all(posts)

            # Create image record for user (image = None)
            image = Image(image=None, user_id=user.id)
            session.add(image)

        session.commit()

        # -------------------------
        # Create Random Comments
        # -------------------------
        # Fetch all posts
        all_posts = session.query(Post).all()

        for user in users:
            # Pick 4 random posts per user
            selected_posts = random.sample(all_posts, 4)

            for post in selected_posts:
                comment = Comment(
                    content=f'Comment from user {user.id} on post {post.id}',
                    timestamp=datetime.now(timezone.utc),
                    user_id=user.id,
                    post_id=post.id
                )
                session.add(comment)

        session.commit()

    except Exception as e:
        # Rollback transaction if anything fails
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Always close DB session
        session.close()

    return {"message": "Database populated successfully!"}


# -------------------------
# Register Routers
# -------------------------
app.include_router(auth.router)
app.include_router(dogs.router)
app.include_router(comments.router)
app.include_router(posts.router)


# -------------------------
# Health Check Endpoint
# -------------------------
@app.get("/")
async def health_check():
    return {"Healthy": 200}
