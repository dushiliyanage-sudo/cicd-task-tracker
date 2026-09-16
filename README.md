# DevOps Task Tracker

A Flask-based web application developed for a DevOps and CI/CD practical assessment. The project demonstrates automated testing, Git version control, Docker containerization, Docker Compose, Docker Hub, and GitHub Actions CI/CD.

---

## Project Overview

The DevOps Task Tracker is a simple web application for managing development and DevOps-related tasks.

Users can:

- View tasks
- Add new tasks
- Mark tasks as completed
- Uncomplete tasks
- Delete tasks
- Check the application health status

The application is developed using Python and Flask and can be deployed locally using Docker and Docker Compose.

---

## Features

- Task management
- Add new tasks
- Complete and uncomplete tasks
- Delete tasks
- Health check endpoint
- Automated testing using pytest
- Docker containerization
- Docker Compose deployment
- Docker Hub image publishing
- GitHub Actions CI/CD
- Gunicorn production server
- Bootstrap-based user interface

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.13 | Programming language |
| Flask 3.1.3 | Web application framework |
| pytest 9.1.1 | Automated testing |
| Gunicorn 26.2.0 | Production WSGI server |
| Docker | Application containerization |
| Docker Compose | Local container deployment |
| Docker Hub | Docker image registry |
| Git | Version control |
| GitHub | Source code repository |
| GitHub Actions | CI/CD automation |
| Bootstrap | User interface styling |
| HTML | Web page structure |

---

## Project Structure

```text
cicd-task-tracker/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── tests/
│   └── test_app.py
│
├── templates/
│   └── index.html
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── app.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Application

The application provides a simple task management interface.

Users can:

1. View existing tasks
2. Add new tasks
3. Mark tasks as completed
4. Delete tasks
5. Check the application health status

The application runs on port `5000`.

---

## Automated Testing

The project uses **pytest** for automated testing.

The test suite verifies:

- The home page loads successfully
- The health endpoint returns a successful response
- A new task can be added successfully

### Run Tests

```powershell
pytest
```

Expected result:

```text
3 passed
```

The automated test suite successfully passed all three tests.

---

## Docker

The application is containerized using Docker.

### Dockerfile

The Dockerfile:

- Uses Python 3.13 slim as the base image
- Sets `/app` as the working directory
- Installs dependencies from `requirements.txt`
- Copies the application files into the container
- Exposes port `5000`
- Runs the application using Gunicorn

### Build Docker Image

```powershell
docker build -t cicd-task-tracker .
```

### Run Docker Container

```powershell
docker run -d -p 5000:5000 --name cicd-task-tracker-container cicd-task-tracker
```

The application can then be accessed at:

```text
http://localhost:5000
```

---

## Docker Compose

Docker Compose is used to simplify local deployment.

### Start the Application

```powershell
docker compose up -d --build
```

### Check Container Status

```powershell
docker compose ps
```

The container should show a status of `Up` with port `5000` mapped to the host.

Example:

```text
NAME                        STATUS              PORTS
cicd-task-tracker-compose   Up                  0.0.0.0:5000->5000/tcp
```

### Stop the Application

```powershell
docker compose down
```

---

## Local Deployment

The application was successfully deployed locally using Docker Compose.

The deployed application is available at:

```text
http://localhost:5000
```

The deployment was verified using:

```powershell
docker compose ps
```

The Docker container was successfully started and the application was accessible through port `5000`.

---

## Health Check

The application includes a health check endpoint.

Open:

```text
http://localhost:5000/health
```

Expected response:

```json
{
  "application": "DevOps Task Tracker",
  "status": "healthy"
}
```

The health endpoint confirms that the application is running correctly.

---

## Docker Hub

The Docker image is published to Docker Hub.

### Docker Hub Repository

```text
dushiliyanage/cicd-task-tracker
```

### Docker Image

```text
dushiliyanage/cicd-task-tracker:latest
```

The `latest` Docker image was successfully pushed to Docker Hub.

The Docker Hub repository contains the published container image used by the CI/CD pipeline.

---

## CI/CD Pipeline

GitHub Actions is used to automate the CI/CD process.

The workflow file is located at:

```text
.github/workflows/ci-cd.yml
```

The pipeline is triggered when code is pushed to the `main` branch or when a pull request targets the `main` branch.

### CI/CD Process

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Checkout Code
    │
    ├── Set Up Python
    │
    ├── Install Dependencies
    │
    ├── Run Automated Tests
    │
    ├── Log in to Docker Hub
    │
    ├── Build Docker Image
    │
    └── Push Docker Image to Docker Hub
```

---

## GitHub Actions Jobs

The workflow contains two main jobs.

### 1. Run Tests

The `Run Tests` job:

- Checks out the source code
- Sets up Python 3.13
- Installs project dependencies
- Runs the pytest test suite

The automated tests completed successfully.

### 2. Build and Push Docker Image

The `Build and Push Docker Image` job runs after the test job succeeds.

It:

- Logs in to Docker Hub
- Builds the Docker image
- Pushes the image to Docker Hub
- Uses the `latest` image tag

The Docker image was successfully built and pushed to Docker Hub.

---

## GitHub Actions Secrets

Docker Hub authentication is handled securely using GitHub Actions Secrets.

The workflow uses:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```

Sensitive Docker Hub credentials are not stored directly in the workflow file.

---

## CI/CD Verification

The GitHub Actions pipeline successfully completed both jobs:

```text
Run Tests
Build and Push Docker Image
```

Both jobs completed successfully with green status.

The Docker image was also successfully published to:

```text
dushiliyanage/cicd-task-tracker:latest
```

---

## Git Version Control

Git is used to track source code changes and manage the project repository.

### GitHub Repository

```text
https://github.com/dushiliyanage-sudo/cicd-task-tracker
```

### Main Branch

```text
main
```

### Important Commits

```text
Create Flask task tracker with automated tests
Add Docker containerization and Docker Compose
Add GitHub Actions CI/CD pipeline
```

The local repository is synchronized with the GitHub `main` branch.

---

## Deployment Verification

The application was verified after deployment using the following checks.

### Application

```text
http://localhost:5000
```

### Health Check

```text
http://localhost:5000/health
```

### Docker Compose Status

```powershell
docker compose ps
```

The Docker Compose container was successfully running with port `5000` exposed.

---

## Screenshots and Evidence

The following screenshots can be included as evidence of the completed implementation:

### 1. Application Screenshot

Screenshot showing the DevOps Task Tracker running in the browser.

### 2. Automated Testing Screenshot

Screenshot showing the pytest result:

```text
3 passed
```

### 3. Docker Compose Screenshot

Screenshot showing:

```powershell
docker compose ps
```

with the container status showing `Up`.

### 4. Local Deployment Screenshot

Screenshot showing the application running at:

```text
http://localhost:5000
```

### 5. Health Check Screenshot

Screenshot showing:

```text
http://localhost:5000/health
```

with:

```json
{
  "application": "DevOps Task Tracker",
  "status": "healthy"
}
```

### 6. Docker Hub Screenshot

Screenshot showing:

```text
dushiliyanage/cicd-task-tracker:latest
```

on Docker Hub.

### 7. GitHub Actions Screenshot

Screenshot showing both successful CI/CD jobs:

```text
Run Tests                    ✓
Build and Push Docker Image  ✓
```

---

## Conclusion

The DevOps Task Tracker demonstrates a complete CI/CD workflow for a Flask web application.

The project includes:

- Flask web application development
- Automated testing using pytest
- Git version control
- GitHub source code management
- Docker containerization
- Docker Compose local deployment
- Docker Hub image publishing
- GitHub Actions CI/CD automation
- Secure Docker Hub authentication using GitHub Secrets
- Local application and health-check verification

The completed pipeline connects source code changes with automated testing, Docker image creation, and Docker Hub publishing.