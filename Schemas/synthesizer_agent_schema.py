from pydantic import BaseModel, Field
from typing import List

class ReportSection(BaseModel):
    section_title: str = Field(description="A descriptive, overarching heading for this section of the report (e.g., 'Primary Degradation Mechanisms').")
    detailed_points: List[str] = Field(description="A detailed, point-by-point breakdown of the facts, arguments, and insights belonging to this section. Do not summarize too broadly; preserve specific details.")
    source_ids: List[str] = Field(description="A list of ChromaDB chunk IDs that prove the points in this section.")

class SynthesizedResearch(BaseModel):
    primary_topic: str = Field(description="The main subject being researched.")
    executive_summary: str = Field(description="A 3-4 sentence overview of the gathered research.")
    report_sections: List[ReportSection] = Field(description="A curated, sequentially organized list of thematic sections that make up the point-by-point report.")