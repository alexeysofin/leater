import uuid
from urllib.parse import urlparse

from boto3_type_annotations import s3

from sqlalchemy.orm import Session

from app.document.service import create_document
from app.document.schemas import DocumentCreate
from app.settings import S3_BUCKET

import trafilatura


def scrape(url: str) -> str:
    downloaded = trafilatura.fetch_url(url)
    return trafilatura.extract(downloaded)


def ingest_document(db: Session, s3_client: s3.Client, text: str):
    p = urlparse(text)

    if p.scheme and p.netloc:
        # TODO: move to scrape queue
        doc_text = scrape(text)
        url = text
    else:
        doc_text = text
        url = ""

    fname = f"{uuid.uuid4()}.txt"
    s3_client.put_object(
        Body=doc_text, Bucket=S3_BUCKET, Key=fname, ContentType="text/plain"
    )

    create_document(
        db, DocumentCreate(text_filename=fname, url=url, summary=doc_text[:100])
    )
