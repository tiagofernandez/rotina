from os import environ
from rotina.settings.common import *

SECRET_KEY = environ['SECRET_KEY']

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': environ['DB_HOST'],
        'PORT': environ['DB_PORT'],
        'NAME': environ['DB_NAME'],
        'USER': environ['DB_USER'],
        'PASSWORD': environ['DB_PASSWORD'],
    }
}

INSTALLED_APPS += (
    'gunicorn',
)
