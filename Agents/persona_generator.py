from LLM.groq_client import llm
from Prompts.PersonaGeneratorPrompt import generate_persona_prompt
from Schemas.PersonaGeneratorSchema import ExpertRolesSchema
import json

class persona_generator:

    def generate_persona(self,Topic, subtopic):

        prompt = generate_persona_prompt(Topic, subtopic)

        structured_llm = llm.with_structured_output(ExpertRolesSchema)

        result = structured_llm.invoke(prompt)

        return result.model_dump()