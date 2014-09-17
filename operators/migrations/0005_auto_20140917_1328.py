# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0004_auto_20140728_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationuser',
            name='groups',
            field=models.ManyToManyField(verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, related_query_name='user', related_name='user_set', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='stationuser',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, related_query_name='user', related_name='user_set', to='auth.Permission'),
        ),
    ]
