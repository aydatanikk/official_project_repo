# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='profile_image'),
        ),
    ]
