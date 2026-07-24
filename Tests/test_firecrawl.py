from firecrawl import Firecrawl
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("FIRECRAWL_API_KEY")
app = Firecrawl(api_key=api_key)

data = app.scrape(
    "https://eureka.patsnap.com/report-model-predictive-control-for-integrated-energy-systems",
    only_main_content=True,
    max_age=172800000,
    parsers=["pdf"],
    formats=["markdown"]
)

print(data)