from dotenv import load_dotenv

from LLM.groq_client import llm
from langchain_core.output_parsers import PydanticOutputParser

from Schemas.writer_schema import SectionSchema
from Prompts.writer_prompt import WRITER_PROMPT

from Schemas.all_db_schemas import ArticleCreate
from backend.database.crud_agents import crud_article
from backend.database.database_session import AsyncSessionLocal
import uuid

load_dotenv()


class WriterAgent:

    def __init__(self):

        self.llm = llm

        self.parser = PydanticOutputParser(
            pydantic_object=SectionSchema
        )

    def write_section(
        self,
        section: str,
        context: str
    ):

        prompt = WRITER_PROMPT.format_messages(
            section=section,
            context=context,
            format_instructions=self.parser.get_format_instructions()
        )

        response = self.llm.invoke(prompt)

        return self.parser.parse(response.content)

    async def save_generated_article(self, project_id: str, final_markdown: str, research_summary: str):
        async with AsyncSessionLocal() as session:
            existing_article = await crud_article.get_by_project(
            db=session, 
            project_id=uuid.UUID(str(project_id))
            )   

            if not existing_article:
                print("❌ Article not found. Cannot update.")
                return

            update_data = {"final_content": final_markdown, "draft_content":research_summary}

            updated_article = await crud_article.update(
            db=session,
            db_obj=existing_article, # <--- Here is how it knows what to update!
            obj_in=update_data       # <--- Here is the new data
            )
            
            print("✅ Successfully updated!")


