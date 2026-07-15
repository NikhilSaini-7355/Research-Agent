from dotenv import load_dotenv

from LLM.groq_client import llm
from langchain_core.output_parsers import PydanticOutputParser

from Schemas.outline_schema import OutlineSchema
from Prompts.outline_generator_prompt import OUTLINE_PROMPT

from Schemas.all_db_schemas import ArticleCreate
from backend.database.crud_agents import crud_article
from backend.database.database_session import AsyncSessionLocal
import uuid

from src.exception import CustomException
from src.logger import logging
import sys

load_dotenv()


class OutlineGenerator:

    def __init__(self):

        self.llm = llm

        self.parser = PydanticOutputParser(
            pydantic_object=OutlineSchema
        )

    def generate_outline(self, research_summary: str):

        prompt = OUTLINE_PROMPT.format_messages(
            research_summary=research_summary,
            format_instructions=self.parser.get_format_instructions()
        )

        response = self.llm.invoke(prompt)

        outline = self.parser.parse(response.content)

        return outline

    async def save_outline(self, project_id: str, outline: OutlineSchema):
        project_id = uuid.UUID(project_id)
        generated_outline = outline.model_dump()
        async with AsyncSessionLocal() as session:
            try:
                article_data = ArticleCreate(
                    project_id=project_id,
                    outline = generated_outline,
                )
                await crud_article.create(db=session, obj_in=article_data)
            except Exception as e:
                logging.error(f"An error occurred while saving the outline: {str(e)}")
                await session.rollback()
                raise CustomException(e, sys)
