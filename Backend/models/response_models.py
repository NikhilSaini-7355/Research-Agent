from pydantic import BaseModel


class ResearchResponse(BaseModel):
    job_id: str
    status: str
    project_id: str


class JobStatusResponse(BaseModel):
    job_id: str
    status: str
    progress: int
    
class ResearchStatusResponse(BaseModel):
    job_id: str
    status: str
    progress: int

class ResearchResultResponse(BaseModel):
    job_id: str
    status: str
    markdown: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
class SignupResponse(BaseModel):
    message: str