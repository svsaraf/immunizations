# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20150204_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
