import os
import re
import sys
import json
import asyncio
import uuid
from typing import List, Dict, Any

from backend.database.database_session import AsyncSessionLocal
from backend.database.chroma_service import chroma_service

from Agents.synthesizer_agent import SynthesizerAgent
from Agents.extractor_agent import ContentExtractor
from Agents.search_agent import web_searcher
from Agents.search_query_generator import SearchQueryGenerator
from Agents.persona_generator import PersonaGenerator
from Agents.question_generator_agent import question_generator_agent
from Agents.questions_dedup_agent import QuestionDeduplicator
from Agents.TopicAnalyzerAgent import TopicAnalyzerAgent
from Agents.embedding_agent import process_pending_embeddings
from Agents.outline_generator import OutlineGenerator
from Agents.writer import WriterAgent

from src.utils.pdf_generator import save_markdown_as_pdf
from src.exception import CustomException
from src.logger import logging
from src.config.sources import allowed_domains
from dotenv import load_dotenv
from Schema.workflow_state_schema import WorkflowState

load_dotenv()

def get_context(results_dict):

    docs = results_dict.get("documents", [[]])[0]

    context = []

    for doc in docs:
        clean = (
            doc.replace("\r\n", "\n")
               .replace("\\", "")
               .strip()
        )

        context.append(clean)

    return "\n\n".join(context)



def topic_analyzer_node(state: WorkflowState) -> WorkflowState:
    try:
        TopicAnalyzerObj = TopicAnalyzerAgent()
        topic = state["topic"]
        analysis_response = TopicAnalyzerObj.analyze(topic)
    except Exception as e:
        logging.error(f"An error occurred while analyzing the topic: {str(e)}")
        raise CustomException(e, sys)
    return {
            "topic_analysis_response": analysis_response
        }

def persona_generator_node(state: WorkflowState) -> WorkflowState:
    try:
        generator = PersonaGenerator()
        topic_analysis_response = state["topic_analysis_response"]
        personas = generator.generate_persona(topic_analysis_response)
    except Exception as e:
        logging.error(f"An error occurred while generating personas: {str(e)}")
        raise CustomException(e, sys)
    return {
        "personas": personas
    }

def question_generator_node(state: WorkflowState) -> WorkflowState:
    try:
        generator = question_generator_agent()
        all_questions = []
        topic = state["topic"]
        personas = state["personas"]
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

    except Exception as e:
        logging.error(f"An error occurred while generating questions: {str(e)}")
        raise CustomException(e, sys)

    return {
        "search_queries": unique_queries
    }

def search_node(state: WorkflowState) -> WorkflowState:
    try:
        searcher = web_searcher()
        all_results = []
        unique_queries = state["search_queries"]
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

    except Exception as e:
        logging.error(f"An error occurred while searching the queries: {str(e)}")
        raise CustomException(e, sys)

    return {
        "search_results": filtered_results
    }       

def content_extractor_node(state: WorkflowState) -> WorkflowState:
    try:
        print(f"Extracting the contents...")
        extractor = ContentExtractor()
        filtered_results = state["search_results"]
        extractor.extract_content(filtered_results)
        print(f"extraction  is completed.")
    except Exception as e:
        logging.error(f"An error occurred while extracting content: {str(e)}")
        raise CustomException(e, sys)
    return {}

async def embedder_node(state: WorkflowState) -> WorkflowState:
    async with AsyncSessionLocal() as session:
        try:
            target_project_id = uuid.UUID(state["project_id"])
            await process_pending_embeddings(db=session, project_id=target_project_id)
            
        except Exception as e:
            logging.error(f"An error occurred while processing embeddings: {str(e)}")
            await session.rollback()
    
    return {}

def synthesizer_node(state: WorkflowState) -> WorkflowState:
    try:
        topic = state["topic"]
        query = f"Comprehensive research summary for the topic: {topic}"
        synthesizer = SynthesizerAgent()
        research_summary = synthesizer.synthesize_research_summary(query, topic)

    except Exception as e:
        logging.error(f"An error occurred while synthesizing the research summary: {str(e)}")
        raise CustomException(e, sys)

    return {
        "research_summary": research_summary
    }

def outline_generator_node(state: WorkflowState) -> WorkflowState:
    try:
        generator = OutlineGenerator()
        research_summary = state["research_summary"]
        outline = generator.generate_outline(research_summary)

    except Exception as e:
        logging.error(f"An error occurred while generating the outline: {str(e)}")
        raise CustomException(e, sys)

    return {
        "outline": outline
    }

def writer_node(state: WorkflowState) -> WorkflowState:
    try:
        writer = WriterAgent()
        paper = []
        project_id = state["project_id"]
        topic = state["topic"]
        outline = state["outline"]
        paper.append(f"# {outline.title}\n")
        for section in outline.sections:
            retrieval_query = f"{topic} {section}"
            retrieved = chroma_service.retrieve_by_query(
                retrieval_query,
                5
            )
            context = get_context(retrieved)
            section_result = writer.write_section(
                section=section,
                context=context
            )
            paper.append(f"## {section_result.section_title}\n")
            paper.append(section_result.content)
            paper.append("\n")
        # -----------------------------
        # Final Markdown
        # -----------------------------
        final_markdown = "\n".join(paper)

        save_markdown_as_pdf(
            markdown_text=final_markdown,
            filename=f"Research_Paper_{project_id}.pdf"
        )

    except Exception as e:
        logging.error(f"An error occurred while writing the research paper: {str(e)}")
        raise CustomException(e, sys)

    return {
        "final_markdown": final_markdown
    }



# db interaction
# async session passage
# project id, user id passage, etc
