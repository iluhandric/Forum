# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-26 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20160325_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='topic',
            name='logo',
            field=models.CharField(blank=True, default='no_logo.jpg', max_length=100),
            preserve_default=False,
        ),
    ]
