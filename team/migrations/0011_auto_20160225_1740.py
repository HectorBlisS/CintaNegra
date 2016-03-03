# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-25 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_auto_20160225_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsable',
            name='team',
        ),
        migrations.AddField(
            model_name='responsable',
            name='grade',
            field=models.CharField(choices=[('5 Primaria', '5 Primaria'), ('6 Primaria', '6 Primaria'), ('1 Secundaria', '1 Secundaria'), ('2 Secundaria', '2 Secundaria'), ('3 Secundaria', '3 Secundaria')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='responsable',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Responsable'),
            preserve_default=False,
        ),
    ]