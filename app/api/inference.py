# Packages
import logging
from fastapi import APIRouter, Header

from app.lib.inference_utils import calculate_ngrams
# Local Modules
from app.models.pydantic import NGRAMPayload, NGRAMResponse

router = APIRouter()
log = logging.getLogger("uvicorn")


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
