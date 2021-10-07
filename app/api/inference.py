# Packages
import logging
from fastapi import APIRouter, Header
from spacy import load

# Local Modules
from app.lib.inference_utils import (
    calculate_ngrams, tag_pos_spacy, ner
)

from app.models.pydantic import (
    NGRAMPayload, NGRAMResponse,
    TextPayload, POSResponse,
    NERResponse
)

router = APIRouter()
log = logging.getLogger("uvicorn")
nlp = load("en_core_web_sm")

@router.post("/ngrams", response_model=NGRAMResponse, status_code=200)
def ngram_inference(payload: NGRAMPayload, x_api_key: str = Header(None)):
    payload_dict = payload.dict()
    responses = payload_dict["responses"]
    min_words = payload_dict.get("min_words", 2)
    max_words = payload_dict.get("max_words", 2)
    ngrams = calculate_ngrams(responses, min_words, max_words)
    response = NGRAMResponse(
        success=True,
        message="NGRAMs calculated successfully",
        totalNGRAMS=len(ngrams),
        data=ngrams,
    )
    return response


@router.post("/pos", response_model=POSResponse, status_code=200)
def pos_inference(payload: TextPayload, x_api_key: str = Header(None)):
    responses = payload.dict()["responses"]
    pos_results = []
    for doc in nlp.pipe(responses):
        tokens, pos_tags = tag_pos_spacy(doc)
        pos_results.append({
            "tokens": tokens, "pos": pos_tags
        })
    response = POSResponse(
        success=True,
        message="Part of speech tagged successfully",
        data = pos_results
    )
    return response


@router.post("/ner", response_model=NERResponse, status_code=200)
def ner_inference(payload: TextPayload, x_api_key: str = Header(None)):
    responses = payload.dict()["responses"]
    data = [ner(doc) for doc in nlp.pipe(responses)]
    response = NERResponse(
        success=True,
        message="Part of speech tagged successfully",
        data = data
    )
    return response
