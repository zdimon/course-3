# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class News(models.Model):
	title=models.CharField(max_length=250)
	content=models.TextField()
	url=models.CharField(max_length=250)