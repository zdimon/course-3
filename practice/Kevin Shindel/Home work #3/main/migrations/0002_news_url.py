# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-03 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
