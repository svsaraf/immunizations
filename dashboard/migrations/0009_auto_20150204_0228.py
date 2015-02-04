# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20150204_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immunization',
            name='immunizationid',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=True,
        ),
    ]
