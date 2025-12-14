from dotenv import load_dotenv

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

# Load environment variables (like your OpenAI API key)
load_dotenv()

# Path to the PDF file (same folder as this script)
pdf_path = Path(__file__).parent / "nodejs.pdf"

# Load the PDF into Python as documents
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load() # docs is an array of pages

# Split the documents into smaller overlapping chunks
# This helps improve retrieval accuracy during RAG
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,     # each chunk has ~1000 characters
    chunk_overlap=400    # overlap ensures context continuity
)

chunks = text_splitter.split_documents(documents=docs)

# Create the embedding model using OpenAI
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# Store all embedded chunks inside Qdrant vector database
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",   # Qdrant local instance
    collection_name="learning_rag" # your vector collection name
)

print("Indexing of documents done....")
