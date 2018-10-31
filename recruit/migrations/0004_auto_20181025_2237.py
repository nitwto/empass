# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-25 17:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import recruit.models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0003_auto_20180906_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='researchpaper',
            field=models.FileField(blank=True, null=True, upload_to=recruit.models.get_path, validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AddField(
            model_name='paper',
            name='teachpaper',
            field=models.FileField(blank=True, null=True, upload_to=recruit.models.get_path, validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]