# Save this file as local.py
from .base import *

SECRET_KEY = "**** Make this unique and don't share with anybody."

# Set correct credentials for production
SERVER_EMAIL = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

RECAPTCHA_PUBLIC_KEY = '****'
RECAPTCHA_PRIVATE_KEY = '****'
RECAPTCHA_USE_SSL = True

NEWSLETTER_API_KEY = '****'
NEWSLETTER_DEFAULT_LIST_ID = '****'
