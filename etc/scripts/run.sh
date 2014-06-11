#!/bin/bash

echo "Setting environment variables..."
export SECRET_KEY=${SECRET_KEY-'a2z=m%0s^@^r_-%*yp3qck4!i1=di#oip*_dwqy836#gi=jlnr'}
export DB_NAME=${DB_NAME-rotina}
export DB_USER=${DB_USER-rotina}
export DB_PASSWORD=${DB_PASSWORD-rotina}
export DB_HOST=${DB_HOST-localhost}
export DB_PORT=${DB_PORT-5432}

source set_env.sh

echo "Running migrations..."
python manage.py migrate

echo "Starting application server..."
python manage.py runserver 0.0.0.0:8000
