# Food catalog

    pip install django-mptt
    
    
    
    INSTALLED_APPS += ['mptt']
    
    
## Model


    from django.db import models

    from mptt.models import MPTTModel, TreeForeignKey

    class Catalog(MPTTModel):
        name = models.CharField(max_length=100, unique=True)
        parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

        class MPTTMeta:
            order_insertion_by = ['name']
                
            
## Admin page


    from mptt.admin import MPTTModelAdmin
    from catalog.models import Catalog

    class CatalogAdmin(MPTTModelAdmin):
        # specify pixel amount for this ModelAdmin only:
        mptt_level_indent = 20

    admin.site.register(Catalog, CatalogAdmin)



## Load test data


    from django.core.management.base import BaseCommand
    from django.utils import timezone
    from django.conf import settings
    from catalog.models import Catalog

    class Command(BaseCommand):

        def handle(self, *args, **kwargs):
            Catalog.objects.all().delete()
            print('Создаем каталог')

            root = Catalog.objects.create(name='Каталог', parent=None)

            juice = Catalog.objects.create(name='Соки', parent=root)

            tee = Catalog.objects.create(name='Чай', parent=root)

            coffee = Catalog()
            coffee.parent = root
            coffee.name = 'Кофе'
            coffee.save()

            print('Done')
        
## Product model

    class Product(models.Model):
        name = models.CharField(max_length=200)
        catalog = models.ManyToManyField(Catalog)
        def __str__(self):
            return self.name
        
        


        
  
        
