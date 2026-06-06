from langchain_core.prompts import ChatPromptTemplate

PersonaGeneratorTemplate = ChatPromptTemplate([
    ('system', "You are a senior research analyst."),
    ('human', """Topic: {Topic}
            
    Subtopics: {subtopic}

    Generate 5 expert personas with distinct viewpoints relevant to the topic.

    Requirements:
    - Roles must be professional expert roles, not specific real people.
    - Each role should represent a unique perspective.
    - Perspectives should be maximum 1 or 2 sentences.
    """)
])

def generate_persona_prompt(topic: str, subtopic: str) -> str:
    prompt = PersonaGeneratorTemplate.invoke({'Topic': topic, 'subtopic': subtopic})
    return prompt