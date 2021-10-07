from typing import List, Optional

from pydantic import BaseModel, Field

sample_text = ["Joe Biden is the president of the United States"]


# NGRAMS
class NGRAM(BaseModel):
    ngram: str
    count: int


class NGRAMResponse(BaseModel):
    success: bool
    message: str
    totalNGRAMS: int = Field(...,example=4)
    data: List[NGRAM] = Field(...,example=[
        {
            "ngram": "biden president",
            "count": 1
        },
        {
            "ngram": "joe biden",
            "count": 1
        },
        {
            "ngram": "president united",
            "count": 1
        },
        {
            "ngram": "united state",
            "count": 1
        }
    ])


class NGRAMPayload(BaseModel):
    responses: List[str] = Field(
        ..., example=sample_text
    )
    minWords: Optional[int] = Field(2)
    maxWords: Optional[int] = Field(2)


# Part of Speech
class POS(BaseModel):
    tokens: List[str]
    pos: List[str]


class POSResponse(BaseModel):
    success: bool
    message: str
    data: List[POS] = Field(...,example=[{
        "tokens": [
            "Joe","Biden","is","the","president",
            "of","the","United","States"
        ],
        "pos": [
            "PROPN","PROPN","AUX","DET","NOUN",
            "ADP","DET","PROPN","PROPN"
        ]
    }])


# Named Entity Recognition
class Entity(BaseModel):
    text: str
    entType: str
    start: int
    end: int


class NERResponse(BaseModel):
    success: bool
    message: str
    data: List[List[Entity]] = Field(...,example=[
        [
            {
                "text": "Joe Biden",
                "entType": "PERSON",
                "start": 0,
                "end": 9
            },
            {
                "text": "the United States",
                "entType": "GPE",
                "start": 30,
                "end": 47
            }
        ]
    ])


class TextPayload(BaseModel):
    responses: List[str] = Field(...,example=sample_text)