from pydantic import BaseModel, Field


class OutlineSchema(BaseModel):
    title: str = Field(description="Title of the review paper")
    sections: list[str] = Field(
        description="Ordered list of section headings"
    )