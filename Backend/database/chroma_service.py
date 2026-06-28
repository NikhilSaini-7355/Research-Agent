import os
import asyncio
import chromadb
from chromadb.utils import embedding_functions
from uuid import UUID
from typing import List
from dotenv import load_dotenv  # 1. Import load_dotenv
from chromadb import Search, K, Knn
from backend.core.context import db_session_var, current_user_var, current_project_id_var

load_dotenv()

# Setup ChromaDB to save to your local disk (or connect to a cloud host)
CHROMA_API_KEY = os.getenv("CHROMA_DB_API_KEY")

class ChromaService:
    def __init__(self):
        # PersistentClient saves data to your local hard drive
        # CloudClient saves data to a chroma db present in the cloud
        self.client = chromadb.CloudClient(
            api_key=CHROMA_API_KEY,
            tenant='de6b16f2-0c84-4e0d-9031-6b19c18dcdcd',
            database='Research-Agent'
            )

        # This function perfectly replicates the VECTOR(1536) from your image.
        # It automatically converts text to vectors upon insertion.
        self.google_ef = embedding_functions.GoogleGeminiEmbeddingFunction(
            model_name="gemini-embedding-001",
            task_type="RETRIEVAL_DOCUMENT",
            dimension=1536,
        )
        
        # Get or create the main "table" (called a Collection in Chroma)
        self.collection = self.client.get_or_create_collection(
            name="research_knowledge_base",
            embedding_function=self.google_ef
        )

    async def ingest_chunks(self, project_id: UUID, content_id: UUID, chunks: List[str]):
        """
        Takes raw text chunks, attaches relational metadata, and saves them to ChromaDB.
        Runs in a background thread to prevent blocking your async FastAPI app.
        """
        if not chunks:
            return

        # 1. Map data to ChromaDB arrays
        # Create unique IDs for each chunk: "contentID_chunkIndex"
        ids = [f"{str(content_id)}_chunk_{i}" for i in range(len(chunks))]
        
        # Map your Postgres Foreign Keys into Chroma Metadata
        metadatas = [
            {
                "project_id": str(project_id), 
                "content_id": str(content_id)
            } for _ in chunks
        ]

        # 2. Add to ChromaDB (Running in a thread because Chroma's local client is synchronous)
        await asyncio.to_thread(
            self.collection.add,
            documents=chunks,
            metadatas=metadatas,
            ids=ids
        )
        print(f"✅ Embedded and stored {len(chunks)} chunks in ChromaDB.")

    def retrieve_by_query(self, query: str, limit: int = 10):
        """
        Retrieve documents from the database based on a query.

        Args:
            query (str): The search query.
            top_k (int): The number of top results to return.
            limit (int): The maximum number of results to retrieve.
        """
        project_id = current_project_id_var.get()
        search = (Search()
        .where(K("project_id") == project_id)
        .rank(Knn(query=query))
        .limit(limit)
        .select(K.DOCUMENT, K.SCORE))

        results = self.collection.search(search)
        return results

# Instantiate the service
chroma_service = ChromaService()