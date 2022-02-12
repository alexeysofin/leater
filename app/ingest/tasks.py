from rq.decorators import job

import boto3

from app.core.db import get_db_ctx
from app.workers import INGEST_QUEUE
from app.ingest import service
from app.settings import S3_ACCESS_KEY, S3_ENDPOINT_URL, S3_REGION, S3_SECRET

S3_CLIENT = boto3.client(
    "s3",
    endpoint_url=S3_ENDPOINT_URL,
    region_name=S3_REGION,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET,
)


@job(INGEST_QUEUE)
def ingest_document(text: str):
    with get_db_ctx() as db:
        service.ingest_document(db, S3_CLIENT, text)
