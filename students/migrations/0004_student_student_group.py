# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(null=True, to='students.Group', on_delete=django.db.models.deletion.PROTECT, verbose_name='Група'),
        ),
    ]
