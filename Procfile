release: python3 manage.py migrate --noinput && python3 manage.py collectstatic --noinput
web: gunicorn e_commers-projek-django.wsgi