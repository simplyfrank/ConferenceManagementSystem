# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0023_auto_20170314_1139'),
        ('SessionManagement', '0004_session_assessors'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='mediatorTeam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mediatorteam', to='UserManagement.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='negotiatorTeam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='negotiatorteam', to='UserManagement.Team'),
            preserve_default=False,
        ),
    ]
