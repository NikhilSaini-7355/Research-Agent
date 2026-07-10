import asyncio
import uuid 
import os
from backend.database.database_session import AsyncSessionLocal
from Agents.embedding_agent import process_pending_embeddings

async def test_entire_multi_agent_pipeline():
    async with AsyncSessionLocal() as session:
        try:
            target_project_id = uuid.UUID('21111111-1111-1111-1111-111111111111')
            await process_pending_embeddings(db=session, project_id=target_project_id)
            
        except Exception as e:
            print(f"\n❌ Pipeline Test Failed: {e}")
            await session.rollback()

if __name__ == "__main__":
    asyncio.run(test_entire_multi_agent_pipeline())