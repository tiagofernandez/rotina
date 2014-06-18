#!/bin/bash

source set_env.sh

echo "Installing required dependencies..."
pip install https://www.djangoproject.com/download/1.7.b4/tarball/
pip install --upgrade -r requirements/prod.txt
