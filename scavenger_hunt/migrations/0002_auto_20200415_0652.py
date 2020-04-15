# Generated by Django 3.0.5 on 2020-04-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scavenger_hunt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='category',
            field=models.CharField(blank=True, choices=[('FE', 'featured')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='other_category',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
