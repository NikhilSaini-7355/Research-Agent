from dotenv import load_dotenv
from tavily_agent_toolkit import search_dedup, ModelConfig, ModelObject
import langchain # Import langchain for debugging
from Schemas.search_agent_schema import SearchResponse
from src.exception import CustomException
from src.logger import logging
from Agents.search_agent import web_searcher

import os
import asyncio

load_dotenv()

# 1. Enable debugging to print the exact LLM errors to your console
langchain.debug = True 

questions = [
    "What is the current impact of AI adoption on India's healthcare sector's GDP contribution?",
    "How does AI in healthcare affect India's economic growth rate compared to other emerging economies?",
    "What are the potential economic benefits of integrating AI in India's public healthcare systems?",
    "How can AI-driven healthcare innovations contribute to India's goal of achieving a $5 trillion GDP by 2025?",
    "What is the estimated return on investment for AI-based healthcare solutions in India compared to traditional healthcare methods?"
]

async def main():
    try:
        searcher = web_searcher()
        max_results = 5
        results = asyncio.run(searcher.search_web(questions, max_results))
        
        print(f"Total results: {len(results.get('results', []))}")
        for r in results.get("results", []):
            print(r['content'])
            print("\n====================")
            
    except Exception as e:
        logging.error("An error occurred while tavily agent toolkit")
        print(CustomException(e, sys))

asyncio.run(main())