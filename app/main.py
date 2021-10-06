import logging
import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from app.api import inference

log = logging.getLogger("uvicorn")

with open("app/description.md","r") as f:
    description = f.read()

with open("app/meta.json") as f:
    meta_data = json.load(f)
tags_metadata = meta_data["tags"]


def create_application() -> FastAPI:
    application = FastAPI(
        title="NLP Annotation API",
        descrition=description,
        openapi_tags=tags_metadata,
    )
    application.include_router(inference.router, prefix="/api/v1.0/inference")
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    return application


app = create_application()
handler = Mangum(app)