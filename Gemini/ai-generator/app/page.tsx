"use client";
import { runAI } from "./actions/ai";
import { useEffect, useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export default function Page() {
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [query, setQuery] = useState("");

  useEffect(() => {
    setQuery(""); // Ensure state is updated after the component mounts
  }, []);

  const handleClick = async (e: any) => {
    e.preventDefault();
    setLoading(true);
    try {
      const data = await runAI(query);
      setResponse(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="m-5">
      <form onSubmit={handleClick}>
        <input
          className="mb-5 bordered-input"
          placeholder="Ask anything!"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <br />
        <Button>Generate with AI</Button>
      </form>
      <Card className="mt-5">
        <CardHeader>AI Response</CardHeader>
        <CardContent>
          <div>{loading ? "Loading..." : response}</div>
        </CardContent>
      </Card>
    </div>
  );
}
