from settings import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

MIDDLEWARE.append('silk.middleware.SilkyMiddleware')
INSTALLED_APPS.append('silk')
SILKY_PYTHON_PROFILER = True

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '${{ secrets.DEVPW }}',
        'HOST': '${{ secrets.DEVDB }}',
        'PORT': '5432',
    }
}
