from typing import List

from datetime import datetime
from sqlalchemy.orm import Session

from app.document.models import Document
from app.document.schemas import DocumentCreate


def create_document(db: Session, dc: DocumentCreate) -> Document:
    db_doc = Document(
        text_filename=dc.text_filename,
        url=dc.url,
        summary=dc.summary,
        updated_at=datetime.utcnow(),
    )
    db.add(db_doc)
    db.commit()
    return db_doc

def list_documents(db: Session) -> List[Document]:
    return db.query(Document).all()
