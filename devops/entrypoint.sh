#!/bin/sh
# Enter entrypoint commands here
python manage.py collectstatic --no-input --clear
gunicorn files.wsgi --name aether-files --workers 3 --bind 0.0.0.0:8000
exec "$@"