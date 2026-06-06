from src.exception import CustomException
from src.logger import logging
import sys 
import json

from Agents.question_generator_agent import question_generator_agent

try:
    generator = question_generator_agent()
    questions = generator.generate_questions(Topic="AI in Healthcare ", persona="Doctor")
    logging.info("Question generation completed successfully.")
    print(json.dumps(questions, indent=2))

except Exception as e:
    logging.error("An error occurred while generating questions.")
    print(CustomException(e, sys))