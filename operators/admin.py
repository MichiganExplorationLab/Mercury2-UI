""" @package operators.admin
This module contains custom Admin classes for managing ground station users.
"""

from django.contrib.auth.admin import UserAdmin
from administration.admin import mercury2_admin
from operators.models import StationUser

class StationUserAdmin(UserAdmin):
  pass

mercury2_admin.register(StationUser, StationUserAdmin)