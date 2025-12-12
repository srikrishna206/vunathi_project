# backend/Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Create logs directory (Django expects this)
RUN mkdir -p /app/logs && chmod -R 777 /app/logs

# Install system deps for PostgreSQL, psycopg2, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev gcc curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]
