# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-05 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axfxx1806', '0009_auto_20181105_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='crteate_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='upload_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
