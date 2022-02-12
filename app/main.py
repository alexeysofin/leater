from fastapi import FastAPI

app = FastAPI()

from app.document.api import document_router

app.include_router(document_router, prefix="/documents")
