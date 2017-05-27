release: python manage.py makemigrations CRMapp && python manage.py migrate --no-input
web: gunicorn CRM.wsgi --log-file -
