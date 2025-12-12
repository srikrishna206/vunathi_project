#!/bin/bash

echo "Starting NOVYA LMS Deployment..."

# Check if Docker and Docker Compose are installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Build and start containers
echo "Building and starting containers..."
docker-compose down
docker-compose build --no-cache
docker-compose up -d

# Wait for services to start
echo "Waiting for services to start..."
sleep 30

# Run database migrations
echo "Running database migrations..."
docker-compose exec backend python manage.py migrate

# Create superuser (optional - uncomment if needed)
# echo "Creating superuser..."
# docker-compose exec backend python manage.py createsuperuser

# Collect static files
echo "Collecting static files..."
docker-compose exec backend python manage.py collectstatic --noinput

echo "Deployment completed!"
echo "Frontend: http://localhost"
echo "Backend API: http://localhost:8000"
echo "AI Backend: http://localhost:8001"
echo "PostgreSQL: localhost:5432"
