import React, { useEffect, useState } from "react";
import { listMembers, createMember } from "../api";

export default function MembersView() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [members, setMembers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");

  const load = async () => {
    try {
      setLoading(true);
      setErr("");
      const data = await listMembers();
      setMembers(data);
    } catch (e) {
      setErr(e.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    load();
  }, []);

  const onSubmit = async (e) => {
    e.preventDefault();
    if (!name.trim() || !email.trim()) {
      setErr("Name and email are required");
      return;
    }
    try {
      setErr("");
      await createMember({ name, email, phone: phone || null });
      setName("");
      setEmail("");
      setPhone("");
      await load();
    } catch (e) {
      setErr(e.message);
    }
  };

  return (
    <div>
      <h2>Members 👤</h2>

      <form onSubmit={onSubmit} style={{ marginBottom: "1rem" }}>
        <div>
          <label>Name:&nbsp;</label>
          <input
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Member name"
          />
        </div>
        <div>
          <label>Email:&nbsp;</label>
          <input
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
          />
        </div>
        <div>
          <label>Phone:&nbsp;</label>
          <input
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            placeholder="Optional"
          />
        </div>
        <button type="submit" style={{ marginTop: "0.5rem" }}>
          Create Member
        </button>
      </form>

      <hr />

      {loading && <p>Loading members…</p>}
      {err && <p style={{ color: "red" }}>{err}</p>}

      {members.length === 0 && !loading ? (
        <p>No members found.</p>
      ) : (
        <ul>
          {members.map((m) => (
            <li key={m.id}>
              <strong>[{m.id}] {m.name}</strong> — {m.email}{" "}
              {m.phone ? `(${m.phone})` : ""}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
