from django.contrib import admin
from main.models import Poem, Category
# Register your models here.


class PoemAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'date')
    list_filter = ('author', 'category')
    search_fields = ('author', 'date')


admin.site.register(Poem, PoemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
