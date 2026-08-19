from typing import List
from pydantic import BaseModel, Field


class ChatResponse(BaseModel):
    answer: str = Field(description="The main answer to the user's question")
    category: str = Field(description="Category of the question: Programming, Mathematics, or General")
    confidence: float = Field(description="Confidence score of the answer, between 0 and 1")
    keywords: List[str] = Field(description="Key terms related to the answer")


class SummaryResponse(BaseModel):
    summary: str = Field(description="A short one or two sentence summary of the answer")
