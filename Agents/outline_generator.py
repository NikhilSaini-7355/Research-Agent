from dotenv import load_dotenv

from LLM.groq_client import llm
from langchain_core.output_parsers import PydanticOutputParser

from Schemas.outline_schema import OutlineSchema
from Prompts.outline_generator_prompt import OUTLINE_PROMPT

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