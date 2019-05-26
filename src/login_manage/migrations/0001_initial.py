# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-24 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('studentID', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='学号')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='姓名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('email', models.EmailField(max_length=255, verbose_name='邮箱地址')),
                ('city', models.CharField(max_length=20, null=True, verbose_name='城市')),
                ('city_num', models.IntegerField(null=True, verbose_name='城市编号')),
                ('detail_address', models.CharField(max_length=255, null=True, verbose_name='详细地址')),
                ('zip_code', models.CharField(max_length=20, null=True, verbose_name='邮编')),
                ('telephone', models.CharField(max_length=20, null=True, verbose_name='电话')),
                ('qq', models.CharField(max_length=20, null=True, verbose_name='QQ号')),
                ('money', models.FloatField(null=True, verbose_name='账户余额')),
                ('is_banned', models.IntegerField(default=0, verbose_name='账户状态')),
            ],
            options={
                'verbose_name': '普通用户',
                'verbose_name_plural': '普通用户',
            },
        ),
    ]
