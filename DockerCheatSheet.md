# 🐳 Docker Cheat Sheet

## 📦 Basic Commands

| Command | Description |
|---------|-------------|
| `docker --version` | Show Docker version |
| `docker info` | Show system-wide Docker info |
| `docker help` | Show help for Docker CLI |

---

## 🏗️ Images

| Command | Description |
|---------|-------------|
| `docker build -t <name> .` | Build image from Dockerfile |
| `docker pull <image>` | Download image from Docker Hub |
| `docker images` | List local images |
| `docker rmi <image>` | Remove image |
| `docker tag <img> <name>:<tag>` | Tag image with a new name |

---

## 🐋 Containers

| Command | Description |
|---------|-------------|
| `docker run <image>` | Run a container |
| `docker run -it <image> sh` | Run container interactively |
| `docker run -d <image>` | Run container in background (detached) |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker stop <container>` | Stop container |
| `docker start <container>` | Start stopped container |
| `docker restart <container>` | Restart container |
| `docker rm <container>` | Remove container |
| `docker exec -it <container> bash` | Run command inside container |
| `docker logs <container>` | View logs from a container |

---

## 📁 Volumes & File Mounts

| Command | Description |
|---------|-------------|
| `docker volume create <name>` | Create volume |
| `docker volume ls` | List volumes |
| `docker run -v <vol-name>:/path <image>` | Mount volume |
| `docker run -v $(pwd):/app <image>` | Bind mount current dir to container |

---

## 🌐 Networks

| Command | Description |
|---------|-------------|
| `docker network ls` | List networks |
| `docker network create <name>` | Create network |
| `docker network connect <net> <container>` | Connect container to network |

---

## 📄 Dockerfile Example

```Dockerfile
# Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "start"]

---

## 🧼 Docker Cleanup

| Command                  | Description                                                |
| ------------------------ | ---------------------------------------------------------- |
| `docker system prune`    | Remove unused data (images, containers, volumes, networks) |
| `docker image prune`     | Remove unused images                                       |
| `docker volume prune`    | Remove unused volumes                                      |
| `docker container prune` | Remove stopped containers                                  |
| `docker builder prune`   | Remove build cache                                         |

---

## 🛠️ Docker Compose

| Command                        | Description                              |
| ------------------------------ | ---------------------------------------- |
| `docker-compose up`            | Start services                           |
| `docker-compose up -d`         | Start in detached mode                   |
| `docker-compose down`          | Stop and remove services                 |
| `docker-compose logs`          | View logs                                |
| `docker-compose ps`            | List running services                    |
| `docker-compose exec <svc> sh` | Execute a shell in the service container |

