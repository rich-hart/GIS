# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribbles', '0002_auto_20170717_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribble',
            name='key',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
