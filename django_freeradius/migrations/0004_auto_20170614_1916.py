# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_freeradius', '0003_auto_20170603_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiusgroup',
            name='group_name',
            field=models.CharField(db_column='groupname', db_index=True, max_length=255, unique=True, verbose_name='groupname'),
        ),
    ]