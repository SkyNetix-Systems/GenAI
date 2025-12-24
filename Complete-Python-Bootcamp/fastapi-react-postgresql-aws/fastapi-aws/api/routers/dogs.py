# APIRouter groups related endpoints, HTTPException is used for error handling
from fastapi import APIRouter, HTTPException

# BaseModel is used to validate incoming request bodies
from pydantic import BaseModel

# SQLAlchemy Dog model representing the dogs table
from api.models import Dog

# Database session dependency and authenticated user dependency
from api.dependencies.deps import db_dependency, user_dependency


# Request body schema for creating a dog
class DogCreateRequest(BaseModel):
    name: str     # Dog's name
    breed: str    # Dog's breed
    age: int      # Dog's age


# Router configuration for dog-related endpoints
router = APIRouter(
    prefix='/dogs',   # All routes start with /dogs
    tags=['Dogs']     # Swagger UI grouping
)


# Get dogs belonging to the currently logged-in user
@router.get("/userdogs")
def read_dog(
    db: db_dependency,     # Injected database session
    user: user_dependency  # Injected authenticated user
):
    # Query all dogs owned by the current user
    dogs = db.query(Dog).filter(Dog.user_id == user.get('id')).all()

    # If no dogs found, raise 404
    # NOTE: .all() returns an empty list, not None
    if not dogs:
        raise HTTPException(status_code=404, detail="Dog not found")

    # Return list of user's dogs
    return dogs


# Get dogs belonging to a specific user (by user_id)
@router.get("/{user_id}")
def read_dog(
    user_id: int,          # User ID from path parameter
    db: db_dependency,     # Injected database session
    user: user_dependency  # Injected authenticated user (for auth check)
):
    # Query dogs for the given user_id
    dogs = db.query(Dog).filter(Dog.user_id == user_id).all()

    # If no dogs found, raise 404
    if not dogs:
        raise HTTPException(status_code=404, detail="Dog not found")

    # Return dogs for that user
    return dogs


# Create a new dog for the logged-in user
@router.post("/")
def create_dog(
    db: db_dependency,         # Injected database session
    user: user_dependency,     # Injected authenticated user
    dog: DogCreateRequest      # Request body payload
):
    # Create Dog ORM object from request data
    db_dog = Dog(**dog.model_dump())

    # Associate dog with the current user
    db_dog.user_id = user.get('id')

    # Add dog to database session
    db.add(db_dog)

    # Commit transaction to persist data
    db.commit()

    # Refresh object to get DB-generated fields (like ID)
    db.refresh(db_dog)

    # Return newly created dog's ID
    return db_dog.id


# Delete a dog owned by the current user
@router.delete("/{dog_id}")
def delete_dog(
    db: db_dependency,        # Injected database session
    user: user_dependency,    # Injected authenticated user
    dog_id: int               # Dog ID from path parameter
):
    # Query dog by ID AND ensure it belongs to the current user
    dog = (
        db.query(Dog)
        .filter(Dog.id == dog_id)
        .filter(Dog.user_id == user.get('id'))
        .first()
    )

    # If dog not found or not owned by user, raise 404
    if dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")

    # Delete dog from DB
    db.delete(dog)

    # Commit deletion
    db.commit()

    # Return confirmation message
    return {"msg": "Dog deleted"}
