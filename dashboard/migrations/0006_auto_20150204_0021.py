# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_patient_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patientid',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
    ]
