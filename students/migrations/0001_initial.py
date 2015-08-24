# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=256, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=256, verbose_name='Прізвище')),
                ('middle_name', models.CharField(max_length=256, blank=True, verbose_name='По-батькові', default='')),
                ('birthday', models.DateField(null=True, verbose_name='Дата народження')),
                ('photo', models.ImageField(upload_to='', null=True, blank=True, verbose_name='Фото')),
                ('ticket', models.CharField(max_length=256, verbose_name='Білет')),
                ('notes', models.TextField(blank=True, verbose_name='Додаткові нотатки')),
            ],
        ),
    ]
