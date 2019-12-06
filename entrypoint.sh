#!/bin/sh
set -e

python manage.py migrate
#python manage.py compress
python manage.py collectstatic --no-input
chmod 755 static/ -R
gunicorn config.wsgiDocker:application \
         --bind 0.0.0.0:8000  \
         --workers=2 \
         --timeout=300
