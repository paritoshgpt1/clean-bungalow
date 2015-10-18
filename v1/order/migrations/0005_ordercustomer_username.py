# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20151016_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercustomer',
            name='username',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Username', blank=True),
        ),
    ]
