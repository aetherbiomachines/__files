from settings import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'lims-stg-db1.cvsjiwtmbmak.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
