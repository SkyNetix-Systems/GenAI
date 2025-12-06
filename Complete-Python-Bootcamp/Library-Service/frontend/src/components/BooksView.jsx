import React, { useEffect, useState } from "react";
import { listBooks, createBook } from "../api";

export default function BooksView() {
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [isbn, setIsbn] = useState("");
  const [onlyAvailable, setOnlyAvailable] = useState(false);
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");

  const load = async () => {
    try {
      setLoading(true);
      setErr("");
      const data = await listBooks(onlyAvailable);
      setBooks(data);
    } catch (e) {
      setErr(e.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    load();
  }, [onlyAvailable]);

  const onSubmit = async (e) => {
    e.preventDefault();
    if (!title.trim() || !author.trim()) {
      setErr("Title and author are required");
      return;
    }
    try {
      setErr("");
      await createBook({ title, author, isbn: isbn || null });
      setTitle("");
      setAuthor("");
      setIsbn("");
      await load();
    } catch (e) {
      setErr(e.message);
    }
  };

  return (
    <div>
      <h2>Books 📖</h2>

      <form onSubmit={onSubmit} style={{ marginBottom: "1rem" }}>
        <div>
          <label>Title:&nbsp;</label>
          <input
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Book title"
          />
        </div>
        <div>
          <label>Author:&nbsp;</label>
          <input
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            placeholder="Author"
          />
        </div>
        <div>
          <label>ISBN:&nbsp;</label>
          <input
            value={isbn}
            onChange={(e) => setIsbn(e.target.value)}
            placeholder="Optional"
          />
        </div>
        <button type="submit" style={{ marginTop: "0.5rem" }}>
          Create Book
        </button>
      </form>

      <hr />

      <label>
        <input
          type="checkbox"
          checked={onlyAvailable}
          onChange={(e) => setOnlyAvailable(e.target.checked)}
        />
        &nbsp;Show only available
      </label>

      {loading && <p>Loading books…</p>}
      {err && <p style={{ color: "red" }}>{err}</p>}

      {books.length === 0 && !loading ? (
        <p>No books found.</p>
      ) : (
        <ul>
          {books.map((b) => (
            <li key={b.id}>
              <strong>[{b.id}] {b.title}</strong> by {b.author} —{" "}
              {b.available ? "✅ Available" : "❌ Borrowed"}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
