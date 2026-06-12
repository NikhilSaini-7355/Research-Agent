from Schemas.questions_dedup_schema import RefinedQuestionSchema
from Prompts.questions_dedup_prompt import generate_dedup_prompt
from LLM.groq_client import llm

class QuestionDeduplicator:

    def deduplicate(self, topic: str, questions: list[str] ):

        prompt = generate_dedup_prompt(
            topic,
            questions
        )

        structured_llm = (
            llm.with_structured_output(
                RefinedQuestionSchema
            )
        )

        result = structured_llm.invoke(
            prompt
        )

        return result