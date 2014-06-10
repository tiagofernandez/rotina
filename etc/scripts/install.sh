#!/bin/bash

source /scripts/set_env.sh

echo "Installing required dependencies..."
pip install https://www.djangoproject.com/download/1.7.b4/tarball/
pip install -r /app/requirements/prod.txt
