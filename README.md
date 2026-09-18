# ✈️ Wanderly – Travel Planner

A modern Flask travel-planning web application created for the CSI2113 practical assessment.

## Features

- Beautiful responsive travel homepage
- Destination discovery page with travel photography
- Embedded travel inspiration video
- Personal trip-planning form
- Saved trip cards
- Flask health-check endpoint
- Automated pytest tests
- Docker + Docker Compose support
- GitHub Actions CI/CD support

## Run locally

```bash
python -m pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

## Run with Docker Compose

```bash
docker compose up --build
```

Open http://localhost:5000

## Project structure

```text
.github/workflows/ci-cd.yml
static/style.css
templates/base.html
templates/index.html
templates/destinations.html
templates/plan.html
tests/test_app.py
app.py
Dockerfile
docker-compose.yml
requirements.txt
```

> Note: destination photos and the inspiration video are loaded from external web services, so an internet connection is needed for those visual assets. The Flask application itself runs locally.
