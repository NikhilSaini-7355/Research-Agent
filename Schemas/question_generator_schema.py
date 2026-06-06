from pydantic import BaseModel, Field
from typing import List

class QuestionGeneratorSchema(BaseModel):
    questions: List[str] = Field(
        description="A list of exactly 5 research questions asked by the persona."
    )