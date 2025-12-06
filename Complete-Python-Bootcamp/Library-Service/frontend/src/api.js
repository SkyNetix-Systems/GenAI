const API_BASE = "http://localhost:8000/api";

async function handleResponse(res) {
  if (!res.ok) {
    let detail = "Request failed";
    try {
      const data = await res.json();
      detail = data.detail || JSON.stringify(data);
    } catch {
      // ignore
    }
    throw new Error(detail);
  }
  return res.json();
}

export function listBooks(onlyAvailable) {
  const url = `${API_BASE}/books?only_available=${onlyAvailable ? "true" : "false"}`;
  return fetch(url).then(handleResponse);
}

export function createBook(payload) {
  return fetch(`${API_BASE}/books`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  }).then(handleResponse);
}

export function listMembers() {
  return fetch(`${API_BASE}/members`).then(handleResponse);
}

export function createMember(payload) {
  return fetch(`${API_BASE}/members`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  }).then(handleResponse);
}

export function borrowBook(payload) {
  return fetch(`${API_BASE}/borrow`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  }).then(handleResponse);
}

export function returnBook(bookId) {
  return fetch(`${API_BASE}/return`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ book_id: bookId })
  }).then(handleResponse);
}

export function listBorrowedBooksByMember(memberId) {
  return fetch(`${API_BASE}/members/${memberId}/borrowed-books`).then(
    handleResponse
  );
}
