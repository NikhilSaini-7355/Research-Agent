from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict, Any
from uuid import UUID

# --- USER SCHEMAS ---
class UserCreate(BaseModel):
    email: EmailStr
    firstname: str
    lastname: str
    password: str

class UserUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    password: Optional[str] = None


# --- PROJECT SCHEMAS ---
class ProjectCreate(BaseModel):
    user_id: UUID
    topic: str
    status: Optional[str] = "pending"

class ProjectUpdate(BaseModel):
    status: Optional[str] = None
    
# --- PERSONA SCHEMAS ---
class PersonaCreate(BaseModel):
    project_id: UUID
    role: str
    expertise: str
    research_dimension: str
    perspective: str

class PersonaUpdate(BaseModel):
    pass # Personas are usually immutable once generated

# --- QUESTION SCHEMAS ---
class QuestionCreate(BaseModel):
    project_id: UUID
    queries: List[str]

class QuestionUpdate(BaseModel):
    status: Optional[str] = None

# --- EXTRACTED CONTENT SCHEMAS ---
class ExtractedContentCreate(BaseModel):
    project_id: UUID
    url: str
    title: Optional[str] = None
    raw_content: str

class ExtractedContentUpdate(BaseModel):
    embedding_status: Optional[str] = None

# --- GENERATED ARTICLE SCHEMAS ---
class ArticleCreate(BaseModel):
    project_id: UUID
    outline: Optional[Dict[str, Any]] = None

class ArticleUpdate(BaseModel):
    draft_content: Optional[str] = None
    final_content: Optional[str] = None
    citations: Optional[List[Dict[str, Any]]] = None
    confidence_score: Optional[float] = None