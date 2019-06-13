# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-13 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_buy', '0005_auto_20190531_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='Edition',
            field=models.IntegerField(blank=True, null=True, verbose_name='版本'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='GoodName',
            field=models.CharField(max_length=255, verbose_name='书籍名称'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='Pages',
            field=models.IntegerField(blank=True, null=True, verbose_name='页数'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='PrintDate',
            field=models.DateField(blank=True, null=True, verbose_name='印刷日期'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='PublishDate',
            field=models.DateField(blank=True, null=True, verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='Publisher',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='Size',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='开本'),
        ),
        migrations.AlterField(
            model_name='order',
            name='IsReturn',
            field=models.IntegerField(default=0, verbose_name='是否要求退款'),
        ),
    ]