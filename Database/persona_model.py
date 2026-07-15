import uuid
from datetime import datetime
from sqlalchemy import TEXT, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Ensure you import your DeclarativeBase from your setup file
from backend.database.models import Base 

class ResearchPersonaModel(Base):
    __tablename__ = "research_personas"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4, 
        server_default=text("gen_random_uuid()")
    )
    
    # index=True natively handles your CREATE INDEX statement.
    # ondelete="CASCADE" handles your CONSTRAINT fk_research_project.
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("research_projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    role: Mapped[str] = mapped_column(TEXT, nullable=False)
    expertise: Mapped[str] = mapped_column(TEXT, nullable=False)
    research_dimension: Mapped[str] = mapped_column(TEXT, nullable=False)
    perspective: Mapped[str] = mapped_column(TEXT, nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=text("CURRENT_TIMESTAMP")
    )

    # ==========================================
    # RELATIONSHIPS 
    # ==========================================
    
    # 1. Looks UP to the Project table
    # This matches the 'personas' relationship we defined in ProjectModel
    project = relationship("ProjectModel", back_populates="personas")