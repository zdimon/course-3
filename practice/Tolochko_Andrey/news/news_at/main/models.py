# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.name

class News(models.Model):
    category = models.ForeignKey(Category, verbose_name= u'Базовая категория',
                                 null=True, blank=True)
    item_title = models.CharField(max_length=250)
    item_link = models.CharField(max_length=250)
    item_short_descr = models.TextField()
    link_photo = models.CharField(max_length = 350, null=True, blank=True)
    article = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return "{0}, {1}, {2}".format(self.item_title, self.item_short_descr, self.article)
