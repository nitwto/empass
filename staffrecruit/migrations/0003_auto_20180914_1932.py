# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-14 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffrecruit', '0002_auto_20180914_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffuser',
            name='obccreamy',
            field=models.CharField(max_length=255),
        ),
    ]
