from langchain_core.output_parsers import PydanticOutputParser
from Schemas.questions_dedup_schema import RefinedQuestionSchema
from Prompts.questions_dedup_prompt import generate_dedup_prompt
from LLM.groq_client import llm

class QuestionDeduplicator:

    def __init__(self):
        self.parser = PydanticOutputParser(
            pydantic_object=RefinedQuestionSchema
        )

    def deduplicate(self, topic: str, questions: list[str] ):

        prompt = generate_dedup_prompt(
            topic,
            questions,
            self.parser.get_format_instructions()
        )

        response = llm.invoke(prompt)

        return self.parser.parse(response.content)