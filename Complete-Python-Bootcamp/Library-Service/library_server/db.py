import os
import psycopg2
from contextlib import contextmanager
from datetime import datetime


def _get_env(name: str, default: str | None = None) -> str:
    value = os.getenv(name, default)
    if value is None:
        raise RuntimeError(f"Environment variable {name} is required")
    return value


DB_CONFIG = {
    "host": _get_env("PGHOST", "localhost"),
    "port": int(os.getenv("PGPORT", "5432")),
    "dbname": _get_env("PGDATABASE", "library_db"),
    "user": _get_env("PGUSER", "admin"),
    "password": _get_env("PGPASSWORD", "admin123!"),
}


@contextmanager
def get_conn():
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()


def _now_iso() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


# ------------ BOOKS ------------

def create_book(title: str, author: str, isbn: str | None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO books (title, author, isbn, available)
                VALUES (%s, %s, %s, TRUE)
                RETURNING id, title, author, isbn, available
                """,
                (title, author, isbn or None),
            )
            row = cur.fetchone()
        conn.commit()
    return row


def update_book(book_id: int, title: str, author: str, isbn: str | None, available: bool):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE books
                   SET title = %s,
                       author = %s,
                       isbn = %s,
                       available = %s
                 WHERE id = %s
                RETURNING id, title, author, isbn, available
                """,
                (title, author, isbn or None, available, book_id),
            )
            row = cur.fetchone()
        conn.commit()
    return row


def list_books(only_available: bool):
    with get_conn() as conn:
        with conn.cursor() as cur:
            if only_available:
                cur.execute(
                    """
                    SELECT id, title, author, isbn, available
                    FROM books
                    WHERE available = TRUE
                    ORDER BY id
                    """
                )
            else:
                cur.execute(
                    """
                    SELECT id, title, author, isbn, available
                    FROM books
                    ORDER BY id
                    """
                )
            rows = cur.fetchall()
    return rows


# ------------ MEMBERS ------------

def create_member(name: str, email: str, phone: str | None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO members (name, email, phone)
                VALUES (%s, %s, %s)
                RETURNING id, name, email, phone
                """,
                (name, email, phone or None),
            )
            row = cur.fetchone()
        conn.commit()
    return row


def update_member(member_id: int, name: str, email: str, phone: str | None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE members
                   SET name = %s,
                       email = %s,
                       phone = %s
                 WHERE id = %s
                RETURNING id, name, email, phone
                """,
                (name, email, phone or None, member_id),
            )
            row = cur.fetchone()
        conn.commit()
    return row


def list_members():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, name, email, phone
                FROM members
                ORDER BY id
                """
            )
            rows = cur.fetchall()
    return rows


def get_member(member_id: int):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, email, phone FROM members WHERE id = %s",
                (member_id,),
            )
            row = cur.fetchone()
    return row


def get_book(book_id: int):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, title, author, isbn, available FROM books WHERE id = %s",
                (book_id,),
            )
            row = cur.fetchone()
    return row


# ------------ LOANS ------------

def borrow_book(member_id: int, book_id: int, due_at: str | None):
    borrowed_at = _now_iso()
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM members WHERE id = %s", (member_id,))
            if cur.fetchone() is None:
                raise ValueError("Member does not exist")

            cur.execute(
                "SELECT available FROM books WHERE id = %s",
                (book_id,),
            )
            book_row = cur.fetchone()
            if book_row is None:
                raise ValueError("Book does not exist")
            if not book_row[0]:
                raise ValueError("Book is not available")

            cur.execute(
                """
                INSERT INTO loans (member_id, book_id, borrowed_at, due_at, returned_at)
                VALUES (%s, %s, %s, %s, NULL)
                RETURNING id, member_id, book_id, borrowed_at, due_at, returned_at
                """,
                (member_id, book_id, borrowed_at, due_at or None),
            )
            loan_row = cur.fetchone()

            cur.execute(
                "UPDATE books SET available = FALSE WHERE id = %s",
                (book_id,),
            )

        conn.commit()
    return loan_row


def return_book(book_id: int):
    returned_at = _now_iso()
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, member_id, book_id, borrowed_at, due_at, returned_at
                FROM loans
                WHERE book_id = %s AND returned_at IS NULL
                ORDER BY id DESC
                LIMIT 1
                """,
                (book_id,),
            )
            loan_row = cur.fetchone()
            if loan_row is None:
                raise ValueError("No active loan for this book")

            loan_id = loan_row[0]

            cur.execute(
                """
                UPDATE loans
                   SET returned_at = %s
                 WHERE id = %s
                RETURNING id, member_id, book_id, borrowed_at, due_at, returned_at
                """,
                (returned_at, loan_id),
            )
            updated_loan = cur.fetchone()

            cur.execute(
                "UPDATE books SET available = TRUE WHERE id = %s",
                (book_id,),
            )

        conn.commit()
    return updated_loan


def list_borrowed_books_by_member(member_id: int):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT b.id, b.title, b.author, b.isbn, b.available
                FROM loans l
                JOIN books b ON b.id = l.book_id
                WHERE l.member_id = %s AND l.returned_at IS NULL
                ORDER BY b.id
                """,
                (member_id,),
            )
            rows = cur.fetchall()
    return rows
