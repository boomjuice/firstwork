# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-01 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_job'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': '招聘信息'},
        ),
        migrations.AlterModelTable(
            name='job',
            table='JobFound',
        ),
    ]
