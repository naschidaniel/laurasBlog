import os
from djangoVue.settings import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS']
