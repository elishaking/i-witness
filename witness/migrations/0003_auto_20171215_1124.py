# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 10:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('witness', '0002_auto_20171215_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='witness',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
