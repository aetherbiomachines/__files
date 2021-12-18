#!/bin/sh

# Enter entrypoint commands here
#spython manage.py collectstatic --no-input --clear
gunicorn analytics.wsgi --env DJANGO_SETTINGS_MODULE=settings.production --name aether-analytics --workers 3 --bind 0.0.0.0:8000 
exec "$@"
