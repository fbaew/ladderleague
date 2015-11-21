# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('handle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('set_count', models.IntegerField()),
                ('player1', models.ForeignKey(related_name='player1', to='scores.Player')),
                ('player2', models.ForeignKey(related_name='player2', to='scores.Player')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='parent_set',
            field=models.ForeignKey(null=True, to='scores.Set'),
        ),
    ]
