# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-24 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181124_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_pub',
            field=models.BooleanField(default=False, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c?'),
        ),
        migrations.AddField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='catalog_pic/', verbose_name='\u0424\u043e\u0442\u043e'),
        ),
        migrations.AddField(
            model_name='news',
            name='pressa_share',
            field=models.PositiveIntegerField(default=40, verbose_name='\u0434\u043e\u043b\u044f'),
        ),
    ]
