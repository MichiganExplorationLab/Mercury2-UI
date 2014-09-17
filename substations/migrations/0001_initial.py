# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=100, help_text='A brief human-readable title for the command.')),
                ('command_id', models.CharField(blank=True, unique=True, verbose_name='title', max_length=100, editable=False, help_text='A unique ID of the command that is used to reference the command.')),
                ('description', models.TextField(blank=True, help_text='A brief description of the device describing its effects and operation.', editable=False, verbose_name='description')),
                ('metadata', jsonfield.fields.JSONField(blank=True, editable=False, help_text="Contains a JSON schema that specifies information about the command's arguments.")),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'command',
                'verbose_name_plural': 'commands',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=100, help_text='A short, human-readable title for the device.')),
                ('device_id', models.CharField(blank=True, unique=True, verbose_name='device ID', max_length=100, editable=False, help_text="The unique ID of the device as specified in the substation's device configuration file.")),
                ('description', models.TextField(blank=True, verbose_name='description', help_text='A brief description of the device describing its capabilities and operation.')),
                ('state', jsonfield.fields.JSONField(blank=True, editable=False, help_text="A JSON object containing the device's most recent state as reported by the substation.")),
                ('configuration', jsonfield.fields.JSONField(blank=True, editable=False, help_text="The device's static configuration as defined in its substation's devices.yml file.")),
            ],
            options={
                'verbose_name': 'device',
                'verbose_name_plural': 'devices',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=100, help_text='A short, human-readable title for the pipeline.')),
                ('pipeline_id', models.CharField(blank=True, unique=True, verbose_name='pipeline ID', max_length=100, editable=False, help_text="The ID of the pipeline as specified in the substation's pipeline configuration file. This is used to reference the pipeline throughout Mercury2.")),
                ('description', models.TextField(blank=True, verbose_name='description', help_text='A brief description of the pipeline explaining its capabilities and usage.')),
                ('state', jsonfield.fields.JSONField(blank=True, editable=False, help_text="A JSON object containing the pipeline's most recent state as reported by the substation.")),
                ('devices', models.ManyToManyField(to='substations.Device')),
            ],
            options={
                'verbose_name': 'pipeline',
                'verbose_name_plural': 'pipelines',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Substation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=100, help_text='A human-readable title for the substation.')),
                ('slug', models.SlugField(unique=True, verbose_name='URL slug', max_length=100, help_text='A URL friendly slug that will be used to reference the substation.')),
                ('longitude', models.DecimalField(blank=True, max_digits=6, verbose_name='longitude', decimal_places=3, editable=False, help_text='The east/west longitude of the substation.')),
                ('latitude', models.DecimalField(blank=True, max_digits=5, verbose_name='latitude', decimal_places=3, editable=False, help_text='The latitude of the substation.')),
                ('altitude', models.IntegerField(blank=True, help_text='The altitude (above sea level) of the substation in meters.', editable=False, verbose_name='altitude')),
                ('public_address', models.CharField(blank=True, help_text='A publicly accessible domain or IP address that routes to the substation', editable=False, max_length=100, verbose_name='public address')),
                ('data_port', models.IntegerField(blank=True, help_text="The port used to access substation pipeline data streams. Must be reachable from the substation's public address.", editable=False, verbose_name='data port')),
                ('telemetry_port', models.IntegerField(blank=True, help_text="The port used to access substation pipeline telemetry streams. Must be reachable from the substation's public address.", editable=False, verbose_name='telemetry port')),
                ('command_port', models.IntegerField(blank=True, help_text="The port used to submit commands to the substation. Must be reachable from the substation's public address.", editable=False, verbose_name='command port')),
                ('state', jsonfield.fields.JSONField(blank=True, editable=False, help_text="A JSON object containing the substation's most recent state as reported by the substation.")),
                ('configuration', jsonfield.fields.JSONField(blank=True, editable=False, help_text="Contains the substation's configuration settings as defined in its configuration.yml file.")),
            ],
            options={
                'verbose_name': 'substation',
                'verbose_name_plural': 'substations',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pipeline',
            name='substation',
            field=models.ForeignKey(to='substations.Substation', help_text='The substation that contains the pipeline.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='device',
            name='substation',
            field=models.ForeignKey(to='substations.Substation', help_text='The substation that the device belongs to.'),
            preserve_default=True,
        ),
    ]
