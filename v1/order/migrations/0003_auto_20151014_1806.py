# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20151014_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercustomer',
            name='mobile',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Mobile No', blank=True),
        ),
    ]
