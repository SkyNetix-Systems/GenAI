import React, { useEffect, useState } from "react";
import {
  listMembers,
  listBooks,
  borrowBook,
  returnBook,
  listBorrowedBooksByMember
} from "../api";

export default function BorrowView() {
  const [members, setMembers] = useState([]);
  const [books, setBooks] = useState([]);
  const [selectedMemberId, setSelectedMemberId] = useState("");
  const [selectedBookId, setSelectedBookId] = useState("");
  const [dueAt, setDueAt] = useState("");
  const [memberIdForList, setMemberIdForList] = useState("");
  const [borrowedBooks, setBorrowedBooks] = useState([]);
  const [bookIdToReturn, setBookIdToReturn] = useState("");
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");
  const [msg, setMsg] = useState("");

  const loadMembersAndBooks = async () => {
    try {
      setLoading(true);
      setErr("");
      const [m, b] = await Promise.all([
        listMembers(),
        listBooks(true)
      ]);
      setMembers(m);
      setBooks(b);
    } catch (e) {
      setErr(e.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadMembersAndBooks();
  }, []);

  const handleBorrow = async (e) => {
    e.preventDefault();
    if (!selectedMemberId || !selectedBookId) {
      setErr("Select both member and book");
      return;
    }
    try {
      setErr("");
      setMsg("");
      await borrowBook({
        member_id: Number(selectedMemberId),
        book_id: Number(selectedBookId),
        due_at: dueAt || null
      });
      setMsg("Book borrowed successfully");
      setDueAt("");
      await loadMembersAndBooks();
    } catch (e) {
      setErr(e.message);
    }
  };

  const handleReturn = async (e) => {
    e.preventDefault();
    if (!bookIdToReturn) {
      setErr("Enter a book ID to return");
      return;
    }
    try {
      setErr("");
      setMsg("");
      await returnBook(Number(bookIdToReturn));
      setMsg("Book returned successfully");
      setBookIdToReturn("");
      await loadMembersAndBooks();
    } catch (e) {
      setErr(e.message);
    }
  };

  const handleListBorrowed = async (e) => {
    e.preventDefault();
    if (!memberIdForList) {
      setErr("Enter a member ID");
      return;
    }
    try {
      setErr("");
      setMsg("");
      const data = await listBorrowedBooksByMember(Number(memberIdForList));
      setBorrowedBooks(data);
    } catch (e) {
      setErr(e.message);
    }
  };

  return (
    <div>
      <h2>Borrow / Return 🔁</h2>
      {loading && <p>Loading…</p>}
      {err && <p style={{ color: "red" }}>{err}</p>}
      {msg && <p style={{ color: "green" }}>{msg}</p>}

      <section style={{ marginBottom: "1rem" }}>
        <h3>Borrow a book</h3>
        <form onSubmit={handleBorrow}>
          <div>
            <label>Member:&nbsp;</label>
            <select
              value={selectedMemberId}
              onChange={(e) => setSelectedMemberId(e.target.value)}
            >
              <option value="">-- select member --</option>
              {members.map((m) => (
                <option key={m.id} value={m.id}>
                  [{m.id}] {m.name}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label>Book:&nbsp;</label>
            <select
              value={selectedBookId}
              onChange={(e) => setSelectedBookId(e.target.value)}
            >
              <option value="">-- select book --</option>
              {books.map((b) => (
                <option key={b.id} value={b.id}>
                  [{b.id}] {b.title}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label>Due at (ISO, optional):&nbsp;</label>
            <input
              value={dueAt}
              onChange={(e) => setDueAt(e.target.value)}
              placeholder="2025-12-31T23:59:59Z"
            />
          </div>

          <button type="submit" style={{ marginTop: "0.5rem" }}>
            Borrow
          </button>
        </form>
      </section>

      <hr />

      <section style={{ marginBottom: "1rem" }}>
        <h3>Return a book</h3>
        <form onSubmit={handleReturn}>
          <label>Book ID:&nbsp;</label>
          <input
            value={bookIdToReturn}
            onChange={(e) => setBookIdToReturn(e.target.value)}
            placeholder="Book ID"
          />
          <button type="submit" style={{ marginLeft: "0.5rem" }}>
            Return
          </button>
        </form>
      </section>

      <hr />

      <section>
        <h3>Books borrowed by a member</h3>
        <form onSubmit={handleListBorrowed}>
          <label>Member ID:&nbsp;</label>
          <input
            value={memberIdForList}
            onChange={(e) => setMemberIdForList(e.target.value)}
            placeholder="Member ID"
          />
          <button type="submit" style={{ marginLeft: "0.5rem" }}>
            List
          </button>
        </form>

        {borrowedBooks.length > 0 ? (
          <ul style={{ marginTop: "0.5rem" }}>
            {borrowedBooks.map((b) => (
              <li key={b.id}>
                <strong>[{b.id}] {b.title}</strong> by {b.author}
              </li>
            ))}
          </ul>
        ) : (
          <p style={{ marginTop: "0.5rem" }}>
            {memberIdForList
              ? "No active borrowed books for this member."
              : "Enter a member ID and click List."}
          </p>
        )}
      </section>
    </div>
  );
}
