import sys
import os

import redis
from rq import Worker, Queue

# Ensure project root is in PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

VALKEY_HOST = "localhost"
VALKEY_PORT = 6379

listen = ["document_queue"]

redis_conn = redis.Redis(
    host=VALKEY_HOST,
    port=VALKEY_PORT
)

if __name__ == "__main__":

    print("Starting worker...")

    queues = [Queue(name, connection=redis_conn) for name in listen]

    worker = Worker(queues, connection=redis_conn)

    print("Worker listening on queue:", listen)

    worker.work()