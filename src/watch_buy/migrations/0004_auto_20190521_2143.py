# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-21 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_buy', '0003_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '订单信息', 'verbose_name_plural': '订单信息'},
        ),
        migrations.AlterField(
            model_name='order',
            name='shipdate',
            field=models.DateTimeField(null=True),
        ),
    ]