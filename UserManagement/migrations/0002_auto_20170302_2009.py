# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 19:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationManagement', '0001_initial'),
        ('SessionManagement', '0002_auto_20170302_2009'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expert',
            name='attendent_ptr',
        ),
        migrations.RemoveField(
            model_name='expert',
            name='team',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='attendent_ptr',
        ),
        migrations.RemoveField(
            model_name='student',
            name='attendent_ptr',
        ),
        migrations.RemoveField(
            model_name='student',
            name='team',
        ),
        migrations.RemoveField(
            model_name='expertprofile',
            name='expert',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='student',
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='expertRole',
            field=models.CharField(blank=True, choices=[('expert', 'Expert Assessor'), ('coach', 'Coach'), ('assessor', 'Assessor')], max_length=20),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coachedTeam', to='UserManagement.Team'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='studentRole',
            field=models.CharField(blank=True, choices=[('negotiator', 'Negotiator'), ('mediator', 'Mediator')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserManagement.Team'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='teamprofile',
            name='languages_spoken',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='teamprofile',
            name='presentation_text',
            field=models.TextField(blank=True, max_length=4000),
        ),
        migrations.AlterField(
            model_name='teamprofile',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UserManagement.Team'),
        ),
        migrations.DeleteModel(
            name='Expert',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]