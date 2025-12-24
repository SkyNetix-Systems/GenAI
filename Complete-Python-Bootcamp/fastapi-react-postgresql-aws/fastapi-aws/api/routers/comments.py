# Import APIRouter to define grouped API routes
from fastapi import APIRouter

# BaseModel is used to validate request bodies
from pydantic import BaseModel

# Used to generate UTC timestamps
from datetime import datetime, timezone

# SQLAlchemy Comment model (represents comments table)
from api.models import Comment

# Database session dependency and authenticated user dependency
from api.dependencies.deps import db_dependency, user_dependency


# Request body schema for creating a comment
class CommentCreateRequest(BaseModel):
    content: str     # Actual comment text
    post_id: int     # ID of the post this comment belongs to


# Router configuration for comment-related endpoints
router = APIRouter(
    prefix='/comments',   # All routes start with /comments
    tags=['Comments']     # Swagger UI grouping
)


# Endpoint to create a new comment
@router.post("/")
def create_comment(
    db: db_dependency,              # Injected database session
    user: user_dependency,           # Injected authenticated user
    comment: CommentCreateRequest    # Request body payload
):
    # Create Comment ORM object from request data
    db_comment = Comment(**comment.model_dump())

    # Set current UTC timestamp
    db_comment.timestamp = datetime.now(timezone.utc)

    # Associate comment with logged-in user
    db_comment.user_id = user.get('id')

    # Add comment to database session
    db.add(db_comment)

    # Commit transaction to persist data
    db.commit()

    # Refresh object to get DB-generated fields (like ID)
    db.refresh(db_comment)

    # Return newly created comment
    return db_comment
