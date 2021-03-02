#python manage.py runserver --settings settings.web
from my_krzyzak21.settings import *

DEBUG = False

ALLOWED_HOSTS = ["www.krzyzak21.space", "krzyzak21.space"]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')