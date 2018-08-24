# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-02 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20180802_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='级别')),
            ],
            options={
                'verbose_name_plural': '级别',
                'db_table': 'Level',
            },
        ),
        migrations.AlterField(
            model_name='video',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Level'),
        ),
    ]
