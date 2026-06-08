from Schemas.search_agent_schema import SearchResponse
from tavily import TavilyClient
from dotenv import load_dotenv
import asyncio
import aiohttp
import os
import re

load_dotenv()

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

    def clean_rag_markdown(self, text: str) -> str:
        """A data janitor function to sanitize Markdown before embedding."""
        if not text:
            return ""
            
        # 1. Remove academic citation links entirely: [[1](https://...)]
        text = re.sub(r'\[\[.*?\]\(.*?\)\]', '', text)
        
        # 2. Flatten standard Markdown Links (Keep the text, delete the URL): [Click Here](https://...) -> Click Here
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        
        # 3. Strip Cloudflare / Bot Wall noise
        bot_phrases = [
            "Checking your browser before accessing",
            "Click here if you are not automatically redirected",
            "Cloudflare JS challenge",
            "This article has multiple issues", 
            "Please help improve it"
        ]
        for phrase in bot_phrases:
            text = text.replace(phrase, "")
            
        # 4. Clean up multiple empty lines left behind
        text = re.sub(r'\n\s*\n', '\n\n', text)
        
        return text.strip()

    async def _fetch_jina_url(self, session: aiohttp.ClientSession, result_obj, bot_keywords: list) -> dict:
        """Worker function to process an individual URL with Jina Reader API."""
        url = str(result_obj.url)
        tavily_fallback_snippet = result_obj.content
        jina_url = f"https://r.jina.ai/{url}"
        
        headers = {
            "X-Return-Format": "markdown"
        }
        
        # Optional: Add Jina Token if available in environment variables to prevent rate-limiting
        jina_api_key = os.getenv("JINA_API_KEY")
        if jina_api_key:
            headers["Authorization"] = f"Bearer {jina_api_key}"
            
        try:
            async with session.get(jina_url, headers=headers, timeout=15) as response:
                if response.status == 200:
                    extracted_text = await response.text()
                    
                    # Check if the text matches any known anti-bot defense page signatures
                    is_bot_wall = any(kw in extracted_text.lower() for kw in bot_keywords) if extracted_text else True
                    
                    if extracted_text and not is_bot_wall:
                        return {
                            "url": url,
                            "content": self.clean_rag_markdown(extracted_text), 
                            "status": "success (Jina API)"
                        }
                    else:
                        status_msg = "fallback to Tavily (Detected Bot Wall)" if is_bot_wall else "fallback to Tavily (Empty Content)"
                        return {
                            "url": url,
                            "content": self.clean_rag_markdown(tavily_fallback_snippet),
                            "status": status_msg
                        }
                else:
                    return {
                        "url": url,
                        "content": self.clean_rag_markdown(tavily_fallback_snippet),
                        "status": f"fallback to Tavily (Jina HTTP {response.status})"
                    }
        except Exception as e:
            return {
                "url": url,
                "content": self.clean_rag_markdown(tavily_fallback_snippet),
                "status": f"fallback to Tavily (Blocked/Error: {str(e)})"
            }

    async def extract_content_with_crawl4ai(self, search_results: list) -> list[dict]:
        """Takes Tavily search results and concurrently extracts clean Markdown using Jina API.
        
        Maintains structural function name compatibility for downstream pipeline nodes.
        """
        bot_keywords = [
            "checking your browser",
            "recaptcha/challenge",
            " please turn on javascript",
            "security check to access",
            "attention required! | cloudflare"
        ]
        
        async with aiohttp.ClientSession() as session:
            tasks = [self._fetch_jina_url(session, res, bot_keywords) for res in search_results]
            cleaned_results = await asyncio.gather(*tasks)
            
        return list(cleaned_results)