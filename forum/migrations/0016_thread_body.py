# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-04 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0015_thread_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
