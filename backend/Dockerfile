# backend/Dockerfile
FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps (adjust if needed)
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc --no-install-recommends && rm -rf /var/lib/apt/lists/*

# copy only requirements first for caching
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# copy application code
COPY . /app

# collect static (optional - adjust STATIC settings in Django)
# RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Command: run with Gunicorn. Assumes Django wsgi: config.wsgi:application
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]
