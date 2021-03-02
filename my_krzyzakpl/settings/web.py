#python manage.py runserver --settings settings.web
from my_krzyzakpl.settings import *

DEBUG = False

ALLOWED_HOSTS = ["www.krzyzak21.pl", "krzyzak21.pl"]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')