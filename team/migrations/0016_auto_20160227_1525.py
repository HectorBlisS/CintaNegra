# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0015_team_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Responsable',
            new_name='Leader',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='responsable',
            new_name='leader',
        ),
    ]
