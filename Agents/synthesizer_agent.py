import sys 
from LLM.groq_client import llm
from Schemas.synthesizer_agent_schema import SynthesizedResearch
from Prompts.synthesizer_prompt import generate_synthesizer_prompt

from uuid import UUID
from backend.core.context import current_project_id_var
from src.exception import CustomException
from src.logger import logging
from backend.database.chroma_service import chroma_service


def get_clean_results(results_dict):
    # Chroma returns lists of lists. We grab [0] because we only sent one search query.
    ids = results_dict.get('ids', [[]])[0]
    documents = results_dict.get('documents', [[]])[0]
    scores = results_dict.get('scores', [[]])[0]

    res = []
    # zip() lets us loop through the IDs, Docs, and Scores all at the same time
    for rank, (chunk_id, doc, score) in enumerate(zip(ids, documents, scores), start=1):
        
        # Clean up the ugly markdown escape characters and excessive newlines
        clean_text = doc.replace('\r\n', '\n').replace('\\', '').strip()
        
        # Print a clean UI block for each chunk
        res.append({
            "id":chunk_id,
            "text":clean_text
        })
    
    return res

class SynthesizerAgent:

    def synthesize_chunks(
        self,
        topic: str,
        retrieved_data: list
    )->SynthesizedResearch:

        prompt = generate_synthesizer_prompt(
            topic=topic,
            retrieved_data=retrieved_data
        )

        structured_llm = llm.with_structured_output(
            SynthesizedResearch
        )

        result = structured_llm.invoke(
            prompt
        )

        return result
    def synthesize_research_summary(self, query: str, topic: str, project_id:str):
        result = chroma_service.retrieve_by_query(query, project_id, 5)
        final_res = get_clean_results(result)
        
        final_ans = self.synthesize_chunks(topic, retrieved_data=final_res)
        
        research_summary = []

        # Executive Summary
        research_summary.append("## Executive Summary")
        research_summary.append(final_ans.executive_summary)
        research_summary.append("")

        # Report Sections
        for section in final_ans.report_sections:

            research_summary.append(f"## {section.section_title}")

            for point in section.detailed_points:
                research_summary.append(f"- {point}")

            research_summary.append(
                f"Sources: {', '.join(section.source_ids)}"
            )

            research_summary.append("")

        # Final string for Outline Generator
        research_summary = "\n".join(research_summary)

        return research_summary

