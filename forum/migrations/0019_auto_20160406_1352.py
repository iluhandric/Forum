# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-06 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_auto_20160405_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]
