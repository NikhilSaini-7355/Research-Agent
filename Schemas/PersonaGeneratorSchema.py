from pydantic import BaseModel, Field

# 1. Define the structure for a single expert
class ExpertPersona(BaseModel):
    role: str = Field(description="The professional role of the expert")
    perspective: str = Field(description="A VERY short perspective max 1 or 2 sentences.")

# 2. Hardcode the 5 slots so Groq knows EXACTLY what keys to expect
class ExpertRolesSchema(BaseModel):
    expert_1: ExpertPersona = Field(description="The first expert persona")
    expert_2: ExpertPersona = Field(description="The second expert persona")
    expert_3: ExpertPersona = Field(description="The third expert persona")
    expert_4: ExpertPersona = Field(description="The fourth expert persona")
    expert_5: ExpertPersona = Field(description="The fifth expert persona")