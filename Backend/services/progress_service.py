from sqlalchemy.orm import Session

from backend.models.research_job import ResearchJob


class ProgressService:
    def __init__(self,db):
        self.db = db

    def update_progress(
        self,
        job_id: str,
        progress: int,
        status: str
    ):

        job = (
            self.db.query(ResearchJob)
            .filter(ResearchJob.job_id == job_id)
            .first()
        )

        if job is None:
            return

        job.progress = progress
        job.status = status

        self.db.commit()