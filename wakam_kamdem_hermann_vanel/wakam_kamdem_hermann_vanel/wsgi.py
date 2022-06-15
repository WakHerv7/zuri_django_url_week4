"""
WSGI config for wakam_kamdem_hermann_vanel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wakam_kamdem_hermann_vanel.settings')

application = get_wsgi_application()
