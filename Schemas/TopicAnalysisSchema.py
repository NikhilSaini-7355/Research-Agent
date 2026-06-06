from pydantic import BaseModel, Field
from typing import  Literal, List

class TopicAnalysisSchema(BaseModel):
    topic: str = Field(description="Write down the Exact Topic")
    domain: str = Field(description="Write down the Domain to which the given topic belongs")
    research_type: Literal["Exploratory","Comparative","Historical","Technical","Predictive","Business","Policy"] = Field(description="The type of research that can be conducted on the given topic (Exploratory, Comparative, Historical, Technical, Predictive, Business, Policy).")
    difficulty:  Literal["Easy", "Intermediate", "Hard"] = Field(description="The overall difficulty in researching on the given topic (Easy, Intermedate, Hard).")
    subtopics: List[str] = Field(min_length=3,max_length=10,description="List all the relevant subtopics related in and around the given topic.")
    keywords: List[str] = Field(min_length=3,max_length=15,description="List all the relevant keywords related in and around the given topic.")
    research_goals: List[str] = Field(description="List all the research goals which can be achieved by doing research on the topic.")