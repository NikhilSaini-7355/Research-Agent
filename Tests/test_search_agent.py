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
    results = searcher.search_web(query, max_results)
    searcher.save_to_chromadb(results)
        
except Exception as e:
    logging.error(f"An error occurred while searching the web: {str(e)}")
    raise CustomException(e, sys)