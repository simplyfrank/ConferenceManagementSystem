# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0014_internship_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='duration',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competition',
            name='measure',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]