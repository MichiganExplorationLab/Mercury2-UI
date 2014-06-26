# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationuser',
            name='city',
            field=models.CharField(verbose_name='City', blank=True, help_text='Your city of residence.', max_length=100),
        ),
        migrations.AlterField(
            model_name='stationuser',
            name='country',
            field=models.CharField(verbose_name='Country', blank=True, max_length=2),
        ),
    ]
