import uuid
from datetime import datetime
from sqlalchemy import String, TEXT, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Ensure you import your DeclarativeBase from your setup file
from backend.database.models import Base 

class ProjectModel(Base):
    __tablename__ = "research_projects"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4, 
        server_default=text("gen_random_uuid()")
    )
    
    # Notice index=True: This perfectly replaces your standalone CREATE INDEX statement.
    # The ondelete="CASCADE" perfectly matches your CONSTRAINT fk_user.
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True 
    )
    
    topic: Mapped[str] = mapped_column(TEXT, nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=text("CURRENT_TIMESTAMP")
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP")
    )

    # ==========================================
    # RELATIONSHIPS 
    # ==========================================
    
    # 1. Looks UP to the User table
    user = relationship("UserModel", back_populates="projects")

    # 2. Looks DOWN to the child tables (Personas, Extracted Content, Final Article)
    # These cascade deletes ensure that if a project is deleted, all its AI-generated data is wiped too.
    personas = relationship(
        "ResearchPersonaModel", 
        back_populates="project", 
        cascade="all, delete-orphan"
    )
    
    extracted_content = relationship(
        "ExtractedContentModel", 
        back_populates="project", 
        cascade="all, delete-orphan"
    )
    
    article = relationship(
        "GeneratedArticleModel", 
        back_populates="project", 
        uselist=False, # uselist=False enforces the strict 1:1 relationship for the final article
        cascade="all, delete-orphan"
    )