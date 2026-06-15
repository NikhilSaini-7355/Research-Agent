from pydantic import BaseModel, Field
from typing import List


class RefinedQuestionSchema(BaseModel):
    questions: List[str] = Field(
        description="Deduplicated research questions"
    )