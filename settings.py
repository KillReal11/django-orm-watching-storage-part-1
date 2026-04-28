import os
from dotenv import load_dotenv
load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('SECURITY_DB_HOST'),
        'PORT': os.getenv('SECURITY_DB_PORT'),
        'NAME': os.getenv('SECURITY_DB_NAME'),
        'USER': os.getenv('SECURITY_DB_USER'),
        'PASSWORD': os.getenv('SECURITY_DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECURITY_SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
