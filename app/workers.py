from redis import Redis
from rq import Queue

from app.settings import REDIS_URL

INGEST_QUEUE = Queue("ingest", connection=Redis.from_url(REDIS_URL))
