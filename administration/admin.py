""" @package administration.admin 
This module contains a custom AdminSite for the Mercury2 user interface that provides custom administration
functionality.
"""

from django.contrib.admin import AdminSite

class Mercury2AdminSite(AdminSite):
  """ This AdminSite provides custom views and functionality for the Mercury2 User Interface administration panel. """

  pass

mercury2_admin = Mercury2AdminSite(name="mercury2_admin")
