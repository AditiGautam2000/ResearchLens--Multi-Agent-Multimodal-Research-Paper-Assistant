"""from backend.services.document_ingestion_service import QdrantService

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings


def process_document(file_path: str):

    print("Worker started processing:", file_path)

    # ---- CREATE QDRANT SERVICE ----
    qdrant_service = QdrantService()

    collection_name = "your_agent"

    # ensure collection exists
    qdrant_service.create_collection(collection_name)

    # ---- LOAD PDF ----
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # ---- SPLIT INTO CHUNKS ----
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    print("Chunks created:", len(chunks))

    # ---- CREATE EMBEDDINGS ----
    embeddings_model = OllamaEmbeddings(model="nomic-embed-text")

    embeddings = embeddings_model.embed_documents(
        [chunk.page_content for chunk in chunks]
    )

    print("Embeddings created:", len(embeddings))

    # ---- INSERT INTO QDRANT ----
    qdrant_service.insert_documents(
        collection_name,
        chunks,
        embeddings
    )

    print("Worker finished processing")"""
from backend.services.document_ingestion_service import process_document


def document_worker(file_path: str):

    print("Worker started processing:", file_path)

    process_document(file_path)

    print("Worker finished processing")