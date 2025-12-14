from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

# Load environment variables (e.g., OPENAI_API_KEY from .env)
load_dotenv()

# Create OpenAI client for chatting with models
openai_client = OpenAI()

# Create OpenAI embedding model to convert text → vectors
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# Connect to an existing Qdrant collection (already indexed earlier)
vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",       # Local Qdrant instance
    collection_name="learning_rag",    # The collection created during indexing
    embedding=embedding_model          # Embedding model used for similarity search
)

# Ask user for a question
user_query = input("Ask something: ")

# Retrieve the MOST relevant chunks (Top-K results) from vector DB
search_results = vector_db.similarity_search(query=user_query)

# Build readable context text from retrieved chunks
# Includes: page content, page number, and source file path
context = "\n\n\n".join([
    f"Page Content: {result.page_content}\n"
    f"Page Number: {result.metadata['page_label']}\n"
    f"File Location: {result.metadata['source']}"
    for result in search_results
])

# System prompt: instructs AI to answer ONLY from retrieved PDF chunks
SYSTEM_PROMPT = f"""
 You are a helpful AI Assistant who answers the user query based on the available context 
 retrieved from a PDF file along with page contents and page numbers.

 You should ONLY answer using the context below and guide the user to the right page number.

 Context:
 {context}
"""

# Send final prompt to OpenAI model
response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": user_query },
    ]
)

# Print the model's answer
print(f"🤖: {response.choices[0].message.content}")
