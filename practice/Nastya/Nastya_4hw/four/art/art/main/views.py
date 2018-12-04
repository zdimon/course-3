# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Art,Category
# Create your views here.
def home(request):
    art=Art.objects.all()
    category=Category.objects.all()
    ctx={'name':'Nastya','art':art,'category':category}
    #return render(request,'base.html',ctx)
    return render(request,'index.html',ctx)

def detail(request,id):
    category=Category.objects.all()
    cat=Category.objects.get(id=id)
    art=Art.objects.filter(category=cat)
    return render(request,'detail.html',{'art':art,'category':category})
