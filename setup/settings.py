"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from django.core.management.utils import get_random_secret_key
import os
import json
from pathlib import Path
import logging.config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
ENV = os.environ.get("ENV", "dev")
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost,*").split(",")

if ENV == "dev":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'storages',
    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'dj_rest_auth.registration',
    'users',
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

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {}
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + os.environ.get('DBENGINE', 'sqlite3'),
        'NAME': os.environ.get('DBNAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.environ.get('DBUSER', ''),
        'PASSWORD': os.environ.get('DBPASSWORD', ''),
        'HOST': os.environ.get('DBHOST', '127.0.0.1'),
        'PORT': os.environ.get('DBPORT', '3306'),
        'OPTIONS': json.loads(
             os.getenv('DATABASE_OPTIONS', '{}')
         ),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.CustomUser'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / "static",
    # '/var/www/static/',
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = "staticfiles/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email configuration
if ENV == "dev":
    STATIC_URL = 'static/'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", True)
    EMAIL_PORT = os.environ.get("EMAIL_PORT", 587)
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", 'dummy@ktechhub.com')
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", '')
    EMAIL_USE_SSL = False
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    SERVER_EMAIL = "info@ktechhub.com"

    # DO Spaces
    AWS_ACCESS_KEY_ID = os.getenv('STATIC_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.getenv('STATIC_SECRET_KEY', '')

    AWS_STORAGE_BUCKET_NAME = os.getenv('STATIC_BUCKET_NAME', '')
    AWS_S3_ENDPOINT_URL = os.getenv('STATIC_ENDPOINT_URL', '')
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_LOCATION = "static"
    AWS_DEFAULT_ACL = 'public-read'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'setup.storage_backends.MediaStorage'
    STATIC_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, AWS_LOCATION)

# Rest Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'users.serializers.CustomRegisterSerializer'
}
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'users.serializers.CustomUserDetailsSerializer',
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
OLD_PASSWORD_FIELD_ENABLED = True
REST_AUTH_PW_RESET_USE_SITES_DOMAIN=True

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=1
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_VERIFICATION="mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET=True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION=False # Login user after verifying email
ACCOUNT_LOGIN_ON_PASSWORD_RESET=True
ACCOUNT_USERNAME_BLACKLIST=["admin",]
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_USER_MODEL_USERNAME_FIELD="username"
ACCOUNT_USERNAME_REQUIRED=False
ACCOUNT_AUTHENTICATION_METHOD="username_email"

SITE_ID = 1

# Logging Configuration
## Clear prev config
LOGGING_CONFIG = None
## Get loglevel from env
LOGLEVEL = os.getenv('DJANGO_LOGLEVEL', 'info').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console',],
        },
    },
})