# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=250)

class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.name

class News(models.Model):
    tags = models.ManyToManyField(Tags)
    category = models.ForeignKey(Category, verbose_name=u'Базовая категория', null=True, blank=True)
    item_title = models.CharField(max_length=250)
    item_link = models.CharField(max_length=250)
    item_short_descr = models.TextField()
    
    photo = models.ImageField(upload_to='catalog_pic/', null=True, blank=True, verbose_name='Фото')


    is_pub = models.BooleanField(verbose_name='Опубликовать?', default=False)
    
    pressa_share = models.PositiveIntegerField(verbose_name='доля', default=40)
    
    def __unicode__(self):
        return '%s %s' % (self.id,self.item_title)
        
        
        
class NewsForm(ModelForm):
    class Meta:
        model = News
        #fields = ['item_title', 'item_short_descr']
        exclude = []

        
        
