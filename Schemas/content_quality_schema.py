from pydantic import BaseModel, Field

class ContentQualitySchema(BaseModel):

    quality: str

    knowledge_density: str

    noise_level: str

    rag_readiness: str

    reason: str