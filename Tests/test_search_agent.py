import os
import re
from Agents.search_agent import web_searcher
from src.exception import CustomException
from src.logger import logging
from dotenv import load_dotenv
# Load environment variables from .env file

load_dotenv()
from pprint import pprint
firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")

import sys

from src.exception import CustomException
from src.logger import logging
import sys 
import json
from Agents.search_query_generator import SearchQueryGenerator
from Agents.persona_generator import PersonaGenerator
from Agents.question_generator_agent import question_generator_agent
from Agents.questions_dedup_agent import QuestionDeduplicator
from Agents.TopicAnalyzerAgent import TopicAnalyzerAgent

TopicAnalyzerObj = TopicAnalyzerAgent()

topic =  "Explain Model Predictive Control"

analysis_response = TopicAnalyzerObj.analyze(topic)

try:
    generator = PersonaGenerator()
    personas = generator.generate_persona(analysis_response)
    expert = personas.experts[0]

    generator = question_generator_agent()
    all_questions = []

    for expert in personas.experts:

        questions = generator.generate_questions(
            topic=topic,
            expert=expert
        )
    
        all_questions.extend(
            questions.questions
        )
    deduper = QuestionDeduplicator()

    refined_questions = deduper.deduplicate(
        topic,
        all_questions
    )
    
    generator = SearchQueryGenerator()
    all_queries = []

    for question in refined_questions.questions:
        result = generator.generate_queries(
        topic= topic,
        question=question
    )
        all_queries.extend(result.queries)

    unique_queries = list(
    dict.fromkeys(all_queries)
    )
    searcher = web_searcher()

    all_results = []

    for query in unique_queries:
    
        try:
            results = searcher.search_web(
                query=query,
                max_results=3
            )
    
            all_results.extend(results)
    
        except Exception as e:
            print(f"Search failed for query: {query}")
            print(e)
    print(f"\nTotal Results: {len(all_results)}")

    for result in all_results:
    
        print("\n" + "=" * 80)
    
        print(f"TITLE: {result.title}")
        print(f"URL: {result.url}")
    
        if hasattr(result, "score"):
            print(f"SCORE: {result.score}")
except Exception as e:
    logging.error(f"An error occurred while searching the web: {str(e)}")
    raise CustomException(e, sys)