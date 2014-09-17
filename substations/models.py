""" @package groundstation.models
This module contains the models used to represent HWM substations, pipelines, devices, and commands.

Many of the models in this module contain read-only attributes that will be periodically synchronized with the ground
station's static configuration (via the API). Most substation, pipeline, and device configuration settings are specified 
in the substation's configuration and mirrored to the user interface in this fashion.
"""

import logging
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from jsonfield import JSONField

class Substation(models.Model):
  """ The Substation model represents Mercury2 Hardware Manager installations.

  The Hardware Manager component of Mercury2 is responsible for managing and providing access to a set of hardware 
  devices. A ground station typically contains one or more HWM instances, or 'substations'. Substations are comprised of
  devices and pipelines, which are specified in the substation's configuration by the ground station administrator.
  """

  # Substation attributes
  title = models.CharField(_('title'),
                           help_text=_('A human-readable title for the substation.'),
                           max_length=100)
  slug = models.SlugField(_('URL slug'),
                          help_text=_('A URL friendly slug that will be used to reference the substation.'),
                          max_length=100,
                          unique=True)
  longitude = models.DecimalField(_('longitude'),
                                  help_text=_('The east/west longitude of the substation.'),
                                  max_digits=6,
                                  decimal_places=3,
                                  blank=True,
                                  editable=False)
  latitude = models.DecimalField(_('latitude'),
                                 help_text=_('The latitude of the substation.'),
                                 max_digits=5,
                                 decimal_places=3,
                                 blank=True,
                                 editable=False)
  altitude = models.IntegerField(_('altitude'),
                                 help_text=_('The altitude (above sea level) of the substation in meters.'),
                                 blank=True,
                                 editable=False)
  public_address = models.CharField(_('public address'),
                                    help_text=_('A publicly accessible domain or IP address that routes to the '\
                                                'substation'),
                                    max_length=100,
                                    blank=True,
                                    editable=False)
  data_port = models.IntegerField(_('data port'),
                                  help_text=_('The port used to access substation pipeline data streams. Must be '\
                                              'reachable from the substation\'s public address.'),
                                  blank=True,
                                  editable=False)
  telemetry_port = models.IntegerField(_('telemetry port'),
                                       help_text=_('The port used to access substation pipeline telemetry streams. '\
                                                   'Must be reachable from the substation\'s public address.'),
                                       blank=True,
                                       editable=False)
  command_port = models.IntegerField(_('command port'),
                                     help_text=_('The port used to submit commands to the substation. Must be '\
                                                 'reachable from the substation\'s public address.'),
                                     blank=True,
                                     editable=False)
  commands = GenericRelation('Command')
  events = GenericRelation('Event')
  state = JSONField(help_text=_('A JSON object containing the substation\'s most recent state as reported by the '\
                            'substation.'),
                    blank=True,
                    editable=False)
  configuration = JSONField(help_text=_('Contains the substation\'s configuration settings as defined in its '\
                                        'configuration.yml file.'),
                            blank=True,
                            editable=False)

  class Meta:
    verbose_name = _('substation')
    verbose_name_plural = _('substations')

class Pipeline(models.Model):
  """ A pipeline is a set of devices that are commonly used together to perform a task.
  
  Pipelines are used to group devices that are frequently used together (such as a radio and antenna controller) into 
  easily schedulable units. Satellite operators will schedule access to a particular pipeline, which will provide data, 
  telemetry, and command ports. Devices may belong to multiple pipelines, with the device configuration specifying how 
  the device should be shared.
  """

  # Pipeline attributes
  title = models.CharField(_('title'),
                           help_text=_('A short, human-readable title for the pipeline.'),
                           max_length=100)
  pipeline_id = models.CharField(_('pipeline ID'),
                                 help_text=_('The ID of the pipeline as specified in the substation\'s pipeline '\
                                             'configuration file. This is used to reference the pipeline throughout '\
                                             'Mercury2.'),
                                 max_length=100,
                                 unique=True,
                                 blank=True,
                                 editable=False)
  description = models.TextField(_('description'),
                                 help_text=_('A brief description of the pipeline explaining its capabilities and '\
                                             'usage.'),
                                 blank=True)
  substation = models.ForeignKey('Substation', 
                                 help_text=_('The substation that contains the pipeline.'))
  devices = models.ManyToManyField('Device')
  events = GenericRelation('Event')
  state = JSONField(help_text=_('A JSON object containing the pipeline\'s most recent state as reported by the '\
                              'substation.'),
                    blank=True,
                    editable=False)

  class Meta:
    verbose_name = _('pipeline')
    verbose_name_plural = _('pipelines')

class Device(models.Model):
  """ A device is a component of a substation that performs some task (or tasks) for its pipelines.

  Devices can either be virtual or physical. Virtual devices are devices that exist purely in code or provide access to 
  some other service (such as a SGP4 propagator) while physical devices provide access to some physical hardware device
  (such as a radio). A dictionary containing the device's static configuration can be accessed via the device's 
  'configuration' attribute. 
  """

  # Device attributes
  title = models.CharField(_('title'),
                           help_text=_('A short, human-readable title for the device.'),
                           max_length=100)
  device_id = models.CharField(_('device ID'),
                               help_text=_('The unique ID of the device as specified in the substation\'s device '\
                                           'configuration file.'),
                               max_length=100,
                               unique=True,
                               blank=True,
                               editable=False)
  description = models.TextField(_('description'),
                                 help_text=_('A brief description of the device describing its capabilities and '\
                                             'operation.'),
                                 blank=True)
  substation = models.ForeignKey('Substation',
                                 help_text=_('The substation that the device belongs to.'))
  commands = GenericRelation('Command')
  events = GenericRelation('Event')
  state = JSONField(help_text=_('A JSON object containing the device\'s most recent state as reported by the '\
                                'substation.'),
                    blank=True,
                    editable=False)
  configuration = JSONField(help_text=_('The device\'s static configuration as defined in its substation\'s '\
                                        'devices.yml file.'),
                            blank=True,
                            editable=False)

  class Meta:
    verbose_name = _('device')
    verbose_name_plural = _('devices')

class Command(models.Model):
  """ Commands expose some device or substation functionality to the user.

  Commands are defined in the HWM by command handlers and can either be device or system level commands. Device commands
  provide some functionality for a specific device, while system commands provide generic or subsystem-wide 
  functionality. The 'metadata' field contains a JSON schema that defines command meta-data, including information about 
  the arguments it takes.
  """

  # Command attributes
  title = models.CharField(_('title'),
                           help_text=_('A brief human-readable title for the command.'),
                           max_length=100)
  command_id = models.CharField(_('title'),
                                help_text=_('A unique ID of the command that is used to reference the command.'),
                                max_length=100,
                                unique=True,
                                blank=True,
                                editable=False)
  description = models.TextField(_('description'),
                                 help_text=_('A brief description of the device describing its effects and operation.'),
                                 blank=True,
                                 editable=False)
  metadata = JSONField(help_text=_('Contains a JSON schema that specifies information about the command\'s arguments.'),
                       blank=True,
                       editable=False)

  content_type = models.ForeignKey(ContentType)
  object_id = models.PositiveIntegerField()
  destination = GenericForeignKey('content_type', 'object_id')

  class Meta:
    verbose_name = _('command')
    verbose_name_plural = _('commands')
