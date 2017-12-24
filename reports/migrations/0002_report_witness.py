# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-24 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('witness', '0006_remove_witness_reports'),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='witness',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='witness.Witness'),
            preserve_default=False,
        ),
    ]
