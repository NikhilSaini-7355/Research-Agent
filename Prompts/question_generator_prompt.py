from langchain_core.prompts import ChatPromptTemplate
from Schemas.PersonaGeneratorSchema import ExpertRolesSchema, ExpertPersona

QuestionGeneratorTemplate = ChatPromptTemplate([
    ('system', "You are a senior research analyst."),
    ('human', """Topic: {Topic}
            
    role: {role}
    perspective: {perspective}

    Generate 5 important research questions that this specific persona would ask regarding the topic.
    
    Requirements:
    - Questions must be highly relevant to the persona's specific expertise.
    - Keep questions concise (maximum 1-2 sentences each).
    - Do not include any explanations or markdown formatting.
    """)
])

def generate_questions_prompt(topic: str, role:str, perspective:str) -> str:
    prompt = QuestionGeneratorTemplate.invoke({'Topic': topic, 'role': role, 'perspective': perspective})
    return prompt
