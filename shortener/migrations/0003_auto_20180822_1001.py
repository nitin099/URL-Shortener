# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-08-22 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_remove_tinyurl_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tinyurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
