# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-23 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_buy', '0008_order_iscompleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='Category',
            field=models.CharField(max_length=20, null=True),
        ),
    ]