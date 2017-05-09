# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0003_flatprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatprofile',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]