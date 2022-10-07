from pathlib import Path
import os
from yamuna_canal_monitoring import configs

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = configs.BASE_DIR
PROJECT_PATH = configs.PROJECT_PATH

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = configs.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = configs.DEBUG

ALLOWED_HOSTS = configs.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps
    'auth_app',
    'monitoring_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = configs.ROOT_URLCONF

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(PROJECT_PATH, 'auth_app/templates/'),
                os.path.join(PROJECT_PATH, 'monitoring_app/templates/'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yamuna_canal_monitoring.wsgi.application'


# Database
DATABASES = configs.DATABASES



# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# STATICFILES_DIRS = ( 
#     #   os.path.join(PROJECT_PATH, 'auth_app/static/'), 
#       os.path.join(PROJECT_PATH, 'monitoring_app/static'),  
# )

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240  # higher than the count of fields

DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880 * 10  # 5mb * 10 incase of multiple years on graph


# Logging Setup
# can set environ LOGLEVEL=debug/info/error etc
LOG_PATH = configs.LOG_PATH
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
LOGGING = configs._LOGGING



# Celery
# sudo service rabbitmq-server restart # if connection refused error
ANONYMOUS_USER_NAME = 'AnonymousUser'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER = configs.EMAIL_USER
EMAIL_HOST_PASSWORD = configs.EMAIL_PASSWORD
# OTP_RECVR_CC = configs.OTP_RECVR_CC
RECEIVER = ['rohit.kumar@i-telemetry.com']




DJANGO_NOTIFICATIONS_CONFIG = {
    'USE_JSONFIELD': True,
    'SOFT_DELETE': False, # delete from DB if False
    'NUM_TO_FETCH': 500
}
