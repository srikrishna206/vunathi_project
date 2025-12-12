#!/bin/bash

# Set Django settings module
export DJANGO_SETTINGS_MODULE=config.settings

# Wait for database to be ready
echo "Waiting for database..."
while ! nc -z postgres 5432; do
  sleep 0.1
done
echo "Database is ready!"

# Check database connection
python -c "
import django
from django.conf import settings
django.setup()
from django.db import connection
try:
    connection.ensure_connection()
    print('✅ Database connection successful')
except Exception as e:
    print('❌ Database connection failed:', e)
    exit(1)
"

# Apply migrations (with error handling)
echo "Applying migrations..."
python manage.py migrate --noinput || {
    echo "Migration failed, trying to continue..."
}

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 config.wsgi:application
