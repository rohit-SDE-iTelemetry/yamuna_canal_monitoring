from pathlib import Path
import os
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'django-insecure-=nq(4v6l4k4oljjpd55(_d%50)h4q3cfmjn$^!ef-9v1w06+9&'

DEBUG = True

ROOT_URLCONF = 'yamuna_canal_monitoring.urls'

LOG_PATH = os.path.join('/var/log/', 'eyc')
EMAIL_USER = 'notifications@aaxisnano.com'
EMAIL_PASSWORD = 'jsdhye#@#456'
# OTP_RECVR_CC = ['sms.cpcb@nic.in']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'mydb',
    #     'USER': 'postgres',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': 5432,
    # }
}

_LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s (%(levelname)s) [%(module)s:%(lineno)d]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
}

