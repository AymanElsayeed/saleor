#!/bin/sh
set -e
cd /app

# Run migrations first (creates/updates tables)
python3 manage.py migrate --no-input

# Create admin user if none exists (idempotent: admin@example.com / admin)
python3 docker-create-admin.py

exec "$@"
