"use client";
import { runAI } from "./actions/ai";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import {Input} from '@/components/ui/input';
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import ReactMarkdown from 'react-markdown';
import Markdown from "react-markdown";


export default function Page() {
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [query, setQuery] = useState("");

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
  );
}
