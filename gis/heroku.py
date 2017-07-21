from .settings import *
import os
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ['SOCIAL_AUTH_FACEBOOK_SECRET']
SECRET_KEY = os.environ['SECRET_KEY']
SOCIAL_AUTH_FACEBOOK_KEY = os.environ['SOCIAL_AUTH_FACEBOOK_KEY']
GOOGLE_MAPS_API_KEY = os.environ['GOOGLE_MAPS_API_KEY']



