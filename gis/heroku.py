import os
import dj_database_url
import django_heroku

from .settings import *

DEBUG = False
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')
SECRET_KEY = os.environ.get('SECRET_KEY')
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')


django_heroku.settings(locals())

