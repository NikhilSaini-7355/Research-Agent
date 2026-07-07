from pydantic import BaseModel, Field


class SectionSchema(BaseModel):
    section_title: str = Field(
        description="Title of the section"
    )

    content: str = Field(
        description="Technical content of the section"
    )