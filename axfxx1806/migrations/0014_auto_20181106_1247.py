# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-06 04:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axfxx1806', '0013_myuser_icon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MineBtns',
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': '我的页面的下一排按钮'},
        ),
        migrations.AlterIndexTogether(
            name='cart',
            index_together=set([]),
        ),
    ]
