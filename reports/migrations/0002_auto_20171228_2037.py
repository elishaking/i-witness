# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='witness',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='witness.Witness'),
        ),
    ]