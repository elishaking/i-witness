# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
