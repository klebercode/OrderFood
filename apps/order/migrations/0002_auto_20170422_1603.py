# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 16:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at'], 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
    ]