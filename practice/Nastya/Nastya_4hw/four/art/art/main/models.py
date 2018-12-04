# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length = 250,blank=True)


    def __unicode__(self):
        return  self.name

class Category(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)

    def __unicode__(self):
        return self.name
    
class Art(models.Model):
    tags=models.ManyToManyField(Tag)
    category=models.ForeignKey(Category, verbose_name=u'Базовая категория', null=True, blank=True)
    title=models.CharField(max_length=250)
    link=models.CharField(max_length=250)
    content=models.TextField(null=True,blank=True)
    photo = models.ImageField(upload_to='catalog_pic/', null=True, blank=True, verbose_name='Photo')
    
    def __unicode__(self):
        return self.title

