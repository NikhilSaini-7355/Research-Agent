from uuid import UUID
from backend.core.context import current_project_id_var
from src.exception import CustomException
from src.logger import logging
import sys 
from backend.database.chroma_service import chroma_service
from Agents.synthesizer_agent import SynthesizerAgent

current_project_id_var.set(UUID('21111111-1111-1111-1111-111111111111'))

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

try:
    query = "Benefits AI has given to the US Citizens"
    result = chroma_service.retrieve_by_query(query,5)
    final_res = get_clean_results(result)
    synthesizer = SynthesizerAgent()
    final_ans = synthesizer.synthesize_chunks(topic="AI in USA", retrieved_data=final_res)
    for finding in final_ans.key_findings:
        print(f"🔹 {finding.theme}: {finding.fact}")
        print(f"   🔗 Source IDs: {finding.source_ids}\n")
        
except Exception as e:
    logging.error("An error occurred while generating personas.")
    print(CustomException(e, sys))