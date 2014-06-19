""" @package mercury2.urls
This package defines the top-level URL routes for the Mercury2 user interface.
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'mercury2.views.home', name='home'),
  url(r'^admin/', include(admin.site.urls)),
)
