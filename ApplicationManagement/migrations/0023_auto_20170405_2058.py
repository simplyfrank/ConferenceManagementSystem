# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationManagement', '0022_auto_20170405_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='application_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='review_completed',
            field=models.BooleanField(default=False, verbose_name='Application review complete'),
        ),
    ]
