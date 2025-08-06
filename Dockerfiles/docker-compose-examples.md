# Docker-compose Examples.


### 1. Running simple conatiner:
`docker run ubuntu sleep 100`

```
version: '1.0'
services:
  ubuntu:
    container_name: ubuntu-server1
    image: ubuntu
    command: sleep 100
```

### 2. Running Conatiner with Port number.
`docker run --name web-server-1 -p 82:80 httpd`

```
version: '1.0'
services:
  web:
    container_name: web-server-1
    image: httpd
    ports:
    - "82:80"
```


### 3. Bind Mounting to the conatiners.
`docker run -it -v /tmp/test-data:/tmp ubuntu bash`

```
version: '1.0'
services:
  web:
    container_name: ubuntu-1
    image: ubuntu
    volumes:
      - /tmp/test-data:/tmp
    command: "sleep 1000"
```


### 4. Volume Mounting to the container.
`docker volume create akshay` <br>
`docker run -v akshay:/tmp ubuntu sleep 1000`

```
---
version: v1
services:
  storage:
    image: ubuntu
    container_name: volume-test
    volumes:
      - akshay:/tmp
    command: sleep 2000
volumes: 
  akshay:

```

### 2. Environment Varibale.
`docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=root -d mysql`

```
---
version: v1
services:
  db:
    image: mysql
    container_name: mydatabase
    environment:
      - MYSQL_ROOT_PASSWORD=root
```
