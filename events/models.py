""" @package events.models
This module contains models that are used to log events from the user interface and hardware manager.
"""

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from jsonfield import JSONField

class Event(models.Model):
  """ Records log entries for Mercury2. 

  The Event model is used to record logging events that can originate from the user interface or the hardware manager 
  via the state reporting API. 
  """ 

  message = models.TextField(_('message'),
                             help_text=_('The log message.'),
                             blank=False,
                             editable=False)
  metadata = JSONField(help_text=_('A JSON object containing additional meta-data about the event.'),
                       blank=True,
                       editable=False)

  content_type = models.ForeignKey(ContentType)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id')
