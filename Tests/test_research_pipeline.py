from src.agents.TopicAnalyzerAgent import TopicAnalyzerAgent
from src.agents.persona_generator import persona_generator
from src.agents.search_agent import web_searcher
from src.agents.question_generator import generate_questions

from src.exception import CustomException
from src.logger import logging

import os 
import sys

topic_analyzer = TopicAnalyzerAgent()
persona_gen = persona_generator()
search_agent = web_searcher()

input_topic = "The impact of AI on healthcare"

try:
    analysis = topic_analyzer.analyze(input_topic)
    print("Topic Analysis:")
    print(analysis)

    personas = persona_gen.generate_persona(analysis.topic, analysis.subtopics)
    print("Generated Persona:")
    print(personas)

    for persona in personas:

        print(f"\n{'='*60}")
        print(f"PERSONA: {persona}")
    
        questions = generate_questions(
            topic=input_topic,
            persona=persona
        )
    
        for question in questions:
    
            print(f"\nQUESTION: {question}")
    
            results = search_agent.search_web(question)
    
            print(f"RESULTS FOUND: {len(results)}")
    
            if results:
                print("TOP RESULT:")
                print(results[0]["title"])
                print(results[0]["url"])
except Exception as e:
    logging.error(f"An error occurred in the research pipeline: {str(e)}")
    raise CustomException(e, sys)
