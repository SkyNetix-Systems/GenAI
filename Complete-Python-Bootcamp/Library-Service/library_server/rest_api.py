from typing import Optional, List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from . import db

app = FastAPI(title="Neighborhood Library REST API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BookCreate(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None


class BookUpdate(BaseModel):
    id: int
    title: str
    author: str
    isbn: Optional[str] = None
    available: bool


class BookOut(BaseModel):
    id: int
    title: str
    author: str
    isbn: Optional[str]
    available: bool


class MemberCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None


class MemberUpdate(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None


class MemberOut(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]


class BorrowRequest(BaseModel):
    member_id: int
    book_id: int
    due_at: Optional[str] = None


class LoanOut(BaseModel):
    id: int
    member_id: int
    book_id: int
    borrowed_at: str
    due_at: Optional[str]
    returned_at: Optional[str]


class ReturnRequest(BaseModel):
    book_id: int


class BorrowedBooksOut(BaseModel):
    id: int
    title: str
    author: str
    isbn: Optional[str]
    available: bool


def _book_row_to_dict(row) -> dict:
    return {
        "id": row[0],
        "title": row[1],
        "author": row[2],
        "isbn": row[3],
        "available": row[4],
    }


def _member_row_to_dict(row) -> dict:
    return {
        "id": row[0],
        "name": row[1],
        "email": row[2],
        "phone": row[3],
    }


def _loan_row_to_dict(row) -> dict:
    return {
        "id": row[0],
        "member_id": row[1],
        "book_id": row[2],
        "borrowed_at": row[3],
        "due_at": row[4],
        "returned_at": row[5],
    }


@app.get("/api/books", response_model=List[BookOut])
def list_books(only_available: bool = False):
    rows = db.list_books(only_available)
    return [_book_row_to_dict(r) for r in rows]


@app.post("/api/books", response_model=BookOut)
def create_book(payload: BookCreate):
    row = db.create_book(payload.title, payload.author, payload.isbn)
    return _book_row_to_dict(row)


@app.put("/api/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, payload: BookUpdate):
    row = db.update_book(
        book_id,
        payload.title,
        payload.author,
        payload.isbn,
        payload.available,
    )
    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return _book_row_to_dict(row)


@app.get("/api/members", response_model=List[MemberOut])
def list_members():
    rows = db.list_members()
    return [_member_row_to_dict(r) for r in rows]


@app.post("/api/members", response_model=MemberOut)
def create_member(payload: MemberCreate):
    row = db.create_member(payload.name, payload.email, payload.phone)
    return _member_row_to_dict(row)


@app.put("/api/members/{member_id}", response_model=MemberOut)
def update_member(member_id: int, payload: MemberUpdate):
    row = db.update_member(
        member_id,
        payload.name,
        payload.email,
        payload.phone,
    )
    if row is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return _member_row_to_dict(row)


@app.post("/api/borrow", response_model=LoanOut)
def borrow_book(payload: BorrowRequest):
    try:
        row = db.borrow_book(payload.member_id, payload.book_id, payload.due_at)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return _loan_row_to_dict(row)


@app.post("/api/return", response_model=LoanOut)
def return_book(payload: ReturnRequest):
    try:
        row = db.return_book(payload.book_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return _loan_row_to_dict(row)


@app.get("/api/members/{member_id}/borrowed-books", response_model=List[BorrowedBooksOut])
def list_borrowed_books_by_member(member_id: int):
    rows = db.list_borrowed_books_by_member(member_id)
    return [
        {
            "id": r[0],
            "title": r[1],
            "author": r[2],
            "isbn": r[3],
            "available": r[4],
        }
        for r in rows
    ]
