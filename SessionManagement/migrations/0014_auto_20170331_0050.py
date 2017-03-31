# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SessionManagement', '0013_session_venue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='Room',
            new_name='room',
        ),
        migrations.AddField(
            model_name='availability',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]