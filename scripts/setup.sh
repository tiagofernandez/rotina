#!/bin/bash

# Activate the virtualenv
. $HOME/.virtualenvs/rotina/bin/activate

# Install the required dependencies
pip install https://www.djangoproject.com/download/1.7.b4/tarball/
pip install -r $HOME/rotina/requirements.txt
