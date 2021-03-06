"""
WSGI config for baseapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""


import os
from django.core.wsgi import get_wsgi_application

project_name = os.path.dirname(os.path.abspath(__file__)).split('/')[-1]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{project_name}.settings')

application = get_wsgi_application()
