from src.agents.search_agent import web_searcher
from src.exception import CustomException
from src.logger import logging


import sys


try:
    query = "AI in Healthcare"
    max_results = 5
    searcher = web_searcher()
    results = searcher.search_web(query, max_results)

    for result in results:
        print("\n====================")
        print("TITLE:", result.title)
        print("URL:", result.url)
        print("CONTENT:", result.content[:300])
except Exception as e:
    logging.error(f"An error occurred while searching the web: {str(e)}")
    raise CustomException(e, sys)