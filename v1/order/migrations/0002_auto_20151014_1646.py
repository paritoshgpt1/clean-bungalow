# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercustomer',
            name='username',
        ),
        migrations.AddField(
            model_name='ordercustomer',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'Is Active'),
        ),
        migrations.AddField(
            model_name='ordercustomer',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ordercustomer',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name=b'Is Super user'),
        ),
        migrations.AddField(
            model_name='ordercustomer',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
        migrations.AlterField(
            model_name='ordercustomer',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
