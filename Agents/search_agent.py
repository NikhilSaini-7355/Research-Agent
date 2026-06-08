from Schemas.search_agent_schema import SearchResponse
from firecrawl import Firecrawl
from src.utils.clean_markdown import clean_markdown
from tavily import TavilyClient
from dotenv import load_dotenv
import asyncio
import aiohttp
import os
import re
import sys

load_dotenv()

firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

class web_searcher:
    def search_web(self, query: str, max_results: int = 1):
        response = client.search(
            query=query,
            max_results=max_results,
            include_raw_content=True
        )
        validated_response: SearchResponse = SearchResponse(**response)
        return validated_response.results

    def save_to_chromadb(self, results):
        firecrawl = Firecrawl(api_key=firecrawl_api_key)
        i=0;
        for result in results:
            i+=1
            # Scrape a website:
            doc = firecrawl.scrape(str(result.url),
                formats=["markdown"],
                only_main_content=True,)

            os.makedirs("output", exist_ok=True)
            article_id = str(result.url).rstrip('/').split('/')[-1]
            with open(f"output/{i}.md", "w", encoding="utf-8") as f:
                f.write(clean_markdown(doc.markdown))

    