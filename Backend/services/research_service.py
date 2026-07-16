from uuid import uuid4
from datetime import datetime
from sqlalchemy.orm import Session

from backend.models.research_job import ResearchJob


class ResearchService:

    def __init__(self, db: Session):
        self.db = db

    def _get_job(
        self,
        job_id: str
    ) -> ResearchJob | None:

        return (
            self.db.query(ResearchJob)
            .filter(ResearchJob.job_id == job_id)
            .first()
        )

    def create_job(self, topic: str) -> ResearchJob:

        job = ResearchJob(
            job_id=str(uuid4()),
            topic=topic,
            status="queued",
            progress=0
        )

        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)

        return job

    def get_job_status(self, job_id: str) -> ResearchJob | None:

        return self._get_job(job_id)

    def get_result(self, job_id: str) -> ResearchJob | None:

        return self._get_job(job_id)

    def save_result(
        self,
        job_id: str,
        markdown: str,
        pdf_path: str
    ) -> ResearchJob | None:

        job = self._get_job(job_id)

        if job is None:
            return None

        job.markdown = markdown
        job.pdf_path = pdf_path
        job.status = "completed"
        job.progress = 100
        job.completed_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(job)

        return job

    def mark_failed(
        self,
        job_id: str,
        error: str
    ) -> ResearchJob | None:

        job = self._get_job(job_id)

        if job is None:
            return None

        job.status = "failed"
        job.error = error
        job.completed_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(job)

        return job
