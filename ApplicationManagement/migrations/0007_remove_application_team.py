# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationManagement', '0006_application_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='team',
        ),
    ]