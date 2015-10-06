# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line_one', models.CharField(max_length=100, null=True, verbose_name=b'Address Line 1', blank=True)),
                ('line_two', models.CharField(max_length=100, null=True, verbose_name=b'Address Line 2', blank=True)),
                ('city', models.CharField(max_length=30, null=True, verbose_name=b'City', blank=True)),
                ('state', models.CharField(max_length=30, null=True, verbose_name=b'State', blank=True)),
                ('landmark', models.CharField(max_length=100, null=True, verbose_name=b'Landmark', blank=True)),
                ('locality', models.CharField(max_length=50, null=True, verbose_name=b'Locality', blank=True)),
                ('pincode', models.PositiveIntegerField(null=True, verbose_name=b'Pin Code', blank=True)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name=b'First Name', blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name=b'Last Name', blank=True)),
                ('username', models.CharField(max_length=50, null=True, verbose_name=b'Username', blank=True)),
                ('password', models.CharField(max_length=50, null=True, verbose_name=b'Password', blank=True)),
                ('email', models.EmailField(max_length=50, unique=True, null=True, verbose_name=b'Email')),
                ('mobile', models.PositiveIntegerField(null=True, verbose_name=b'Mobile No', blank=True)),
                ('billing_address', models.ForeignKey(related_name='billing_customer', verbose_name=b'Billing Address', blank=True, to='customer.Address', null=True)),
                ('shipping_address', models.ForeignKey(related_name='shipping_customer', verbose_name=b'Shipping Address', blank=True, to='customer.Address', null=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(verbose_name=b'Customer', blank=True, to='customer.Customer', null=True),
        ),
    ]
