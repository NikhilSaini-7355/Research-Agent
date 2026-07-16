from sqlalchemy import Column, String, Integer, DateTime, Text
from datetime import datetime

from backend.database.database import Base

class ResearchJob(Base):

    __tablename__ = "research_jobs"

    job_id = Column(
        String,
        primary_key=True,
        index=True
    )

    topic = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )

    progress = Column(
        Integer,
        default=0
    )

    markdown = Column(
        Text,
        nullable=True
    )

    pdf_path = Column(
        String,
        nullable=True
    )

    error = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    completed_at = Column(
        DateTime,
        nullable=True
    )