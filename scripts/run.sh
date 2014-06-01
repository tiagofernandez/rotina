#!/bin/bash

# Set the environment variables
export SECRET_KEY="a2z=m%0s^@^r_-%*yp3qck4!i1=di#oip*_dwqy836#gi=jlnr"
export DATABASE_NAME="rotina"
export DATABASE_USER="rotina"
export DATABASE_PASSWORD="rotina"
export DATABASE_HOST="localhost"
export DATABASE_PORT="5432"

# Activate the virtualenv
. $HOME/.virtualenvs/rotina/bin/activate

# Run the application server
python $HOME/rotina/manage.py runserver 0.0.0.0:8000
