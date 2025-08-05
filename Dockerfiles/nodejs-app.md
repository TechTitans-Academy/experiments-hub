# Simple Node.js App

This is a simple Node.js application using Express.js, packaged with Docker.

## 🚀 Features

- Lightweight Express server
- Dockerized for easy deployment
- Minimal setup and easy to understand

## 🧾 Prerequisites

- [Node.js](https://nodejs.org/) (if running locally without Docker)
- [Docker](https://www.docker.com/) (for containerized usage)

## 📁 Project Structure

```
.
├── app.js
├── Dockerfile
└── package.json
```

`app.js`

```
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello from Node.js!');
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
```

`package.json`
```
{
  "name": "simple-node-app",
  "version": "1.0.0",
  "description": "A simple Node.js app",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

`Dockerfile`

```
# Use the official Node.js 18 image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Expose the app port
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]

```
Then open http://localhost:3000 in your browser — you should see Hello from Node.js!.
