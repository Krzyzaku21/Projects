#python manage.py runserver --settings settings.local
from my_gless.settings import *

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]