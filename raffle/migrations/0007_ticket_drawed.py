# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raffle', '0006_prize_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='drawed',
            field=models.BooleanField(default=False),
        ),
    ]
