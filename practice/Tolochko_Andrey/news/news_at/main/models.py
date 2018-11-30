# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class News(models.Model):
    item_title = models.CharField(max_length=250)
    item_link = models.CharField(max_length=250)
    item_short_descr = models.TextField()
    
