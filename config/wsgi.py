"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Nuclear option: Run migrations and create_admin at startup
try:
    print("--- Bootstrapping Database ---")
    call_command('migrate', interactive=False)
    call_command('create_admin')
    print("--- Bootstrap Complete ---")
except Exception as e:
    print(f"--- Bootstrap Error: {e} ---")

application = get_wsgi_application()
