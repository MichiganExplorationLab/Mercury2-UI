""" @package operators.models
This module includes models related to ground station and satellite operators such as a custom User model.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class StationUser(AbstractUser):
  """ A custom user model that provides some additional fields and functionality needed for Mercury2. """
  
  organization = models.CharField('Organization', help_text='The organization you represent.', blank=True, 
                                  max_length=100)
  city = models.CharField('City', help_text='Your city of residence.', max_length=100, blank=True)
  region = models.CharField('Region', help_text='The region or state that you live in.', max_length=50, blank=True)
  country = models.CharField('Country', max_length=2, blank=True)
