# Generated by Django 3.0.5 on 2020-04-22 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('solution_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scavenger_hunt.Solution')),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('scavenger_hunt.solution',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scavenger_hunt.Problem')),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('scavenger_hunt.problem',),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scavenger_hunt.Game')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scavenger_hunt.Player')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(to='scavenger_hunt.Player'),
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('index', models.IntegerField(default=1)),
                ('game', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenges', to='scavenger_hunt.Game')),
                ('problem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scavenger_hunt.Problem')),
                ('solution', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scavenger_hunt.Solution')),
            ],
            options={
                'ordering': ['index', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('verified', models.DateTimeField(blank=True, default=None, null=True)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scavenger_hunt.Challenge')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scavenger_hunt.Player')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
