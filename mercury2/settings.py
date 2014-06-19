""" @package mercury2.settings
This module contains the settings for the Mercury2 User Interface.

@see https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Ground station specific settings (override in local_settings.py)
SECRET_KEY = 'your-super-secret-key'
ADMINS = (
  ('Your Name', 'your.email@gmail.com')
)
MANAGERS = ADMINS
DEBUG = True
TEMPLATE_DEBUG = True
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'mercury2',                      
    'USER': 'mercury2',
    'PASSWORD': 'devpassword',
    'HOST': ''
  }
}

# UI application configuration
INSTALLED_APPS = (
  # Mercury2 applications
  'mercury2',

  # Django and external applications
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mercury2.urls'
WSGI_APPLICATION = 'mercury2.wsgi.application'

STATIC_URL = '/static/'

ALLOWED_HOSTS = []

# Internationalization options
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

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
