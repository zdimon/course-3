# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import *
# Register your models here.
class TagAdmin(admin.ModelAdmin):
    pass
   
admin.site.register(Tag,TagAdmin)
    
class CategoryAdmin(admin.ModelAdmin):
    #pass
    list_display=('name',)
    #list_filter=('category',)
    #search_fields=('title',)
   
admin.site.register(Category,CategoryAdmin)


class ArtAdmin(admin.ModelAdmin):
    #pass
    list_display=('title','content')
    list_filter=('category',)
    #search_fields=('title',)
   
admin.site.register(Art,ArtAdmin)
