# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-28 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_auto_20180928_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charge',
            name='active',
        ),
        migrations.RemoveField(
            model_name='charge',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='card',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='card',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
