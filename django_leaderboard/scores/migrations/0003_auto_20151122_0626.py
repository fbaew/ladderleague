# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0002_auto_20151121_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='id',
        ),
        migrations.AddField(
            model_name='player',
            name='short_id',
            field=models.CharField(serialize=False, primary_key=True, default='CHUMP', max_length=200),
        ),
    ]
