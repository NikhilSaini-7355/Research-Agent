import uuid
from datetime import datetime
from typing import Optional
from sqlalchemy import String, TEXT, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Ensure you import your DeclarativeBase from your setup file
from backend.database.models import Base 

class ExtractedContentModel(Base):
    __tablename__ = "extracted_content"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4, 
        server_default=text("gen_random_uuid()")
    )
    
    # index=True handles your CREATE INDEX statement.
    # ondelete="CASCADE" handles your CONSTRAINT fk_extracted_content.
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("research_projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    url: Mapped[str] = mapped_column(TEXT, nullable=False)
    
    # Title is nullable because web scraping doesn't always yield a clean title tag
    title: Mapped[Optional[str]] = mapped_column(TEXT, nullable=True)
    
    raw_content: Mapped[str] = mapped_column(TEXT, nullable=False)
    
    embedding_status: Mapped[str] = mapped_column(
        String(30), 
        nullable=False,
        default="pending",
        server_default=text("'pending'")
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=text("CURRENT_TIMESTAMP")
    )

    # ==========================================
    # RELATIONSHIPS 
    # ==========================================
    
    # Looks UP to the Project table
    # This matches the 'extracted_content' relationship defined in ProjectModel
    project = relationship("ProjectModel", back_populates="extracted_content")