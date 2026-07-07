from dotenv import load_dotenv

from LLM.groq_client import llm
from langchain_core.output_parsers import PydanticOutputParser

from Schemas.writer_schema import SectionSchema
from Prompts.writer_prompt import WRITER_PROMPT

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