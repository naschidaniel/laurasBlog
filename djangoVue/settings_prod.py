import os
from djangoVue.settings import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRESQL_NAME'],
        'USER': os.environ['POSTGRESQL_USER'],
        'PASSWORD': os.environ['POSTGRESQL_PASSWORD'],
        'HOST': 'db',
        'PORT': os.environ['POSTGRESQL_PORT'],
    }
}
