# Generated by Django 3.0.5 on 2020-04-22 08:48

from django.db import migrations, models
import django.db.models.deletion
import scavenger_hunt.models


class Migration(migrations.Migration):

    dependencies = [
        ('scavenger_hunt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PenaltyTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(choices=[(0, scavenger_hunt.models.PenaltyTag.Type['yellow']), (1, scavenger_hunt.models.PenaltyTag.Type['red']), (2, scavenger_hunt.models.PenaltyTag.Type['general'])], default='general', max_length=127)),
                ('description', models.TextField()),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', related_query_name='tag', to='scavenger_hunt.Penalty')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
