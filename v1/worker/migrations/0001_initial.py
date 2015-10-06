# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name=b'First Name', blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name=b'Last Name', blank=True)),
                ('mobile', models.PositiveIntegerField(null=True, verbose_name=b'Mobile No', blank=True)),
                ('start_time', models.DateTimeField(null=True, verbose_name=b'Start Time', blank=True)),
                ('end_time', models.DateTimeField(null=True, verbose_name=b'End Time', blank=True)),
                ('service', models.ManyToManyField(to='service.Service', verbose_name=b'Services', blank=True)),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Workers',
            },
        ),
    ]
