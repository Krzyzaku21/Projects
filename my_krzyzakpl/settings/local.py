#python manage.py runserver --settings settings.local
from my_krzyzakpl.settings import *

DEBUG = True

ALLOWED_HOSTS = []

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')