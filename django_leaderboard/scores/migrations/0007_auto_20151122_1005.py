# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0006_auto_20151122_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='set',
            old_name='set_id',
            new_name='setid',
        ),
    ]
