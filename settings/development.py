from settings import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

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
