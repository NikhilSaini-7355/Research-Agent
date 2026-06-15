from LLM.groq_client import llm
from Prompts.question_generator_prompt import generate_questions_prompt
from Schemas.question_generator_schema import QuestionSchema
import json

class question_generator_agent:
    def generate_questions(self,topic,expert):
        prompt = generate_questions_prompt(
            topic = topic,
            role = expert.role,
            expertise = expert.expertise,
            research_dimension = expert.research_dimension,
            perspective = expert.perspective
        )
        structured_llm = llm.with_structured_output(QuestionSchema)
        result = structured_llm.invoke(prompt)
        return result

