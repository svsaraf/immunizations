# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_immunization_recommended_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='immunization',
            name='catchup_age',
            field=models.DecimalField(default=12, max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
