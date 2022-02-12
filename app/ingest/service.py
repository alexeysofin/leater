from urllib.parse import urlparse
from app.core.db import get_db_ctx

from app.document.service import create_document
from app.document.schemas import DocumentCreate

import trafilatura


def scrape(url: str) -> str:
    downloaded = trafilatura.fetch_url(url)
    return trafilatura.extract(downloaded)


def ingest_document(text: str):
    p = urlparse(text)

    if p.scheme and p.netloc:
        # TODO: move to scrape queue
        doc_text = scrape(text)
        url = text    
    else:
        doc_text = text
        url = ""

    with get_db_ctx() as db:
        create_document(db, DocumentCreate(text=doc_text, url=url))
