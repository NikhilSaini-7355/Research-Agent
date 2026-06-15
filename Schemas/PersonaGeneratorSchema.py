from pydantic import BaseModel, Field
from typing import List


from pydantic import BaseModel, Field


class ExpertPersona(BaseModel):

    role: str = Field(
        description="Professional role of the expert"
    )

    expertise: str = Field(
        description="Primary area of expertise"
    )

    research_dimension: str = Field(
        description="""
        Assigned research dimension.

        Must be one of:
        - Fundamentals and Core Concepts
        - Technical and Mathematical Foundations
        - Implementation and Practical Deployment
        - Applications and Industrial Use Cases
        - Future Trends and Research Directions
        """
    )

    perspective: str = Field(
        description="Unique research perspective"
    )

class ExpertRolesSchema(BaseModel):
    experts: List[ExpertPersona] = Field(
        description="List of expert personas"
    )