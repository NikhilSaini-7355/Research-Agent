import asyncio
import uuid # 1. Added this import
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
import os
from Agents.embedding_agent import process_pending_embeddings

load_dotenv()

DATABASE_URL = os.getenv("NEON_DATABASE_URL")

async def test_entire_multi_agent_pipeline():
    print("🚀 Initializing Database Connection...")
    engine = create_async_engine(DATABASE_URL, echo=False)
    AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

    async with AsyncSessionLocal() as session:
        try:
            target_project_id = uuid.UUID('21111111-1111-1111-1111-111111111111')
            await process_pending_embeddings(db=session, project_id=target_project_id)
            
        except Exception as e:
            print(f"\n❌ Pipeline Test Failed: {e}")
            await session.rollback()

    await engine.dispose()
    print("🛑 Disconnected.")

if __name__ == "__main__":
    asyncio.run(test_entire_multi_agent_pipeline())