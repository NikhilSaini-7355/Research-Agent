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
from langchain_text_splitters import MarkdownTextSplitter
import sys

load_dotenv()

firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
neon_db_url = os.getenv("NEON_DATABASE_URL")

# Initialize Vector DB (Chroma)
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="new_articles")

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

class web_searcher:
    def search_web(self, query: str, max_results: int = 5):
        response = client.search(
            query=query,
            max_results=max_results,
            include_raw_content=False
        )
        validated_response = SearchResponse(**response)
        return validated_response.results

    def scrape_and_store_to_neon(self, results):
        """Step 1: Scrape websites and save the full raw markdown to Neon Postgres."""
        firecrawl = Firecrawl(api_key=firecrawl_api_key)
        i=0
        for result in results:
            i+=1
            # Scrape a website:
            doc = firecrawl.scrape(str(result.url),
                formats=["markdown"],
                only_main_content=True,)

            os.makedirs("output", exist_ok=True)
            #article_id = str(result.url).rstrip('/').split('/')[-1]
            with open(f"output/{i}.md", "w", encoding="utf-8") as f:
                f.write(clean_markdown(doc.markdown))

    