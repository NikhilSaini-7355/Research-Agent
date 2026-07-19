from backend.database.database import Base, engine

# Import ALL models before create_all()
from backend.models.research_job import ResearchJob

Base.metadata.create_all(bind=engine)

print("Database initialized successfully.")