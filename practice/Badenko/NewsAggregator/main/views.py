# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    data = {'title': 'Landing Page',}
    return render(request, 'index.html', context = data)

def data(request):
    a = Article()       
    data = {'title': 'Data','list': a.getAll()}
    return render(request, 'data.html', context = data)

def contact(request):
    data = {'title': 'Contact Information',}
    return render(request, 'contact.html', context = data)

