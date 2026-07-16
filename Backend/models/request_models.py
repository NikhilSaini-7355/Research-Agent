from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    topic: str = Field(
        ...,
        description="Research topic provided by the user"
    )