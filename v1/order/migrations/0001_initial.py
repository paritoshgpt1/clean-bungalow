# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=50, null=True, verbose_name=b'Order Code', blank=True)),
                ('start_time', models.DateTimeField(null=True, verbose_name=b'Start Time', blank=True)),
                ('stop_time', models.DateTimeField(null=True, verbose_name=b'Stop Time', blank=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderAddress',
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
                'verbose_name': 'Order Address',
                'verbose_name_plural': 'Order Addresses',
            },
        ),
        migrations.CreateModel(
            name='OrderCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=30, null=True, verbose_name=b'Category Name', blank=True)),
            ],
            options={
                'verbose_name': 'Order Category',
                'verbose_name_plural': 'Order Categories',
            },
        ),
        migrations.CreateModel(
            name='OrderCustomer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name=b'First Name', blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name=b'Last Name', blank=True)),
                ('username', models.CharField(max_length=50, null=True, verbose_name=b'Username', blank=True)),
                ('password', models.CharField(max_length=50, null=True, verbose_name=b'Password', blank=True)),
                ('email', models.EmailField(max_length=50, unique=True, null=True, verbose_name=b'Email')),
                ('mobile', models.PositiveIntegerField(null=True, verbose_name=b'Mobile No', blank=True)),
                ('billing_address', models.ForeignKey(related_name='billing_customer', verbose_name=b'Billing Address', blank=True, to='order.OrderAddress', null=True)),
                ('shipping_address', models.ForeignKey(related_name='shipping_customer', verbose_name=b'Shipping Address', blank=True, to='order.OrderAddress', null=True)),
            ],
            options={
                'verbose_name': 'Order Customer',
                'verbose_name_plural': 'Order Customers',
            },
        ),
        migrations.CreateModel(
            name='OrderService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(max_length=50, null=True, verbose_name=b'Service Name', blank=True)),
                ('category', models.ForeignKey(verbose_name=b'Category', blank=True, to='order.OrderCategory', null=True)),
            ],
            options={
                'verbose_name': 'Order Service',
                'verbose_name_plural': 'Order Services',
            },
        ),
        migrations.CreateModel(
            name='OrderWorker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name=b'First Name', blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name=b'Last Name', blank=True)),
                ('mobile', models.PositiveIntegerField(null=True, verbose_name=b'Mobile No', blank=True)),
                ('start_time', models.DateTimeField(null=True, verbose_name=b'Start Time', blank=True)),
                ('end_time', models.DateTimeField(null=True, verbose_name=b'End Time', blank=True)),
                ('service', models.ManyToManyField(to='order.OrderService', verbose_name=b'Services', blank=True)),
            ],
            options={
                'verbose_name': 'Order Worker',
                'verbose_name_plural': 'Order Workers',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(verbose_name=b'Order Customer', blank=True, to='order.OrderCustomer', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ForeignKey(verbose_name=b'Order Service', blank=True, to='order.OrderService', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='worker',
            field=models.ForeignKey(verbose_name=b'Order Worker', blank=True, to='order.OrderWorker', null=True),
        ),
    ]
