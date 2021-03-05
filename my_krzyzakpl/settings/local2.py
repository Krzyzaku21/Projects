# python manage.py runserver --settings settings.local2
from my_krzyzakpl.settings import *
import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open('C:/Users/Krzyz/Desktop/Radek Python/secret_keys/keys_my_krzyzakpl.json') as config_file:
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
    }
}


DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
