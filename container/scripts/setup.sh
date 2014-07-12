#!/bin/bash

echo "Installing required dependencies..."
pip3 install https://www.djangoproject.com/download/1.7.b4/tarball/
pip3 install --upgrade -r /app/requirements/prod.txt
