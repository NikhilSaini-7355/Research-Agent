import os
import re
from Agents.search_agent import web_searcher
from src.exception import CustomException
from src.logger import logging
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")

import sys


try:
    query = "AI in USA"
    max_results = 5
    searcher = web_searcher()
    print("Searching the web...")
    results = searcher.search_web(query, max_results)
    
    # Pipeline Step 1: Ingest into Neon PostgreSQL
    print("Scraping and storing raw data to Neon.tech...")
    searcher.scrape_and_store_to_neon(results)
    
    # Pipeline Step 2: Chunk, embed, and sync to ChromaDB
    print("Processing Neon articles into ChromaDB text embeddings...")
    searcher.process_neon_to_chroma()
    
    print("Pipeline complete!")
        
except Exception as e:
    logging.error(f"An error occurred while searching the web: {str(e)}")
    raise CustomException(e, sys)