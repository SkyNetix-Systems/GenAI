Neighborhood Library Service
=================================

Backend (FastAPI + PostgreSQL) + Frontend (React + Vite)

This project is a complete library management system built with:

- FastAPI (REST backend)
- PostgreSQL (database)
- React + Vite (frontend UI)
- Python (business logic + optional gRPC server)

It supports:
- Manage Books
- Manage Members
- Borrow / Return Books
- View borrowed books per member

-----------------------------------------
1. Project Structure
-----------------------------------------

Library-Service/
├── proto/
│   └── library.proto
├── sql/
│   └── schema.sql
├── library_server/
│   ├── __init__.py
│   ├── db.py
│   ├── rest_api.py
│   ├── app_server.py
│   ├── library_pb2.py (generated)
│   └── library_pb2_grpc.py (generated)
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   ├── src/
│   │    ├── App.jsx
│   │    ├── main.jsx
│   │    ├── api.js
│   │    └── components/
│   │         ├── BooksView.jsx
│   │         ├── MembersView.jsx
│   │         └── BorrowView.jsx
└── requirements.txt

-----------------------------------------
2. Install Dependencies
-----------------------------------------

Backend:

    pip install -r requirements.txt

Frontend:

    cd frontend
    npm install

-----------------------------------------
3. Setup PostgreSQL Database
-----------------------------------------

Run:

    psql -h localhost -U <your_user> -d <your_db> -f sql/schema.sql

Required environment variables:

    PGHOST=localhost
    PGPORT=5432
    PGDATABASE=library_db
    PGUSER=library_user
    PGPASSWORD=library_pass

-----------------------------------------
4. Start Backend (FastAPI)
Uvicorn = a super-fast server that runs your Python web app
"Asynchronous Server Gateway Interface"
-----------------------------------------

    uvicorn library_server.rest_api:app --reload --port 8000

API exposed at:
    http://localhost:8000/api

-----------------------------------------
5. Start Frontend (React + Vite)
-----------------------------------------

    cd frontend
    npm run dev

Open frontend UI:
    http://localhost:5173

-----------------------------------------
6. API Endpoints
-----------------------------------------

Books:
    GET /api/books
    POST /api/books
    PUT /api/books/{book_id}

Members:
    GET /api/members
    POST /api/members
    PUT /api/members/{member_id}

Borrow / Return:
    POST /api/borrow
    POST /api/return
    GET  /api/members/{id}/borrowed-books

-----------------------------------------
7. Optional: gRPC Server
-----------------------------------------

    python -m library_server.app_server

gRPC runs on port 50051.

-----------------------------------------
8. Regenerate gRPC Files
-----------------------------------------

    python -m grpc_tools.protoc -I=./proto --python_out=./library_server --grpc_python_out=./library_server proto/library.proto

-----------------------------------------
9. Done!
-----------------------------------------

Frontend: http://localhost:5173
API Docs: http://localhost:8000/docs
