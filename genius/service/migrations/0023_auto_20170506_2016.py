# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 03:16
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0022_auto_20170506_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service.Review')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Restaurant')),
            ],
            bases=('service.review',),
        ),
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]