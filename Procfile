web: bash -c "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn registro_proveedores.wsgi --bind 0.0.0.0:$PORT"
