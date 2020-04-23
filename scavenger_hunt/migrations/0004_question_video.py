# Generated by Django 3.0.5 on 2020-04-23 00:09

from django.db import migrations, models
import gis.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('scavenger_hunt', '0003_award_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='video',
            field=models.FileField(blank=True, default=None, null=True, storage=gis.storage_backends.MediaStorage(), upload_to=''),
        ),
    ]
