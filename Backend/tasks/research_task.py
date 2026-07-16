from sqlalchemy.orm import Session

from Graph.research_pipeline import app
from backend.database.database import SessionLocal
from backend.services.progress_service import ProgressService
from backend.services.research_service import ResearchService


async def run_research_job(
    job_id: str,
    topic: str
):

    db: Session = SessionLocal()
    
    try:

        progress_service = ProgressService(db)
        research_service = ResearchService(db)

        job = research_service.get_job(job_id)
        if job is None:
            raise ValueError(f"Job {job_id} not found")

        inputs = {
            "job_id": job.job_id,
            "project_id": job.project_id,
            "topic": job.topic,
            "services": {
                "progress": progress_service
            }
        }

        final_state = await app.ainvoke(inputs)

        research_service.save_result(
            job_id=job_id,
            markdown=final_state["final_markdown"],
            pdf_path=""
        )

    except Exception as e:

        research_service.mark_failed(
            job_id,
            str(e)
        )

    finally:

        db.close()