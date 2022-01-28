#!/bin/bash

# Collect static files
echo "Collect static files"
# python manage.py collectstatic --noinput
echo "Collect static files finished...."

# Apply database migrations
echo "Starting make database migrations"
python manage.py makemigrations
echo "Database migrations finished...."

# Apply database migrations
echo "Starting Apply database migrations"
python manage.py migrate
echo "Apply database migrations finished...."

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
echo "Server started successfully...."

