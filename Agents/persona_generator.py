from LLM.groq_client import llm
from Prompts.PersonaGeneratorPrompt import generate_persona_prompt
from Schemas.PersonaGeneratorSchema import ExpertRolesSchema
import json

class PersonaGenerator:

    def generate_persona(self, topic_analysis):

        prompt = generate_persona_prompt(
            topic=topic_analysis.topic,
            domain=topic_analysis.domain,
            difficulty=topic_analysis.difficulty,
            subtopics=topic_analysis.subtopics,
            keywords=topic_analysis.keywords,
            research_goals=topic_analysis.research_goals
        )

        structured_llm = llm.with_structured_output(
            ExpertRolesSchema
        )

        personas = structured_llm.invoke(prompt)

        return personas