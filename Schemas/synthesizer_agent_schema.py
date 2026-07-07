from pydantic import BaseModel, Field
from typing import List

class KeyFinding(BaseModel):
    theme: str = Field(description="The overarching category of the finding, e.g., 'Degradation Mechanisms'")
    fact: str = Field(description="A concise, factual summary of the retrieved information.")
    source_ids: List[str] = Field(description="A list of ChromaDB chunk IDs that prove this fact.")

class SynthesizedResearch(BaseModel):
    primary_topic: str = Field(description="The main subject being researched.")
    executive_summary: str = Field(description="A 3-4 sentence overview of the gathered research.")
    key_findings: List[KeyFinding] = Field(description="A curated list of the most important facts gathered from the documents.")