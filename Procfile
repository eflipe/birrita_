release: python birrita_root/manage.py makemigrations
release: python birrita_root/manage.py migrate
web: gunicorn --pythonpath birrita_root birrita_site.wsgi --log-file -
