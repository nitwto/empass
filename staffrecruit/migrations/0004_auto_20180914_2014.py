# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-14 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import staffrecruit.models


class Migration(migrations.Migration):

    dependencies = [
        ('staffrecruit', '0003_auto_20180914_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proof',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('prooffile', models.FileField(null=True, upload_to=staffrecruit.models.get_proof_path)),
            ],
        ),
        migrations.AddField(
            model_name='staffuser',
            name='proof',
            field=models.ManyToManyField(to='staffrecruit.Proof'),
        ),
    ]
