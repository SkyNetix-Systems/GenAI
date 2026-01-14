from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated, List

from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.mongodb import MongoDBSaver

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

class State(TypedDict):
    messages: Annotated[List, add_messages]

def chatbot(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# 🔥 NO AUTH URI (LOCAL DEV)
DB_URI = "mongodb://localhost:27017"

with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph = graph_builder.compile(checkpointer=checkpointer)

    config = {
        "configurable": {
            "thread_id": "piyush" # user id
        }
    }

    for chunk in graph.stream(
        {"messages": [HumanMessage(content="What is my name?")]},
        config=config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()
