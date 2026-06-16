import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional
from sqlalchemy import TEXT, Numeric, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Ensure you import your DeclarativeBase from your setup file
from backend.database.models import Base 

class GeneratedArticleModel(Base):
    __tablename__ = "generated_articles"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4, 
        server_default=text("gen_random_uuid()")
    )
    
    # unique=True enforces the strict 1:1 relationship (one article per project).
    # index=True explicitly satisfies your CREATE INDEX statement.
    # ondelete="CASCADE" handles your CONSTRAINT fk_generated_article.
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("research_projects.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True
    )
    
    # JSONB columns map directly to Python dicts and lists.
    # We use Optional[] because these fields are generated later in the pipeline.
    outline: Mapped[Optional[Dict[str, Any]]] = mapped_column(JSONB, nullable=True)
    
    draft_content: Mapped[Optional[str]] = mapped_column(TEXT, nullable=True)
    final_content: Mapped[Optional[str]] = mapped_column(TEXT, nullable=True)
    
    # Citations typically take the form of a list of dictionary objects
    citations: Mapped[Optional[List[Dict[str, Any]]]] = mapped_column(JSONB, nullable=True)
    
    # Numeric is used for the confidence score (e.g., 85.5, 99.9)
    confidence_score: Mapped[Optional[float]] = mapped_column(Numeric, nullable=True)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=text("CURRENT_TIMESTAMP")
    )

    # ==========================================
    # RELATIONSHIPS 
    # ==========================================
    
    # Looks UP to the Project table
    # This perfectly matches the 'article' relationship defined in ProjectModel, 
    # where we used uselist=False to ensure Python knows it's a 1:1 mapping.
    project = relationship("ProjectModel", back_populates="article")