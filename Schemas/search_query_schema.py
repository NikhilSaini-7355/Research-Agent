from pydantic import BaseModel, Field
from typing import List


class SearchQuerySchema(BaseModel):
    queries: List[str] = Field(
        description="""
        List of optimized web search queries derived
        from the research question.
        Generate exactly 3 queries.
        """
    )