#!/bin/bash

# Ensure script is executable
# chmod +x deploy.sh

# Pull latest changes
git pull origin main

# Collect static files
docker compose run --rm django python manage.py collectstatic --noinput

# Run migrations
docker compose run --rm django python manage.py migrate

# Rebuild and restart containers
docker compose down
docker compose up --build -d

# Cleanup old images
docker image prune -f