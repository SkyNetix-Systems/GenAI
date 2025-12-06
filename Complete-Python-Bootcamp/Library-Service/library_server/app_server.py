from concurrent import futures
import logging

import grpc

from . import db
from . import library_pb2, library_pb2_grpc


def _book_row_to_msg(row):
    return library_pb2.Book(
        id=row[0],
        title=row[1],
        author=row[2],
        isbn=row[3] or "",
        available=row[4],
    )


def _member_row_to_msg(row):
    return library_pb2.Member(
        id=row[0],
        name=row[1],
        email=row[2],
        phone=row[3] or "",
    )


def _loan_row_to_msg(row):
    return library_pb2.Loan(
        id=row[0],
        member_id=row[1],
        book_id=row[2],
        borrowed_at=row[3],
        due_at=row[4] or "",
        returned_at=row[5] or "",
    )


class LibraryService(library_pb2_grpc.LibraryServiceServicer):
    def CreateBook(self, request, context):
        row = db.create_book(request.title, request.author, request.isbn)
        return library_pb2.BookResponse(book=_book_row_to_msg(row))

    def UpdateBook(self, request, context):
        row = db.update_book(
            request.id,
            request.title,
            request.author,
            request.isbn,
            request.available,
        )
        if row is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Book not found")
        return library_pb2.BookResponse(book=_book_row_to_msg(row))

    def ListBooks(self, request, context):
        rows = db.list_books(request.only_available)
        return library_pb2.ListBooksResponse(
            books=[_book_row_to_msg(r) for r in rows]
        )

    def CreateMember(self, request, context):
        row = db.create_member(request.name, request.email, request.phone)
        return library_pb2.MemberResponse(member=_member_row_to_msg(row))

    def UpdateMember(self, request, context):
        row = db.update_member(
            request.id,
            request.name,
            request.email,
            request.phone,
        )
        if row is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Member not found")
        return library_pb2.MemberResponse(member=_member_row_to_msg(row))

    def ListMembers(self, request, context):
        rows = db.list_members()
        return library_pb2.ListMembersResponse(
            members=[_member_row_to_msg(r) for r in rows]
        )

    def BorrowBook(self, request, context):
        try:
            row = db.borrow_book(
                request.member_id,
                request.book_id,
                request.due_at or None,
            )
        except ValueError as e:
            context.abort(grpc.StatusCode.FAILED_PRECONDITION, str(e))
        return library_pb2.BorrowBookResponse(loan=_loan_row_to_msg(row))

    def ReturnBook(self, request, context):
        try:
            row = db.return_book(request.book_id)
        except ValueError as e:
            context.abort(grpc.StatusCode.FAILED_PRECONDITION, str(e))
        return library_pb2.ReturnBookResponse(loan=_loan_row_to_msg(row))

    def ListBorrowedBooksByMember(self, request, context):
        rows = db.list_borrowed_books_by_member(request.member_id)
        return library_pb2.ListBorrowedBooksByMemberResponse(
            books=[_book_row_to_msg(r) for r in rows]
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_LibraryServiceServicer_to_server(
        LibraryService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    logging.info("LibraryService gRPC server started on :50051")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
