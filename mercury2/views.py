""" @package mercury2.views
This module contains top-level views for the Mercury2 user interface that don't fit with the other applications. 
"""

from django.shortcuts import render_to_response

def home(request):
  """ This view is responsible for generating the Mercury2 homepage, which will be displayed to all unauthenticated
  users.
  """

  return render_to_response('mercury2/home.html')