web: gunicorn muypicky.wsgi
web: python muypicky/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT muypicky/settings.py 
