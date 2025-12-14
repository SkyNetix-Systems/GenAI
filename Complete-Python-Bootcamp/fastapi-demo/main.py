# Import FastAPI core classes
# FastAPI → main app class
# Depends → dependency injection (for DB sessions)
# HTTPException → to return proper HTTP error responses
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware


# Import SQLAlchemy Session type (used for typing and DB operations)
from sqlalchemy.orm import Session

# Import SQLAlchemy ORM models (tables)
import database_models

# Import database session factory and engine
from database import SessionLocal, engine

# Import Pydantic model used for request/response validation
from models import Product


# Create database tables if they do not already exist
# This scans database_models and creates tables based on ORM definitions
database_models.Base.metadata.create_all(bind=engine)


# Create FastAPI application instance
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (dev only)
    allow_credentials=True,
    allow_methods=["*"],  # allow GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)



# Dependency function to provide a database session per request
def get_db():
    # Create a new SQLAlchemy session
    db = SessionLocal()
    try:
        # Yield the session to the API endpoint
        # FastAPI injects this into route functions
        yield db
    finally:
        # Always close the session after request is completed
        # Prevents connection leaks
        db.close()


# Sample product data (Pydantic models)
# Used to initialize database with default records
products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

# Single product instance (not used directly, but kept as an example)
product = Product(
    id=5,
    name="Chair",
    description="A comfortable chair",
    price=89.99,
    quantity=15
)


# Function to initialize database with sample data
def init_db():
    # Create a standalone DB session (not request-scoped)
    db = SessionLocal()

    # Count existing product records
    existing_count = db.query(database_models.Product).count()

    # Only insert sample data if table is empty
    if existing_count == 0:
        for product in products:
            # Convert Pydantic model → dict → ORM model
            # The ** operator unpacks a dictionary into keyword arguments
            db.add(database_models.Product(**product.model_dump())) 
        # Commit transaction to persist records
        db.commit()
        print("Database initialized with sample products.")

    # Close the session
    db.close()


# Initialize database when application starts
init_db()


# -------------------- API ENDPOINTS --------------------


# GET all products
@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    # Query all product records from database
    products = db.query(database_models.Product).all()
    return products


# GET product by ID
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    # Query product matching the given ID
    product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == product_id)
        .first()
    )
    # Return product if found
    if product:
        return product

    # Return error if product not found
    return {"error": "Product not found"}


# CREATE a new product
@app.post("/products/")
def create_product(product: Product, db: Session = Depends(get_db)):
    # Convert incoming Pydantic model to ORM object
    db.add(database_models.Product(**product.model_dump()))

    # Commit transaction to insert record
    db.commit()

    return {"message": "Product created successfully", "product": product}


# UPDATE an existing product
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product, db: Session = Depends(get_db)):
    # Fetch product from database
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == product_id)
        .first()
    )

    # If product does not exist, raise 404 error
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Update fields
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity

    # Commit changes
    db.commit()

    # Refresh object to get latest DB state
    db.refresh(db_product)

    return {"message": "Product updated successfully", "product": db_product}


# DELETE a product
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    # Fetch product by ID
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == product_id)
        .first()
    )

    # If product does not exist, raise 404
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Delete record
    db.delete(db_product)

    # Commit deletion
    db.commit()

    return {"message": "Product deleted successfully"}
