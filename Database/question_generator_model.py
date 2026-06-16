import uuid
from datetime import datetime
from typing import List
from sqlalchemy import String, TEXT, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Ensure you import your DeclarativeBase from your setup file
from backend.database.models import Base 

class ResearchQuestionModel(Base):
    __tablename__ = "research_questions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4, 
        server_default=text("gen_random_uuid()")
    )
    
    # index=True natively handles your CREATE INDEX statement.
    # ondelete="CASCADE" handles your CONSTRAINT fk_research_question.
    persona_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("research_personas.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    question_text: Mapped[str] = mapped_column(TEXT, nullable=False)
    
    # Mapping the Postgres TEXT[] array to a Python List of Strings
    queries: Mapped[List[str]] = mapped_column(ARRAY(TEXT), nullable=False)
    
    status: Mapped[str] = mapped_column(
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
    
    # Looks UP to the Persona table
    # This matches the 'questions' relationship defined in ResearchPersonaModel
    persona = relationship("ResearchPersonaModel", back_populates="questions")