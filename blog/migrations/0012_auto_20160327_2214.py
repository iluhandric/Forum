# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-27 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_topic_colnum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='thread',
            name='comments',
            field=models.ManyToManyField(blank=True, to='blog.Comment'),
        ),
    ]
