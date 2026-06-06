from LLM.groq_client import llm
from Prompts.question_generator_prompt import generate_questions_prompt
from Schemas.question_generator_schema import QuestionGeneratorSchema
import json

class question_generator_agent:
    def generate_questions(self,Topic, role, perspective):
        prompt = generate_questions_prompt(Topic, role, perspective)
        structured_llm = llm.with_structured_output(QuestionGeneratorSchema)
        result = structured_llm.invoke(prompt)
        return result.model_dump()


