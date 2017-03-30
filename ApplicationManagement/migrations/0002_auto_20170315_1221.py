# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='term_accepted',
            field=models.BooleanField(default=False, verbose_name='Accept Legal Terms'),
        ),
        migrations.AlterField(
            model_name='application',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.IntegerField(choices=[(0, 'Unreviewed'), (1, 'Reviewed'), (2, 'Selected'), (3, 'Accepted'), (4, 'Declined')], default=0),
        ),
    ]
