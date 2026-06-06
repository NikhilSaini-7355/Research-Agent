from Schemas.search_agent_schema import SearchResponse
from  tavily import TavilyClient
from dotenv import load_dotenv
import os
load_dotenv()

client = TavilyClient(
    api_key = os.getenv("TAVILY_API_KEY")
)

class web_searcher:
    def search_web(self,query: str, max_results: int = 1):

        response = client.search(
            query=query,
            max_results=max_results
        )
        validated_response: SearchResponse = SearchResponse(**response)
        return validated_response.results
