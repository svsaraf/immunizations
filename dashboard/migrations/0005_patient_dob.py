# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_patient_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 4, 0, 18, 14, 815547, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
