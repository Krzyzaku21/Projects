# python manage.py runserver --settings settings.web
from my_krzyzak21.settings import *
import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open('/secret_keys/keys_my_krzyzak21.json') as config_file:
    config = json.load(config_file)

SECRET_KEY = config['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['NAME'],
        'USER': config['USER'],
        'PASSWORD': config['PASSWORD'],
        'HOST': config['HOST'],
        'PORT': '5432',
    }
}

DEBUG = False

ALLOWED_HOSTS = ["www.krzyzak21.space", "krzyzak21.space"]

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# EMAILS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
