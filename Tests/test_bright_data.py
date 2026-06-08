from firecrawl import Firecrawl
import os
import re
from src.agents.search_agent import web_searcher
from src.exception import CustomException
from src.logger import logging
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")

import sys

def clean_markdown(markdown: str) -> str:
    """
    Remove common RAG-unfriendly noise.
    """

    patterns = [
    # --- Previously defined standard patterns ---
    r"\[Download.*?\]\(.*?\)",
    r"\[Listen.*?\]\(.*?\)",
    r"\[Print.*?\]\(.*?\)",
    r"\[Share.*?\]\(.*?\)",
    r"\[Subscribe.*?\]\(.*?\)",
    r"\[View.*?\]\(.*?\)",
    r"\[Citation.*?\]\(.*?\)",
    r"\[skip to.*?\]\(.*?\)",
    r"\[back to top\]\(.*?\)",
    r"\[Read more.*?\]\(.*?\)",
    r"PDF Version History",
    r"Version History",
    r"Cookie Policy",
    r"Privacy Policy",
    r"Terms of Service",

    # --- CRS Site Navigation & UI Controls ---
    r"\[Site Feedback\]\(.*?\)",
    r"\[Hide Overview\]\(.*?\)",
    r"\[Jump to Main Text of Report\]\(.*?\)",
    r"\[Close\]\(.*?\)",
    r"\|\s*\[\]\(.*?\)", # Catches empty linked table cells like "| [](https...)"
    
    # --- Report Version History Links ---
    # Matches: [December 30, 2024 (R48319 - Version: 4)](...pdf)
    r"\[.*?\(.*?-\s*Version:\s*\d+\)\]\(.*?\)",

    # --- Table of Contents Links (Optional) ---
    # Removes the markdown link but keeps the text if you want to strip the URL noise
    # If you want to remove the TOC lines entirely, use: r"- \[.*?\]\(.*?#_Toc\d+\)"
    r"\(https://www\.congress\.gov/crs-product.*?#_Toc\d+\)",

    # --- Footnotes ---
    # 1. Inline footnotes: [1](... "...")
    r"\[\d+\]\(https://www\.congress\.gov/crs-product.*?#fn\d+.*?\"\)",
    # 2. Footnote list anchors at the bottom: [1](...#ifn1)
    r"\[\d+\]\(https://www\.congress\.gov/crs-product.*?#ifn\d+\)",

    # --- Image & Media Placeholders ---
    # Removes markdown image tags like ![media/image4.png](...)
    r"!\[.*?\]\(.*?\)", 

    # --- Footer, Disclaimer, & Sign-in Boilerplate ---
    r"Disclaimer:\s*These documents were prepared by the Congressional Research Service[\s\S]*?wish to copy or otherwise use copyrighted material\.",
    r"Loading\.\.\.",
    r"Sign InClose",
    r"## Sign In",
    r"Email\s*Password\s*Remember Me",
    r"By using this system, you agree to comply with the \[Library's security requirements\]\(.*?\)\.",
    r"Sign in",
    r"\[Forgot password\??\]\(.*?\)",
    r"\[Create an account\]\(.*?\)",
    r"\[Contact sales\]\(.*?\)",
    r"\[Contact us\]\(.*?\)",
    r"#\s*Footnotes",
    r"\|[\s\xA0]*\|[\s\xA0]*\|",
    r"\|\s*---\s*\|\s*---\s*\|",
    r"\|\s*\.\s*\|.*?\|",
    r"##\s*References[\s\S]*"
]

    text = markdown

    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


try:
    query = "AI in Healthcare"
    max_results = 5
    searcher = web_searcher()
    results = searcher.search_web(query, max_results)

    firecrawl = Firecrawl(api_key=firecrawl_api_key)
    for result in results:

        # Scrape a website:
        doc = firecrawl.scrape(str(result.url),
            formats=["markdown"],
            only_main_content=True,)
        

        os.makedirs("output", exist_ok=True)
        article_id = str(result.url).rstrip('/').split('/')[-1]
        with open(f"output/{article_id}.md", "w", encoding="utf-8") as f:
            f.write(clean_markdown(doc.markdown))
        
except Exception as e:
    logging.error(f"An error occurred while searching the web: {str(e)}")
    raise CustomException(e, sys)

