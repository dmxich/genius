# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0017_merge_20170426_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
