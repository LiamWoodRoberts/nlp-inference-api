from typing import List, Optional

from pydantic import BaseModel, Field


# NGRAMS
class NGRAM(BaseModel):
    ngram: str
    count: int


class NGRAMResponse(BaseModel):
    success: bool
    message: str
    totalNGRAMS: int
    data: List[NGRAM]


class NGRAMPayload(BaseModel):
    responses: List[str] = Field(
        ..., example=["Joe Biden is the president of the United States"]
    )
    minWords: Optional[int] = Field(2)
    maxWords: Optional[int] = Field(2)
