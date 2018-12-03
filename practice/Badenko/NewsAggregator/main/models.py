# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Domain(models.Model):
    url = models.URLField(unique=True)

class Article(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    creationDate = models.DateField(auto_now_add=True)
    htmlSource = models.FileField(null=True, upload_to='Articles/')    
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, to_field='url')

   

    def getAll(self):
        return Article.objects.all().order_by('-creationDate')
