# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180115_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.CharField(blank=True, default=1, max_length=100000000000000000000),
            preserve_default=False,
        ),
    ]
