import os
import re
import sys
import json

from Agents.extractor_agent import ContentExtractor
from Agents.search_agent import web_searcher
from Agents.search_query_generator import SearchQueryGenerator
from Agents.persona_generator import PersonaGenerator
from Agents.question_generator_agent import question_generator_agent
from Agents.questions_dedup_agent import QuestionDeduplicator
from Agents.TopicAnalyzerAgent import TopicAnalyzerAgent

from src.exception import CustomException
from src.logger import logging
from src.config.sources import allowed_domains
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()

firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")

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
    HIGH_SCORE_THRESHOLD = 0.75

    filtered_results = []

    for result in all_results:


        score = getattr(result, "score", 0.0)

        is_high_score = (
            score is not None
            and score >= HIGH_SCORE_THRESHOLD
        )

        if is_high_score:
            filtered_results.append(result)
    print(f"Original URLs: {len(all_results)}")
    print(f"Filtered URLs: {len(filtered_results)}")

    print(f"Extracting the contents...")
    extractor = ContentExtractor()
    extractor.extract_content(filtered_results)
    print(f"extraction  is completed.")
    
except Exception as e:
    logging.error(f"An error occurred while searching the web: {str(e)}")
    raise CustomException(e, sys)