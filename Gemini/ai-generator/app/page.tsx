"use client";
import { runAI } from "./actions/ai";
<<<<<<< HEAD
import { useEffect, useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
=======
import { useState } from "react";
import { Button } from "@/components/ui/button";
import {Input} from '@/components/ui/input';
>>>>>>> 0591152e7460dd07b3fb22375410a6ffc2df8b58
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
<<<<<<< HEAD
} from "@/components/ui/card";
=======
} from "@/components/ui/card"
import ReactMarkdown from 'react-markdown';
import Markdown from "react-markdown";

>>>>>>> 0591152e7460dd07b3fb22375410a6ffc2df8b58

export default function Page() {
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [query, setQuery] = useState("");

<<<<<<< HEAD
  useEffect(() => {
    setQuery(""); // Ensure state is updated after the component mounts
  }, []);

=======
>>>>>>> 0591152e7460dd07b3fb22375410a6ffc2df8b58
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
<<<<<<< HEAD
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
=======
    <>
        <form onSubmit={handleClick}>
          <Input className="mb-5" placeholder="Ask anything!" value={query} onChange={e => setQuery(e.target.value)}/>
          <Button>Generate with AI</Button>
        </form>
        <Card className="mt-5">
          <CardHeader className="mt-5">AI response will appear here...</CardHeader>
          <CardContent>
          {loading? <div>Loading...</div> : 
            <ReactMarkdown> 
              {response}
            </ReactMarkdown>
          }
          </CardContent>
        </Card>
        </>
>>>>>>> 0591152e7460dd07b3fb22375410a6ffc2df8b58
  );
}
