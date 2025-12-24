from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import func
from typing import Optional, List
from datetime import datetime, timezone

from api.models import Post, Comment, User, Image
from api.dependencies.deps import db_dependency, user_dependency


# -------------------------
# Request & Response Schemas
# -------------------------

class PostCreateRequest(BaseModel):
    content: str


class UserBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    image: Optional[str] = None


class CommentSchema(BaseModel):
    id: int
    content: str
    time_ago: str
    user_id: int
    user: UserBase


class PostSchema(BaseModel):
    id: int
    content: str
    time_ago: str
    user_id: int
    user: UserBase
    comments: List[CommentSchema] = []


class PostUserResponse(BaseModel):
    id: int
    content: str
    time_ago: str
    user_id: int
    first_name: str
    last_name: str
    username: str
    comments_count: int
    image: Optional[str] = None


# -------------------------
# Router
# -------------------------

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


# -------------------------
# Read paginated posts feed
# -------------------------

@router.get("/")
def read_posts(
    db: db_dependency,
    user: user_dependency,
    page: int = Query(1, ge=1)
):
    size = 10
    offset = (page - 1) * size

    posts = (
        db.query(
            Post,
            User.first_name,
            User.last_name,
            User.username,
            Image,
            func.count(Comment.id).label("comments_count")
        )
        .join(User, Post.user_id == User.id)
        .join(Image, Image.user_id == User.id)
        .outerjoin(Comment, Comment.post_id == Post.id)
        .group_by(Post.id, User.first_name, User.last_name, User.username, Image.id)
        .order_by(Post.id.desc())
        .offset(offset)
        .limit(size)
        .all()
    )

    return [
        PostUserResponse(
            id=post.id,
            content=post.content,
            time_ago=human_time(post.timestamp),
            user_id=post.user_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
            image=image.image,
            comments_count=comments_count
        )
        for post, first_name, last_name, username, image, comments_count in posts
    ]


# -------------------------
# Read single post + comments
# -------------------------

@router.get("/{post_id}", response_model=PostSchema)
def read_post(post_id: int, db: db_dependency):
    post = (
        db.query(Post)
        .options(
            joinedload(Post.user),
            joinedload(Post.comments).joinedload(Comment.user)
        )
        .filter(Post.id == post_id)
        .first()
    )

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Attach user image
    user_image = db.query(Image).filter(Image.user_id == post.user.id).first()
    post.user.image = user_image.image if user_image else None

    post.time_ago = human_time(post.timestamp)

    # Sort comments newest first
    post.comments.sort(key=lambda c: c.timestamp, reverse=True)

    for comment in post.comments:
        comment.time_ago = human_time(comment.timestamp)
        image = db.query(Image).filter(Image.user_id == comment.user_id).first()
        comment.user.image = image.image if image else None

    return post


# -------------------------
# Create post
# -------------------------

@router.post("/")
def create_post(
    db: db_dependency,
    user: user_dependency,
    post: PostCreateRequest
):
    db_post = Post(
        content=post.content,
        user_id=user.get("id"),
        timestamp=datetime.now(timezone.utc)
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return {"post_id": db_post.id}


# -------------------------
# Utility: Human-readable time
# -------------------------

def human_time(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)

    now = datetime.now(timezone.utc)
    diff = int((now - dt).total_seconds())

    if diff < 60:
        return "now"
    elif diff < 3600:
        return f"{diff // 60}m"
    else:
        return f"{diff // 3600}h"
