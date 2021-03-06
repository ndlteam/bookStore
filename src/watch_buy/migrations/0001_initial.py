# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-24 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qty', models.IntegerField(default=1, verbose_name='数量')),
            ],
            options={
                'verbose_name': '购物车信息',
                'verbose_name_plural': '购物车信息',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('GoodISBN', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ISBN')),
                ('GoodName', models.CharField(max_length=255, unique=True, verbose_name='书籍名称')),
                ('GoodPrice', models.FloatField(verbose_name='单价')),
                ('GoodAuthor', models.CharField(max_length=255, null=True, verbose_name='作者')),
                ('GoodIntro', models.TextField(null=True, verbose_name='商品介绍')),
                ('GoodRemain', models.IntegerField(default=0, verbose_name='库存')),
                ('GoodDiscount', models.FloatField(default=1.0, verbose_name='折扣')),
                ('IsForSale', models.IntegerField(default=0, verbose_name='是否打折')),
                ('IsNew', models.IntegerField(default=0, verbose_name='是否新品')),
                ('Intro_pic', models.ImageField(null=True, upload_to='', verbose_name='介绍图片')),
                ('Category', models.CharField(max_length=20, null=True, verbose_name='分类')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
            },
        ),
        migrations.CreateModel(
            name='GoodsPic',
            fields=[
                ('PicId', models.AutoField(primary_key=True, serialize=False, verbose_name='图片ID')),
                ('GoodPic', models.ImageField(upload_to='', verbose_name='文件名')),
                ('GoodISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch_buy.Goods', verbose_name='图书信息')),
            ],
            options={
                'verbose_name': '商品图像',
                'verbose_name_plural': '商品图像',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderid', models.AutoField(primary_key=True, serialize=False, verbose_name='订单号')),
                ('orderdate', models.DateTimeField(verbose_name='下单时间')),
                ('shipdate', models.DateTimeField(blank=True, null=True, verbose_name='发货时间')),
                ('address', models.CharField(max_length=255, verbose_name='收货人地址')),
                ('IsShipped', models.IntegerField(default=0, verbose_name='是否发货')),
                ('IsCancle', models.IntegerField(default=0, verbose_name='是否申请退货中')),
                ('IsHandled', models.IntegerField(default=0, verbose_name='是否确认订单')),
                ('IsCancled', models.IntegerField(default=0, verbose_name='是否取消')),
                ('username', models.CharField(max_length=20, verbose_name='收货人姓名')),
                ('telephone', models.CharField(max_length=25, verbose_name='收货人电话')),
                ('zipcode', models.CharField(max_length=25, verbose_name='收货人邮编')),
                ('qq', models.CharField(max_length=15, verbose_name='收货人QQ')),
                ('IsCompleted', models.IntegerField(default=0, verbose_name='订单是否完成')),
                ('Comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='用户评论')),
                ('IsReturn', models.IntegerField(default=0, verbose_name='是否要求退货')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_manage.User', verbose_name='下单用户')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
            },
        ),
        migrations.CreateModel(
            name='OrderGood',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='订单号')),
                ('count', models.IntegerField(default=1, verbose_name='数量')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch_buy.Goods', verbose_name='商品信息')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch_buy.Order', verbose_name='订单信息')),
            ],
            options={
                'verbose_name': '订单图书',
                'verbose_name_plural': '订单图书',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='GoodID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch_buy.Goods', verbose_name='商品信息'),
        ),
        migrations.AddField(
            model_name='cart',
            name='studentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_manage.User', verbose_name='学号'),
        ),
    ]
