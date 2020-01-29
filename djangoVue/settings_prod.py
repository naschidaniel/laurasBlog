import os
from djangoVue.settings import *
import environ

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('POSTGRESQL_NAME'),
#         'USER': env('POSTGRESQL_USER'),
#         'PASSWORD': env('POSTGRESQL_PASSWORD'),
#         'HOST': 'db',
#         'PORT': env('POSTGRESQL_PORT'),
#     }
# }
