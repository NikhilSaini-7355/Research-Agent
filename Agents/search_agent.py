from Schemas.search_agent_schema import SearchResponse
from firecrawl import Firecrawl
from src.utils.clean_markdown import clean_markdown
from tavily import TavilyClient
from dotenv import load_dotenv
import asyncio
import aiohttp
import os
import re
import uuid
import psycopg2
from psycopg2.extras import execute_values
import chromadb
from datetime import datetime
from langchain_text_splitters import MarkdownTextSplitter, RecursiveCharacterTextSplitter
from tavily_agent_toolkit import search_dedup, ModelConfig, ModelObject
import sys

load_dotenv()

firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
neon_db_url = os.getenv("NEON_DATABASE_URL")

# Initialize Vector DB (Chroma)
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="new_articles")

class web_searcher:
    def __init__(self):
        # self.client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        self._init_neon_db()
    
    def _init_neon_db(self):
        """Initializes the PostgreSQL table on Neon if it doesn't exist."""
        with psycopg2.connect(neon_db_url) as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS articles (
                        id VARCHAR(50) PRIMARY KEY,
                        url TEXT UNIQUE,
                        title TEXT,
                        markdown_content TEXT,
                        scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        is_vectorized BOOLEAN DEFAULT FALSE
                    );
                ''')
                conn.commit()

    async def search_web(self, queries: list[str], max_results: int = 1):
        results = await search_dedup(
            api_key=os.getenv("TAVILY_API_KEY"),
            queries=queries,
            search_depth="advanced",
            max_results=max_results,
        )
        validated_response: SearchResponse = SearchResponse(**results)
        return validated_response.results
        # return results

    # def scrape_and_store_to_neon(self, results): 
    #     """Step 1: Scrape websites and save the full raw markdown to Neon Postgres."""
    #     firecrawl = Firecrawl(api_key=firecrawl_api_key)
        
    #     with psycopg2.connect(neon_db_url) as conn:
    #         with conn.cursor() as cursor:
    #             for result in results:
    #                 url_str = result.get('url') if isinstance(result, dict) else str(result.url)
    #                 title_str = result.get('title', 'Unknown Title') if isinstance(result, dict) else getattr(result, 'title', 'Unknown Title')
                    
    #                 try:
    #                     # Scrape raw markdown
    #                     doc = firecrawl.scrape(
    #                         url_str,
    #                         formats=["markdown"],
    #                         only_main_content=True
    #                     )
    #                     cleaned_content = clean_markdown(doc.markdown)
    #                     article_id = f"art_{uuid.uuid4().hex[:8]}"

    #                     # Postgres specific syntax: ON CONFLICT DO NOTHING
    #                     cursor.execute('''
    #                         INSERT INTO articles (id, url, title, markdown_content, is_vectorized)
    #                         VALUES (%s, %s, %s, %s, %s)
    #                         ON CONFLICT (url) DO NOTHING;
    #                     ''', (article_id, url_str, title_str, cleaned_content, False))
                        
    #                     print(f" Saved to Neon: {url_str}")

    #                 except Exception as e:
    #                     print(f"❌ Scraping failed for {url_str}: {str(e)}")
    #             conn.commit()

    # def process_neon_to_chroma(self):
    #     """Step 2: Fetch unprocessed text from Neon, chunk it, and upsert to ChromaDB."""
    #     with psycopg2.connect(neon_db_url) as conn:
    #         with conn.cursor() as cursor:
    #             # Fetch pending articles
    #             cursor.execute('SELECT id, url, title, markdown_content FROM articles WHERE is_vectorized = FALSE;')
    #             unprocessed_articles = cursor.fetchall()

    #             if not unprocessed_articles:
    #                 print("No new articles to process into ChromaDB.")
    #                 return
                
    #             # headers_to_split_on = [
    #             #     ("#", "Header_1"),
    #             #     ("##", "Header_2"),
    #             #     ("###", "Header_3"),
    #             # ]

    #             text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=300)

    #             for article in unprocessed_articles:
    #                 db_id, url, title, content = article
                    
    #                 # Split markdown into clean chunks
    #                 chunks = text_splitter.split_text(content)
                    
    #                 documents = []
    #                 metadatas = []
    #                 ids = []

    #                 for i, chunk in enumerate(chunks):
    #                     documents.append(chunk)
    #                     metadatas.append({
    #                         "source_url": url,
    #                         "title": title,
    #                         "chunk_index": i,
    #                         "neon_db_id": db_id 
    #                     })
    #                     ids.append(f"{db_id}_chunk_{i}")

    #                 # Store chunks inside ChromaDB
    #                 collection.upsert(
    #                     documents=documents,
    #                     metadatas=metadatas,
    #                     ids=ids
    #                 )

    #                 peek_results = collection.peek()
    #                 vector_dimension = len(peek_results['embeddings'][0])
    #                 print(f" Vector dimension for ChromaDB: {vector_dimension}")

    #                 # Update status back in Neon
    #                 cursor.execute('UPDATE articles SET is_vectorized = TRUE WHERE id = %s;', (db_id,))
    #                 print(f" Vectorized & Synced to Chroma: {title}")
                
    #             conn.commit()

    