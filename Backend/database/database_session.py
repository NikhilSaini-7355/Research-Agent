from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import os
import ssl
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("NEON_DATABASE_URL")

# 1. GLOBAL ENGINE
print("🚀 Initializing Database Connection...")

# Create a default SSL context (Required for NeonDB with asyncpg)
ssl_context = ssl.create_default_context()

engine = create_async_engine(
    DATABASE_URL, 
    echo=False,
    connect_args={
        "ssl": ssl_context,
        "timeout": 60 # Gives Neon time to wake up from scale-to-zero
    }
)

# 2. GLOBAL SESSION FACTORY
AsyncSessionLocal = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession,
    expire_on_commit=False # Crucial for async so objects don't expire after commit
)

# 3. DEPENDENCY GENERATOR
async def get_db():
    """
    Yields a database session for a single request, 
    then reliably closes it when the request is done.
    """
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()