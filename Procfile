release: python manage.py migrate --no-input && python manage.py create_admin
web: gunicorn config.wsgi
