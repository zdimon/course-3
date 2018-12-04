from django.core.management.base import BaseCommand, CommandError
from main.models import News, Category


class Command(BaseCommand):
    

    def handle(self, *args, **options):
        # ...
        print 'Start'
        try:
            cat = Category.objects.get(name='Goods')
            n = News()
            n.category = cat
            n.item_title = ' News of %s' % cat.name
            n.save()
            print 'Saving....'
        except:
            pass
       
