# Packages
import sklearn # Throws an error if this isn't imported first
import json
import logging
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from spacy import load

# Local Modules
from app.api import inference

log = logging.getLogger("uvicorn")

with open("app/description.md", "r") as f:
    description = f.read()

with open("app/meta.json") as f:
    meta_data = json.load(f)
tags_metadata = meta_data["tags"]

if os.getenv("ENVIRONMENT") == "dev":
    prefix = ""
else:
    prefix = "/prod"


def create_application() -> FastAPI:
    application = FastAPI(
        title="NLP Annotation API",
        description=description,
        openapi_tags=tags_metadata,
        root_path=prefix
    )
    application.include_router(inference.router, prefix="/api/v1.0/inference")
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application


app = create_application()
handler = Mangum(app,api_gateway_base_path=prefix)
