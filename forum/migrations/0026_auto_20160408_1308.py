# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-08 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0025_auto_20160408_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='thread',
            name='text',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
