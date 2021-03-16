# python manage.py runserver --settings settings.web
from my_gless.settings import *
import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open('/secret_keys/keys_my_gless.json') as config_file:
    config = json.load(config_file)

SECRET_KEY = config['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config['NAME'],
        'USER': config['USER'],
        'PASSWORD': config['PASSWORD'],
        'HOST': config['HOST'],
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

SOCIAL_AUTH_GITHUB_KEY = config['SOCIAL_AUTH_GITHUB_KEY']
SOCIAL_AUTH_GITHUB_SECRET = config['SOCIAL_AUTH_GITHUB_SECRET']

SOCIAL_AUTH_FACEBOOK_KEY = config['SOCIAL_AUTH_FACEBOOK_KEY']
SOCIAL_AUTH_FACEBOOK_SECRET = config['SOCIAL_AUTH_FACEBOOK_SECRET']


# EMAIL RESPONSE

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DEBUG = False

ALLOWED_HOSTS = ["www.gless.click", "gless.click"]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
