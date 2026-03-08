import redis
from rq import Queue

VALKEY_HOST = "localhost"
VALKEY_PORT = 6379

redis_conn = redis.Redis(
    host=VALKEY_HOST,
    port=VALKEY_PORT
)

document_queue = Queue(
    "document_queue",
    connection=redis_conn
)
#This creates a background job queue.

print(redis_conn.ping())