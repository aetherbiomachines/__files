from settings import *

DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '${{ secrets.STAGINGPW }}',
        'HOST': '${{ secrets.STAGINGDB }}',
        'PORT': '5432',
    }
}
