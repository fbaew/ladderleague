# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0012_auto_20160212_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='hometown',
            field=models.CharField(default='Parts Unknown, Planet Earth', max_length=100),
        ),
    ]
