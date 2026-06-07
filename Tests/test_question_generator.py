from src.exception import CustomException
from src.logger import logging
import sys 
import json

from Agents.question_generator_agent import question_generator_agent
from Agents.persona_generator import persona_generator

Topic =  "India vs China economic comparison"

subtopics = [
    "GDP Comparison",
    "Trade Relations",
    "Investment Climate",
    "Poverty Alleviation",
    "Infrastructure Development",
    "Economic Reforms"
  ]

try:
    generator = persona_generator()
    personas = generator.generate_persona(Topic, subtopics)

    expert1 = personas.expert_1
    generator = question_generator_agent()
    questions = generator.generate_questions(Topic="AI in Healthcare ", role=expert1.role, perspective=expert1.perspective)
    
    logging.info("Question generation completed successfully.")
    print(json.dumps(questions, indent=2))

except Exception as e:
    logging.error("An error occurred while generating questions.")
    print(CustomException(e, sys))