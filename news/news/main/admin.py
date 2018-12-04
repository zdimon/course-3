# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import *

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    #pass
    list_display = ('item_title', 'item_short_descr')
    list_filter = ('tags',)
    search_fields = ('item_title',)
admin.site.register(News, NewsAdmin)


class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tags, TagAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass
    #list_display = ('item_title', 'item_short_descr')
    #list_filter = ('item_title',)
    #search_fields = ('item_title',)
admin.site.register(Category, CategoryAdmin)
