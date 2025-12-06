import React, { useState } from "react";
import BooksView from "./components/BooksView";
import MembersView from "./components/MembersView";
import BorrowView from "./components/BorrowView";

export default function App() {
  const [tab, setTab] = useState("books");

  const TabButton = ({ id, label }) => (
    <button
      onClick={() => setTab(id)}
      style={{
        padding: "0.5rem 1rem",
        marginRight: "0.5rem",
        borderRadius: "999px",
        border: "1px solid #ccc",
        backgroundColor: tab === id ? "#333" : "#fff",
        color: tab === id ? "#fff" : "#000",
        cursor: "pointer"
      }}
    >
      {label}
    </button>
  );

  return (
    <div style={{ fontFamily: "system-ui, sans-serif", padding: "1rem 2rem" }}>
      <h1>📚 Neighborhood Library Manager</h1>

      <div style={{ marginBottom: "1rem" }}>
        <TabButton id="books" label="Books" />
        <TabButton id="members" label="Members" />
        <TabButton id="borrow" label="Borrow / Return" />
      </div>

      <div>
        {tab === "books" && <BooksView />}
        {tab === "members" && <MembersView />}
        {tab === "borrow" && <BorrowView />}
      </div>
    </div>
  );
}
