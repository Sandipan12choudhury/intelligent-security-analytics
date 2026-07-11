# =============================================================================
# Intelligent Security Analytics Platform - Backend Dockerfile
#
# Build from the PROJECT ROOT (not from inside backend/):
#     docker build -f backend/Dockerfile -t isap-backend .
#
# Run:
#     docker run -p 8000:8000 --env-file .env isap-backend
# =============================================================================

FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Application code and the datasets it reads from

COPY backend/ backend/
COPY ai/ ai/
COPY ml/ ml/
COPY dataset/ dataset/

# Created automatically at runtime (SQLite DB, generated PDF reports)
# but declared here so they exist even before the app writes to them

RUN mkdir -p reports database

EXPOSE 8000

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
