from starlette.config import Config

config = Config(".env")

DB_URL = config("DB_URL", cast=str, default="postgresql://app:app@db/app")

TELEGRAM_BOT_KEY = config(
    "TELEGRAM_BOT_KEY",
    cast=str,
    default="",
)

INGEST_QUEUE = config("INGEST_QUEUE", cast=str, default="ingest")

REDIS_URL = config("REDIS_URL", cast=str, default="redis://redis:6379")

S3_ACCESS_KEY = config("S3_ACCESS_KEY", cast=str, default="minio")
S3_SECRET = config("S3_SECRET", cast=str, default="minio123")
S3_ENDPOINT_URL = config("S3_ENDPOINT_URL", cast=str, default="http://minio:9000")
S3_REGION = config("S3_REGION", cast=str, default="us-east-2")
S3_BUCKET = config("S3_BUCKET", cast=str, default="leater")