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

    print(f"Total Queries: {len(unique_queries)}")
    
    for q in unique_queries:
        print(q)
    
except Exception as e:
    logging.error("An error occurred while generating personas.")
    print(CustomException(e, sys))