# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 01:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_auto_20170426_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='name',
            new_name='title',
        ),
    ]