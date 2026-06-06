from dotenv import load_dotenv
from tavily import TavilyClient
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

response = client.search(
    query="AI in Healthcare",
    max_results=5
)

for result in response["results"]:

    print("\n====================")
    print("TITLE:", result["title"])
    print("URL:", result["url"])
    print("CONTENT:", result["content"][:300])