# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20150204_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='patientid',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
