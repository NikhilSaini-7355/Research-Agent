from pydantic import BaseModel, Field, HttpUrl
from typing import List,Optional

class SearchResult(BaseModel):
    """Schema representing a single web search result."""
    title: str = Field(
        ..., 
        description="The headline or title of the web page/article."
    )
    url: str = Field(
        ..., 
        description="The valid URL link to the source."
    )
    
    raw_content: Optional[str] = Field(
        default=None,
        description="The raw HTML content of the page fetched by Tavily. Passed to Trafilatura for markdown extraction."
    )
    score: Optional[float] = Field(
        default=None,
        description="The relevance score of the search result."
    )

class SearchResponse(BaseModel):
    """Schema representing the complete output from the search agent."""
    query: str = Field(
        ..., 
        description="The original search query that was executed."
    )
    results: List[SearchResult] = Field( #type: ignore
        default_factory=list,
        description="A list containing the individual search results."
    )
    response_time: Optional[float] = Field(
        default=None,
        description="The total time taken for the search response, typically in seconds."
    )