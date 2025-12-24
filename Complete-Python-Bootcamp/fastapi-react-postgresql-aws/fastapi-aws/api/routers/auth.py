# Import timedelta (for token expiry), datetime (current time), timezone (UTC support)
from datetime import timedelta, datetime, timezone

# Annotated is used with Depends(), Optional allows None values
from typing import Annotated, Optional

# APIRouter for grouping routes, Depends for dependency injection, HTTPException for errors
from fastapi import APIRouter, Depends, HTTPException

# BaseModel is used to define request/response schemas
from pydantic import BaseModel

# HTTP status codes (201, 401, etc.)
from starlette import status

# OAuth2 form for username/password login
from fastapi.security import OAuth2PasswordRequestForm

# JWT library for encoding tokens
from jose import jwt

# Loads environment variables from .env file
from dotenv import load_dotenv

# OS module to access environment variables
import os

# SQLAlchemy models for User and Image tables
from api.models import User, Image

# Database dependency and bcrypt password context
from api.dependencies.deps import db_dependency, bcrypt_context


# Load variables from .env into environment
load_dotenv()


# Create an API router for authentication routes
router = APIRouter(
    prefix='/auth',     # All routes will start with /auth
    tags=['auth']       # Swagger UI grouping
)


# Read secret key used to sign JWT tokens
SECRET_KEY = os.getenv("AUTH_SECRET_KEY")

# Read JWT algorithm (e.g., HS256)
ALGORITHM = os.getenv("AUTH_ALGORITHM")


# Request body model for user registration
class UserCreateRequest(BaseModel):
    username: str                  # Username
    password: str                  # Plain-text password (will be hashed)
    first_name: str                # User first name
    last_name: str                 # User last name
    image: Optional[str] = None    # Optional profile image (URL/base64/etc.)


# Response model returned when issuing JWT tokens
class Token(BaseModel):
    access_token: str              # JWT token string
    token_type: str                # Usually "bearer"
    image: Optional[str] = None    # Optional profile image


# Authenticate user credentials
def authenticate_user(username: str, password: str, db):
    # Fetch user from DB using username
    user = db.query(User).filter(User.username == username).first()
    
    # Fetch user image using user id
    image = db.query(Image).filter(Image.user_id == user.id).first()
    
    # Attach image to user object dynamically
    user.image = image.image

    # If user not found → authentication fails
    if not user:
        return False

    # Verify plain password against hashed password
    if not bcrypt_context.verify(password, user.hashed_password):
        return False

    # If all checks pass, return user object
    return user


# Create JWT access token
def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    # JWT payload (subject + user id)
    encode = {'sub': username, 'id': user_id}

    # Calculate expiration time in UTC
    expires = datetime.now(timezone.utc) + expires_delta

    # Add expiration to payload
    encode.update({'exp': expires})

    # Encode JWT using secret key and algorithm
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


# User registration endpoint
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    db: db_dependency,                     # Inject database session
    create_user_request: UserCreateRequest # Request body
):
    # Create User DB model
    create_user_model = User(
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        # Hash password before storing
        hashed_password=bcrypt_context.hash(create_user_request.password),
    )

    # Save user to DB
    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)  # Get generated user ID

    # Create Image DB model linked to user
    image_model = Image(
        image=create_user_request.image,
        user_id=create_user_model.id,
    )

    # Save image to DB
    db.add(image_model)
    db.commit()


# Login endpoint that issues JWT token
@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],  # OAuth2 login form
    db: db_dependency                                            # Inject DB session
):
    # Authenticate username & password
    user = authenticate_user(form_data.username, form_data.password, db)

    # If authentication fails → 401 Unauthorized
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate user.'
        )

    # Generate JWT token valid for 20 minutes
    token = create_access_token(
        user.username,
        user.id,
        timedelta(minutes=20)
    )

    # Return token response
    return {
        'access_token': token,
        'token_type': 'bearer',
        'image': user.image
    }
