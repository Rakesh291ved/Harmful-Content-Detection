import redis
import json

queue = redis.Redis()

# Add request to queue
request_data = {"text": "You are ugly!"}
queue.lpush("requests", json.dumps(request_data))

# Fetch request
data = json.loads(queue.rpop("requests"))
print("Processing:", data)
