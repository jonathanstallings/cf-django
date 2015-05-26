"""
WSGI config for cf_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling  # Modified for Heroku deployment

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cf_django.settings")

application = Cling(get_wsgi_application())  # Modified for Heroku
