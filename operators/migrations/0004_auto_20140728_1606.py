# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0003_auto_20140728_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationuser',
            name='city',
            field=models.CharField(verbose_name='city', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='stationuser',
            name='country',
            field=models.CharField(verbose_name='country', blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='stationuser',
            name='organization',
            field=models.CharField(verbose_name='organization', blank=True, max_length=100, help_text="The organization that you're associated with."),
        ),
        migrations.AlterField(
            model_name='stationuser',
            name='region',
            field=models.CharField(verbose_name='region', blank=True, max_length=50, help_text='The region or state that you live in.'),
        ),
    ]
