# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 21:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tribbles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribble',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
