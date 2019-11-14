from .base import *

import pymysql


DEBUG = False
ADMINS = (
    ('CZM', 'jimmychanyzy@gmail.com'),
)
ALLOWED_HOSTS = ['*']
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'ms',
        'USER': 'root',
        'PASSWORD': 'czm850510!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}