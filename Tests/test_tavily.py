from src.config.sources import CONTROL_SOURCES as sources
from src.utils.query_classifier import classify_query
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

query = "Pressure transmitter calibration procedure"

classification = classify_query(query)
domain = classification["domain"]

allowed_domains = sources[domain]

response = client.search(
    query=query,
    include_domains=allowed_domains,
    max_results=10
)

