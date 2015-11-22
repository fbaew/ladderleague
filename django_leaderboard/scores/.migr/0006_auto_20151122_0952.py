# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0005_auto_20151122_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='set_id',
            field=models.IntegerField(serialize=False, default=0, primary_key=True),
        ),
    ]
