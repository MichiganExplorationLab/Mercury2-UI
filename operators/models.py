""" @package operators.models
This module includes models related to ground station and satellite operators such as a custom User model.
"""

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

class StationUser(AbstractUser):
  """ A custom user model that provides some additional fields and functionality needed for Mercury2. """
  
  organization = models.CharField(_('organization'), help_text=_('The organization that you\'re associated with.'),
                                  blank=True, max_length=100)
  city = models.CharField(_('city'), max_length=100, blank=True)
  region = models.CharField(_('region'), help_text=_('The region or state that you live in.'), max_length=50, 
                            blank=True)
  country = models.CharField(_('country'), max_length=2, blank=True)
