# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20151014_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercustomer',
            name='email',
            field=models.EmailField(max_length=50, unique=True, null=True, verbose_name=b'Email', blank=True),
        ),
    ]
