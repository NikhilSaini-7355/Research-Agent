import asyncio
import re
import os
import sys
import urllib.parse
import requests
from typing import List

from dotenv import load_dotenv

load_dotenv()

browserbase_api_key = os.getenv("BROWSERBASE_API_KEY")
browserbase_project_id = os.getenv("BROWSERBASE_PROJECT_ID")

# Crawl4AI v0.8.9 Imports
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

def fetch_with_jina_fallback(url: str) -> str:
    """Uses Jina AI's Reader API to bypass hard CAPTCHAs when Crawl4AI is blocked."""
    print(f"     [!] Triggering Jina API Fallback for {url}...")
    try:
        # Prepend the Jina Reader endpoint to the target URL
        response = requests.get(f"https://r.jina.ai/{url}", timeout=20)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"     [X] Jina fallback failed: {e}")
    return ""

def clean_extracted_markdown(text: str) -> str:
    """Strips out top metadata, trailing references, and all images."""
    if not text:
        return ""
        
    # --- 1. TRIM THE TOP (Headers, Authors, Affiliations) ---
    start_markers = [
        r"^##?\s+Abstract", 
        r"^##?\s+Introduction", 
        r"^##?\s+Background",
        r"^##?\s+Summary"
    ]
    start_pattern = "|".join(start_markers)
    start_match = re.search(start_pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    
    if start_match:
        text = text[start_match.start():]
        
    # --- 2. TRIM THE BOTTOM (References, Citations) ---
    cutoff_markers = [
        r"\n##?\s+References", 
        r"\n##?\s+Bibliography", 
        r"\n##?\s+Sources", 
        r"\n##?\s+Footnotes",
        r"\n##?\s+Conflicts\s+of\s+Interest", 
        r"\n##?\s+Acknowledgments",
        r"\n##?\s+Author\s+information"
    ]
    end_pattern = "|".join(cutoff_markers)
    end_match = re.search(end_pattern, text, flags=re.IGNORECASE)
    
    if end_match:
        text = text[:end_match.start()]
        
    # --- 3. STRIP ALL MARKDOWN IMAGES ---
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
        
    return re.sub(r'\n{3,}', '\n\n', text).strip()

async def extract_web_content(urls: List[str]) -> dict:
    """
    Crawls a list of URLs and returns a dictionary mapping each URL to its cleaned Markdown.
    """
    extracted_data = {}
    ws_url = f"wss://connect.browserbase.com?apiKey={browserbase_api_key}&projectId={browserbase_project_id}"
    # 1. Setup the Headless Browser
    browser_config = BrowserConfig(
        browser_mode="custom",  # Tells Crawl4AI not to launch a local browser
        cdp_url=ws_url          # Connects directly to the Browserbase cloud
    )
    
    # 2. Setup the Markdown Generator
    md_generator = DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.4)
    )
    
    # 3. Setup the Crawler Run Config (Maximum Stealth)
    # 3. Setup the Crawler Run Config (Maximum Stealth)
    run_config = CrawlerRunConfig(
        word_count_threshold=200,
        cache_mode=CacheMode.BYPASS,  # <--- THE FIX: Ignore the old blocked files!
        excluded_tags=['nav', 'footer', 'header', 'aside', 'form', 'img', 'picture', 'svg'],
        exclude_external_links=True,
        remove_overlay_elements=True,
        markdown_generator=md_generator,
        css_selector="main, article, .main-content, #main-content, .article-body",
        
        # Anti-Bot & Stealth Configuration
        magic=True,
        simulate_user=True,
        override_navigator=True,
        delay_before_return_html=12.0, 
        page_timeout=60000 
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        for raw_url in urls:
            url = str(raw_url).strip() 
            if not url:
                continue
                
            try:
                print(f"Scraping: {url}...")
                result = await crawler.arun(url=url, config=run_config)
                
                raw_markdown = ""
                
                if result.success:
                    # 1. Check for security keywords
                    lower_md = result.markdown.lower()
                    security_keywords = [
                        "recaptcha", 
                        "security verification", 
                        "verifies you are not a bot", 
                        "enable javascript and cookies"
                    ]
                    found_keyword = any(keyword in lower_md for keyword in security_keywords)
                    
                    # 2. Check document length
                    # A security block page is tiny. A real article is massive.
                    is_suspiciously_short = len(result.markdown) < 1500
                    
                    # 3. ONLY trigger the wall if BOTH conditions are true
                    if (found_keyword and is_suspiciously_short) or len(result.markdown) < 200:
                        print("     [!] Real Security Wall Detected. Triggering Fallback...")
                        raw_markdown = await asyncio.to_thread(fetch_with_jina_fallback, url)
                    else:
                        # If it has a keyword but is thousands of characters long, it's a false positive!
                        raw_markdown = result.markdown
                else:
                    print(f"     [X] Crawl4AI Failed: {result.error_message}")
                    # Trigger Fallback on complete failure
                    raw_markdown = await asyncio.to_thread(fetch_with_jina_fallback, url)
                
                # Clean the final text regardless of which tool fetched it
                if raw_markdown:
                    cleaned_text = clean_extracted_markdown(raw_markdown)
                    if cleaned_text:
                        extracted_data[url] = cleaned_text
                        print("     [+] Successfully extracted content.")
                    
            except Exception as e:
                print(f"Error processing {url}: {e}")
                
    return extracted_data

if __name__ == "__main__":
    from src.agents.search_agent import web_searcher
    from src.exception import CustomException
    from src.logger import logging
    
    try:
        query = "AI in Defense: Recent Advances and Future Trends"
        max_results = 5
        searcher = web_searcher()
        results = searcher.search_web(query, max_results)

        urls = [result.url for result in results]
        
        # Run the async function
        extracted_results = asyncio.run(extract_web_content(urls))

        # Ensure output directory exists
        os.makedirs("output", exist_ok=True)
        print("\n====================")

        for i, (url, content) in enumerate(extracted_results.items(), start=1):
            
            # Format a safe filename
            parsed_url = urllib.parse.urlparse(url)
            domain = parsed_url.netloc.replace("www.", "")
            safe_domain_name = re.sub(r'[^a-zA-Z0-9]', '_', domain)
            
            filename = f"output/source_{i}_{safe_domain_name}.md"
            
            # Write to file
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"### Source: {url}\n\n")
                f.write(content)
                
            print(f"Saved: {filename}")

    except Exception as e:
        logging.error(f"An error occurred while searching the web: {str(e)}")
        raise CustomException(e, sys)