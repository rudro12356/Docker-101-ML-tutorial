# Docker-101-ML-tutorial
![image](https://github.com/user-attachments/assets/79fcba91-139f-401a-a033-9e670a0cb21e)

## Introduction

This tutorial covers the basics of Docker for Machine Learning (ML) applications and demonstrates how to use Docker to containerize and deploy a simple Flask-based application. Docker is a powerful tool that allows you to package and distribute applications along with their dependencies in a portable and consistent way. 

By the end of this tutorial, you’ll learn how to:

1. Understand Docker concepts (Images, Containers, Ports).
2. Dockerize a simple Flask ML application.
3. Run the Dockerized app locally.

## Table of Contents

- [What is Docker?](#what-is-docker)
- [Why Use Docker for ML Applications?](#why-use-docker-for-ml-applications)
- [Docker Basics](#docker-basics)
- [Dockerizing a Flask ML Application](#dockerizing-a-flask-ml-application)
- [How to Build and Run the Dockerized Application](#how-to-build-and-run-the-dockerized-application)
- [Conclusion](#conclusion)

## What is Docker?

Docker is an open-source platform used for automating the deployment of applications inside lightweight containers. Containers allow an application to be bundled with all its dependencies, ensuring that it can run on any system without compatibility issues.

### Key Concepts

- **Docker Images**: A Docker image is a snapshot of an application and its dependencies. It is the blueprint for creating Docker containers.
- **Docker Containers**: A container is an instance of an image that is executed in an isolated environment.
- **Ports**: Docker containers expose certain ports to make services (e.g., web apps) accessible to the outside world.
- **Dockerfile**: A text file containing instructions to build a Docker image.

## Why Use Docker for ML Applications?

- **Reproducibility**: Docker ensures that your application and its dependencies are packaged together, making it easy to replicate the environment across various platforms.
- **Environment Isolation**: Docker containers provide isolated environments, preventing dependency conflicts between different applications.
- **Portability**: Docker images can be shared and run on any system with Docker installed, ensuring that your model works the same way in different environments.
- **Simplified Deployment**: Docker makes it easy to deploy ML models to cloud environments, servers, or even other developers' machines.

## Docker Basics

Before diving into Dockerizing the Flask app, let’s understand some key Docker concepts:

1. **Images**: A Docker image is a snapshot of your application and its dependencies. It is built using the instructions in a Dockerfile. Images are read-only.
   
2. **Containers**: Containers are running instances of Docker images. They are created when you run an image and can be started, stopped, or deleted.

3. **Ports**: When running a containerized application, you can expose certain ports to make it accessible from outside the container. For example, a Flask app typically runs on port 5000 inside the container.

4. **Dockerfile**: A `Dockerfile` contains instructions to build a Docker image. It specifies the base image, copies files, installs dependencies, and defines how the application should be executed.

## Dockerizing a Flask ML Application

In this section, we’ll containerize a simple Flask application that serves an ML model.

### Steps

1. **Create the Flask Application**

   First, ensure you have the `app.py` file ready with the Flask API to serve the model.

   ```python
   from flask import Flask, request, jsonify
   import numpy as np
   import pickle

   app = Flask(__name__)

   # Load the pre-trained model
   with open('model.pkl', 'rb') as file:
       model = pickle.load(file)

   @app.route('/predict', methods=['POST'])
   def predict():
       data = request.get_json(force=True)
       prediction = model.predict([np.array(data['input'])])
       return jsonify({'prediction': prediction[0]})

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)

# DockerFile

## Use the official Python image from Docker Hub
FROM python:3.8-slim

## Set the working directory inside the container
WORKDIR /app

## Copy the current directory contents into the container
COPY . /app

## Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

## Expose the port the app runs on
EXPOSE 5000

## Define the command to run the app
CMD ["python", "app.py"]

## Create requirements.txt

```
Flask==2.1.0
scikit-learn==0.24.2
numpy==1.19.5
```

# Building and running the application

## In the directory where your Dockerfile and application files are located, run the following command to build the Docker image:
```
docker build -t flask-ml-app
```

## After the image is built, run the container with:

```
docker run -p 5000:5000 flask-ml-app
```

## Test the API using Postman
![image](https://github.com/user-attachments/assets/9487a5cc-b167-4986-8a2d-9f483c2ec41f)

# Resources
1. https://www.linkedin.com/learning-login/share?forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fdocker-for-data-scientists%3Ftrk%3Dshare_ent_url%26shareId%3DMQp3OFc3SVacLzKQPF4fJQ%253D%253D
2. https://www.datacamp.com/tutorial/docker-for-data-science-introduction
3. Chatgpt
