web: gunicorn projeto.wsgi --log-file -
release: python3 manage.py migrate && python3 manage.py collectstatic --noinput