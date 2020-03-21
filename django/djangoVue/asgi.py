"""
ASGI config for djangoVue
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoVue.settings')

application = get_asgi_application()
