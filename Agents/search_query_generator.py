from LLM.groq_client import llm

from Schemas.search_query_schema import (
    SearchQuerySchema
)

from Prompts.search_query_prompt import (
    generate_search_query_prompt
)


class SearchQueryGenerator:

    def generate_queries(
        self,
        topic: str,
        question: str
    ):

        prompt = generate_search_query_prompt(
            topic=topic,
            question=question
        )

        structured_llm = llm.with_structured_output(
            SearchQuerySchema
        )

        result = structured_llm.invoke(
            prompt
        )

        return result