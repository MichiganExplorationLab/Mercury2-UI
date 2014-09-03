""" @package mercury2.urls
This package defines the top-level URL routes for the Mercury2 user interface.
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
#from administration.admin import mercury2_admin

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'mercury2.views.home', name='home'),
  url(r'^users/', include('allauth.urls')),
  url(r'^admin/', include(admin.site.urls)),
  #url(r'^admin/', include(mercury2_admin.urls)),
)
