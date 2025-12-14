# Import SQLAlchemy function to create a database engine
# The engine manages the connection pool to the database
from sqlalchemy import create_engine

# Import sessionmaker to create database sessions
# Sessions are used to interact with the database (CRUD operations)
from sqlalchemy.orm import sessionmaker

# Database connection URL
# Format:
# postgresql://<username>:<password>@<host>:<port>/<database_name>
db_url = "postgresql://postgres:0000@localhost:5432/skynetix"

# Create the SQLAlchemy Engine
# This does NOT open a connection immediately
# It configures the database dialect, driver, and connection pool
engine = create_engine(db_url)

# Create a session factory (SessionLocal)
# autocommit=False → transactions must be committed explicitly
# autoflush=False → changes are flushed to DB only when commit() is called
# bind=engine → sessions created will use the above engine
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
