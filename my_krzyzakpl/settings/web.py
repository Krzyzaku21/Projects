# python manage.py runserver --settings settings.web
from my_krzyzakpl.settings import *
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open("/secret_keys/keys_my_krzyzakpl.json") as config_file:
    config = json.load(config_file)

SECRET_KEY = config["SECRET_KEY"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config["NAME"],
        "USER": config["USER"],
        "PASSWORD": config["PASSWORD"],
        "HOST": config["HOST"],
        "PORT": "3306",
    }
}

DEBUG = False

ALLOWED_HOSTS = ["www.krzyzak21.pl", "krzyzak21.pl", "panel.krzyzak21.pl"]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
