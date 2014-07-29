# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0002_auto_20140625_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationuser',
            name='city',
            field=models.CharField(max_length=100, verbose_name='City', blank=True),
        ),
        migrations.AlterField(
            model_name='stationuser',
            name='organization',
            field=models.CharField(help_text="The organization that you're associated with.", max_length=100, verbose_name='Organization', blank=True),
        ),
    ]
