from rq.decorators import job

from app.workers import INGEST_QUEUE
from app.ingest import service


@job(INGEST_QUEUE)
def ingest_document(text: str):
    service.ingest_document(text)
