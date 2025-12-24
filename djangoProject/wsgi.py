# """
# WSGI config for djangoProject project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

# application = get_wsgi_application()


import os
import sys

path = '/home/YOUR_USERNAME/online_shop'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoProject.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()