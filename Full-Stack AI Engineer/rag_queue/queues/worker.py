from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

openai_client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model,
)

def process_query(query: str):
    print("🔍 Searching chunks:", query)

    search_results = vector_db.similarity_search(query=query)

    context = "\n\n\n".join(
        f"Page Content: {r.page_content}\n"
        f"Page Number: {r.metadata.get('page_label')}\n"
        f"File Location: {r.metadata.get('source')}"
        for r in search_results
    )

    SYSTEM_PROMPT = f"""
You are a helpful AI assistant.
Answer ONLY from the context.
Mention page numbers when relevant.

Context:
{context}
"""

    response = openai_client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ],
    )

    answer = response.choices[0].message.content
    print("🤖:", answer)

    return answer
