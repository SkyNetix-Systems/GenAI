"use client";
import { runAI } from "./actions/ai";
import { useState } from "react";

export default function Page() {
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      const data = await runAI("How are you?");
      setResponse(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <button className="custom-button" onClick={handleClick}>
        What can I do for you?
      </button>
      <br />
      <div>{loading ? "Loading..." : response}</div>
    </>
  );
}
