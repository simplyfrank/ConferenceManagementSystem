# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 20:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0026_auto_20170315_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='team',
        ),
    ]
