# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_immunization_catchup_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.DecimalField(default=1, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]
