# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-21 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_buy', '0004_auto_20190521_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
    ]