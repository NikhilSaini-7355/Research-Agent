from uuid import UUID
from backend.core.context import current_project_id_var
from src.exception import CustomException
from src.logger import logging
import sys 
from backend.database.chroma_service import chroma_service

current_project_id_var.set(UUID('21111111-1111-1111-1111-111111111111'))

def print_clean_results(results_dict):
    # Chroma returns lists of lists. We grab [0] because we only sent one search query.
    ids = results_dict.get('ids', [[]])[0]
    documents = results_dict.get('documents', [[]])[0]
    scores = results_dict.get('scores', [[]])[0]

    print(f"🔍 Found {len(ids)} Retrieved Chunks\n" + "="*60)

    # zip() lets us loop through the IDs, Docs, and Scores all at the same time
    for rank, (chunk_id, doc, score) in enumerate(zip(ids, documents, scores), start=1):
        
        # Clean up the ugly markdown escape characters and excessive newlines
        clean_text = doc.replace('\r\n', '\n').replace('\\', '').strip()
        
        # Print a clean UI block for each chunk
        print(f"🏆 Rank:  {rank}")
        print(f"🔑 ID:    {chunk_id}")
        print(f"🎯 Score: {score:.5f} (Lower = More Relevant)")
        print("-" * 60)
        print(clean_text)
        print("=" * 60 + "\n")

try:
    query = "Benefits AI has given to the US Citizens"
    result = chroma_service.retrieve_by_query(query,15)
    print_clean_results(result)

except Exception as e:
    logging.error("An error occurred while generating personas.")
    print(CustomException(e, sys))