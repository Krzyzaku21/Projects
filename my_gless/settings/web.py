#python manage.py runserver --settings settings.web
from my_gless.settings import *

DEBUG = False

ALLOWED_HOSTS = ["www.gless.click", "gless.click"]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')