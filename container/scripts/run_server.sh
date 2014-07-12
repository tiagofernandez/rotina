#!/bin/bash

echo "Setting environment variables..."
export SECRET_KEY=${SECRET_KEY-'b1x=p%9e^@^k_-%*vt2zvs1!p5=xr#qas*_lmxd238#mn=rxsg'}
export DB_HOST=${DB_HOST-localhost}
export DB_PORT=${DB_PORT-5432}
export DB_NAME=${DB_NAME-rotina}
export DB_USER=${DB_USERNAME-rotina}
export DB_PASSWORD=${DB_PASSWORD-rotina}
printenv

echo "Running migrations..."
python3 /app/manage.py migrate

echo "Loading fixtures..."
python3 /app/manage.py loaddata rotina/apps/core/fixtures/initial_data.json

echo "Starting application server..."
CMD=${1:-"gunicorn rotina.wsgi:application \
    --access-logfile=/logs/gunicorn_access.log \
    --error-logfile=/logs/gunicorn_error.log \
    --chdir=/app --workers=4 --bind 0.0.0.0:8000"}
$CMD
