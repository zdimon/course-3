# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import *
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('item_title', 'item_short_descr')
    list_filter = ('item_title',)
    search_fields = ('item_title',)


admin.site.register(News, NewsAdmin)


