web: gunicorn mysite.wsgi --log-file -
celery -A mysite.celery worker --pool=solo -l info