# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-13 07:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import staffregistration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('postID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicationID', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=14)),
                ('postApplied', models.CharField(max_length=100)),
                ('termsRead', models.BooleanField(default=False)),
                ('profilePic', models.ImageField(blank=True, null=True, upload_to=staffregistration.models.get_profilepic_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
