# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='immunization',
            name='recommended_age',
            field=models.DecimalField(default=1, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]
