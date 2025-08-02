# Docker File Samples.

Here’s a list of Dockerfile samples for different use cases. Each snippet demonstrates a common scenario to help you understand Dockerfile syntax and best practices.


### 🧱 1. Simple Python App: 

<b>Use Case:</b> Run a Python script.

```
# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Run the application
CMD ["python", "app.py"]
```
---

### 🌐 2. Node.js Web Server
<b>Use Case:</b> Run a Node.js web app.

```
FROM node:20

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000
CMD ["node", "server.js"]
```
---

### 🧪 9. Alpine-based Bash Script Runner
<b>Use Case:</b> Lightweight image to run shell scripts.

```
FROM alpine:3.19

RUN apk add --no-cache bash

COPY ./script.sh /app/script.sh
RUN chmod +x /app/script.sh

CMD ["/app/script.sh"]
```
