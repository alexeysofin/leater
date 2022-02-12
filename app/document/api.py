from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.core.db import get_db

from app.document.schemas import DocumentRead
from app.document import service

document_router = APIRouter()


@document_router.get("", response_model=List[DocumentRead])
def list_documents(db: Session = Depends(get_db)):
    return service.list_documents(db)