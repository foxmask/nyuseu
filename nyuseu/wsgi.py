# coding: utf-8
"""
Nyuseu :: News :: 뉴스

WSGI config for nyuseu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nyuseu.settings')

application = get_wsgi_application()
