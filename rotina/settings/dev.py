from rotina.settings.common import *

INSTALLED_APPS += (
   'django_extensions',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'rotina',
        'USER': 'rotina',
        'PASSWORD': 'rotina',
    }
}
