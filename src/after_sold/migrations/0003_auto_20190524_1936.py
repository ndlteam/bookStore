# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-24 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('after_sold', '0002_auto_20190524_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
    ]