# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-16 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castvote', '0004_storevote_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='storevote',
            name='hascounted',
            field=models.BooleanField(default=False),
        ),
    ]
