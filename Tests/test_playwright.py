from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth  # <-- New import
import trafilatura

url = "https://www.myneta.info/WestBengal2026/index.php?action=show_winners&sort=default"


def fetch_and_extract(url):
    # Wrap the Playwright context manager with the Stealth class
    with Stealth().use_sync(sync_playwright()) as p:
        
        # Launch Chromium invisibly
        browser = p.chromium.launch(headless=True)
        
        # All pages spawned here automatically have anti-bot evasions applied
        page = browser.new_page() 
        
        # Go to the URL and wait for the page to fully load
        page.goto(url, wait_until="networkidle")
        
        # Grab the raw HTML after the JS challenges are solved
        raw_html = page.content()
        browser.close()
        
        print(raw_html)  # Print the first 1000 characters of the raw HTML for verification
        # Pass the HTML to Trafilatura
        # clean_markdown = trafilatura.extract(raw_html, output_format="markdown")
        # return clean_markdown

print(fetch_and_extract(url))