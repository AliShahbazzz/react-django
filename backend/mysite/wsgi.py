"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
os.environ.setdefault(
    'SECRET_KEY', 'rtsf2lk+sw@ap$qv4ps&#&na6c1hp5+91nly(^1@lez4c#g#!)')

application = get_wsgi_application()
