# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import News, Category

# Create your views here.

def home(request):
	category = Category.objects.all()
	news = News.objects.filter(category__name = 'Main')

	ctx = {'news':news, 'category':category}
	return render(request, 'index.html', ctx)


def detail(request, id):
	news = News.objects.get(id = id)
	category = Category.objects.all()
	return render(request, 'detail.html', {'news':news, 'category':category})

def subsection(request, name):
	category = Category.objects.all()	
	news = News.objects.filter(category__name = name)
	return render(request, 'subsection.html', {'news':news, 'category':category })



