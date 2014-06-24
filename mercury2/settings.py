""" @package mercury2.settings
This module contains the settings for the Mercury2 User Interface.

@see https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Ground station specific settings (override in local_settings.py)
SECRET_KEY = 'your-super-duper-secret-key'
DEBUG = False
TEMPLATE_DEBUG = False

# Django project configuration
SITE_ID = 1
ROOT_URLCONF = 'mercury2.urls'
WSGI_APPLICATION = 'mercury2.wsgi.application'
AUTH_USER_MODEL = 'operators.StationUser'
ALLOWED_HOSTS = []

STATIC_URL = '/static/'

INSTALLED_APPS = (
  # Mercury2 applications
  'mercury2',
  'operators',

  # Django and external applications
  'allauth',
  'allauth.account',
  'django.contrib.sites',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles'
)

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
  "django.contrib.auth.context_processors.auth",
  "django.core.context_processors.request",
  "django.contrib.messages.context_processors.messages",
  "allauth.account.context_processors.account",
  "allauth.socialaccount.context_processors.socialaccount"
)

AUTHENTICATION_BACKENDS = (
  "django.contrib.auth.backends.ModelBackend",
  "allauth.account.auth_backends.AuthenticationBackend"
)

# Internationalization options
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# django-allauth configuration
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_USERNAME_MIN_LENGTH = 3

# Logging configuration
LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'verbose': {
      'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
      'datefmt' : "%d/%b/%Y %H:%M:%S"
    },
    'simple': {
      'format': '%(levelname)s %(message)s'
    },
  },
  'handlers': {
    'django_file': {
      'level': 'DEBUG',
      'class': 'logging.FileHandler',
      'filename': 'logs/django.log',
      'formatter': 'verbose'
    },
    'mercury2_file': {
      'level': 'DEBUG',
      'class': 'logging.FileHandler',
      'filename': 'logs/mercury2.log',
      'formatter': 'verbose'
    },
  },
  'loggers': {
    '': {
      'handlers': ['mercury2_file'],
      'level': 'INFO',
    },
    'django': {
      'handlers':['django_file'],
      'propagate': False,
      'level':'INFO',
    }
  }
}
