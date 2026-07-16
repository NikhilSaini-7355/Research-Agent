from backend.database.database import SessionLocal
from backend.services.research_service import ResearchService

db = SessionLocal()

service = ResearchService(db)

job = service.create_job("Artificial Intelligence")

service.mark_failed(
    job.job_id,
    "Tavily API request timed out."
)

updated_job = service.get_job_status(job.job_id)
job = service.get_result(job.job_id)

print(job.markdown)
print(job.pdf_path)


db.close()