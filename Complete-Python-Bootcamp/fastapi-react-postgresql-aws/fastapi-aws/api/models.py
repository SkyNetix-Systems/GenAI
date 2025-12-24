# SQLAlchemy core imports
from sqlalchemy import (
    create_engine,      # Creates DB engine/connection
    Column,             # Defines table columns
    Integer, String,    # Column data types
    ForeignKey,         # Foreign key relationships
    DateTime            # Timestamp columns
)

# Base class for ORM models
from sqlalchemy.ext.declarative import declarative_base

# ORM helpers
from sqlalchemy.orm import (
    relationship,      # Define table relationships
    sessionmaker,      # Create DB sessions
    validates           # (Not used yet, but for field validation)
)

# Datetime utilities with timezone support
from datetime import datetime, timezone

# Load environment variables from .env
from dotenv import load_dotenv

# OS module for environment variables
import os


# Load .env values into environment
load_dotenv()


# Base class all ORM models inherit from
Base = declarative_base()


# -------------------------
# Database Engine
# -------------------------

# If running in DEV (usually SQLite)
if os.getenv("DEPLOYMENT_ENVIRONMENT") == 'DEV':
    engine = create_engine(
        os.getenv("DB_URL"),
        connect_args={'check_same_thread': False}  # Required for SQLite + FastAPI
    )
else:
    # Production DB (Postgres / MySQL / etc.)
    engine = create_engine(os.getenv("DB_URL"))


# -------------------------
# Session Factory
# -------------------------

# Creates a new DB session per request
SessionLocal = sessionmaker(
    autocommit=False,   # Explicit commits only
    autoflush=False,    # Prevent auto-flush before queries
    bind=engine
)


# -------------------------
# User Model
# -------------------------

class User(Base):
    __tablename__ = 'users'   # Table name

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    # One-to-many relationship: User → Dogs
    dogs = relationship(
        "Dog",
        back_populates="owner"
    )

    # One-to-many relationship: User → Posts
    posts = relationship(
        "Post",
        back_populates="user"
    )

    # One-to-one relationship: User → Image
    images = relationship(
        "Image",
        back_populates="owner",
        uselist=False
    )


# -------------------------
# Image Model
# -------------------------

class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)  # Image URL / base64 / path
    user_id = Column(Integer, ForeignKey('users.id'))

    # Back reference to owning user
    owner = relationship(
        "User",
        back_populates="images"
    )


# -------------------------
# Dog Model
# -------------------------

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    breed = Column(String)
    age = Column(Integer)

    # Foreign key linking dog to user
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationship back to user
    owner = relationship(
        "User",
        back_populates="dogs"
    )


# -------------------------
# Post Model
# -------------------------

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)

    # Timestamp stored in UTC
    timestamp = Column(
        DateTime,
        default=datetime.now(timezone.utc)
    )

    # Foreign key linking post to user
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationship to author
    user = relationship(
        "User",
        back_populates="posts"
    )

    # One-to-many relationship: Post → Comments
    comments = relationship(
        "Comment",
        back_populates="post",
        order_by="Comment.id"
    )


# -------------------------
# Comment Model
# -------------------------

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)

    # Timestamp stored in UTC
    timestamp = Column(
        DateTime,
        default=datetime.now(timezone.utc)
    )

    # Foreign keys
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    # Relationship to user (author of comment)
    user = relationship("User")

    # Relationship to post
    post = relationship(
        "Post",
        back_populates="comments"
    )


# -------------------------
# Create Tables
# -------------------------

# Create all tables in the database
# (Only for dev/small apps — use Alembic in prod)
Base.metadata.create_all(bind=engine)
