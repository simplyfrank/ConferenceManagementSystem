# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationManagement', '0017_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(),
        ),
    ]