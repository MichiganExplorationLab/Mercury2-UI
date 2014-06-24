""" @package mercury2.local_settings
This module contains local settings for the Mercury2 user interface.
"""

from mercury2.settings import *

SECRET_KEY = 'your-super-duper-secret-key'
ADMINS = (
  ('Admin', 'admin@localhost.com')
)
MANAGERS = ADMINS

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'db-database',                      
    'USER': 'db-username',
    'PASSWORD': 'db-password',
    'HOST': 'localhost'
  }
}
