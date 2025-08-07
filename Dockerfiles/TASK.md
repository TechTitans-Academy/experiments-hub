### Hosting website with Customized containers with docker-compose

#### <b>`index.html` code:</b>

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Docker Greeting</title>
  <style>
    body {
      margin: 0;
      background-color: #282c34; /* Dark background */
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      color: #ffffff;
      font-family: Arial, sans-serif;
      font-size: 2rem;
    }
  </style>
</head>
<body>
  Hi, from Docker container! 😊👋
</body>
</html>
```

#### <b>`Dockerfile` code:</b>

```
# Using base image ubuntu.
FROM ubuntu

# Installting the packages.
RUN apt update && apt install apache2 -y

# COPY index.html /var/www/html/index.html
COPY index.html /var/www/html/

# Expose port 80
EXPOSE 80

# Starting service.
RUN service apache2 start

# Start Apache in the foreground.
CMD ["apachectl", "-D", "FOREGROUND"]
```
