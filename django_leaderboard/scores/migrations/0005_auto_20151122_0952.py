# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0004_auto_20151122_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='id',
        ),
        migrations.AddField(
            model_name='set',
            name='set_id',
            field=models.IntegerField(serialize=False, primary_key=True, default=0),
        ),
    ]
