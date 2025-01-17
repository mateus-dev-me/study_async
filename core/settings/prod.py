# prod.py
from .base import *
import json

DEBUG = False
ALLOWED_HOSTS = ['study_async.mateus-dev-me.com.br']

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'OPTIONS': json.loads(
             os.getenv('DATABASE_OPTIONS', '{}')
         ),
    }
}


SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
