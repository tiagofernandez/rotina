from rotina.settings.common import *

INSTALLED_APPS += (
   'django_extensions',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rotina',
        'USER': 'rotina',
        'PASSWORD': 'rotina',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
