# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('finalized', 'Finalized'), ('rejected', 'Rejected'), ('cancelled_by_user', 'Cancelled by user')], default='new', max_length=100),
        ),
    ]