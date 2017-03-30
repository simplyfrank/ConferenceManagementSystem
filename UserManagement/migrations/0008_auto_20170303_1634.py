# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0007_auto_20170303_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='twitter',
        ),
        migrations.AddField(
            model_name='profile',
            name='blog',
            field=models.URLField(blank=True, default='Your Professional Website/Blog', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, default='Your Facebook Account', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True, default='Your LinkedIn Account', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(blank=True, default='Your Phone Number', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.URLField(blank=True, default='Your Twitter Account', null=True),
        ),
    ]