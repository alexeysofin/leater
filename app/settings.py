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
