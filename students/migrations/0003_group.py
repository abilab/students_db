# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20150923_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=256, verbose_name='Назва')),
                ('notes', models.TextField(verbose_name='Додаткові нотатки', blank=True)),
                ('leader', models.OneToOneField(on_delete=django.db.models.deletion.SET_NULL, to='students.Student', null=True, verbose_name='Староста', blank=True)),
            ],
            options={
                'verbose_name': 'Група',
                'verbose_name_plural': 'Групи',
            },
        ),
    ]
