# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_auto_20180112_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='filename',
            field=models.CharField(max_length=200),
        ),
    ]
