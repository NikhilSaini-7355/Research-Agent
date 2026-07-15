from backend.database.crud_agents import crud_content
from backend.core.chunking import text_processor
from backend.database.chroma_service import chroma_service
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

async def process_pending_embeddings(db: AsyncSession, project_id: UUID):
    """
    1. Fetches pending text from Postgres.
    2. Chunks it.
    3. Embeds and stores it in ChromaDB.
    4. Marks it as 'completed' in Postgres.
    """
    
    # 1. Use the CRUD helper we built earlier to find pending text
    pending_items = await crud_content.get_pending_embeddings(db=db, project_id=project_id)
    
    if not pending_items:
        print("No pending embeddings found.")
        return

    for item in pending_items:
        try:
            print(f"Processing content: {item.url}...")
            
            # 2. Chunk the raw text
            chunks = text_processor.chunk_text(item.raw_content)
            
            # 3. Store in Vector DB (Automatically calculates 1536-dim embeddings)
            await chroma_service.ingest_chunks(
                project_id=item.project_id,
                content_id=item.id,
                chunks=chunks
            )
            
            # 4. Update Postgres status using our CRUD layer
            item.embedding_status = "completed"
            db.add(item)
            await db.commit()
            
        except Exception as e:
            print(f"❌ Failed to embed content {item.id}: {e}")
            item.embedding_status = "pending"
            db.add(item)
            await db.commit()

    print("🎉 Embedding  complete!")