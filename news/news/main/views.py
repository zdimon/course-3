# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import News, NewsForm

# Create your views here.

def home(request):
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        n = News()
        n.item_title = request.POST.get('title', 'default')
        n.save()
        #print 
    news = News.objects.all()
    form = NewsForm(instance=news[0])
    ctx = { 'name': 'Dima', 'news': news, 'form': form }
    return render(request, 'index.html', ctx)
    
    
def detail(request,id):
    news = News.objects.get(id=id)
    return render(request, 'detail.html', {'news': news})
