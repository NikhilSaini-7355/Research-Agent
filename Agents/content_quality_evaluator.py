from Schemas.content_quality_schema import (
    ContentQualitySchema
)

from Prompts.content_quality_prompt import (
    generate_quality_prompt
)

from LLM.groq_client import llm


class ContentQualityEvaluator:

    def evaluate(
        self,
        content: str
    ):

        prompt = generate_quality_prompt(
            content
        )

        structured_llm = (
            llm.with_structured_output(
                ContentQualitySchema
            )
        )

        result = structured_llm.invoke(
            prompt
        )

        return result