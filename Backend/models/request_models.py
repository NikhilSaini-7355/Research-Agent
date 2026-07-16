from pydantic import BaseModel, Field,EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class ResearchRequest(BaseModel):
    topic: str = Field(
        ...,
        description="Research topic provided by the user"
    )
class SignupRequest(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    