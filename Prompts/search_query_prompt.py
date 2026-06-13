from langchain_core.prompts import ChatPromptTemplate


SearchQueryGeneratorTemplate = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert research librarian.

            Convert the given research question into
            EXACTLY 3 optimized search queries.

            Requirements:

            - Use technical terminology.
            - Keep queries concise.
            - Focus on authoritative and academic sources.
            - Each query should explore a different aspect.
            - Do not return complete sentences.
            - Do not include quotation marks.
            - Return search-engine friendly queries.
            """
        ),
        (
            "human",
            """
            Topic:
            {topic}

            Research Question:
            {question}
            """
        )
    ]
)


def generate_search_query_prompt(
    topic: str,
    question: str
):
    return SearchQueryGeneratorTemplate.invoke(
        {
            "topic": topic,
            "question": question
        }
    )