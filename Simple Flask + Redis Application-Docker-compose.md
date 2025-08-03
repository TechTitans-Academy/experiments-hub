# 🚀 Application Overview: Flask + Redis Counter

This is a minimal web application designed to demonstrate container communication in Docker Compose. It's perfect for learning purposes because:

- It's simple but interactive.
- It showcases service-to-service communication.
- It uses a lightweight cache-based counter (Redis) instead of a database.


### 🔹 How it Works

Flask Web App (web container):

- Serves a simple HTTP route (/).
- On each visit, it connects to Redis and increments a counter.
- Returns the number of visits in the response.
- Redis (redis container):
- Acts as an in-memory key-value store.
- Stores a single key hits that tracks how many times the page was visited.


#### Project structure.

```
.
├── app
│   ├── app.py
│   └── requirements.txt
├── docker-compose.yml
└── Dockerfile
2 directories, 4 files
```

#### app.py:

```
from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f'Hello! This page has been viewed {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

#### requirements.txt
```
flask
redis
```

#### docker-compose.yml
```
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5005:5000"
    depends_on:
      - redis

  redis:
    image: "redis:alpine"
```

#### Dockerfile:
```
FROM python:3.10-slim
WORKDIR /app
COPY app /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

