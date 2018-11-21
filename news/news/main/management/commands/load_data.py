from django.core.management.base import BaseCommand, CommandError
from main.models import News


class Command(BaseCommand):
    def add_arguments(self, parser):
        
        # Named (optional) arguments
        parser.add_argument(
            '--url',
            dest='url',
            help='Url address',
        )

    def handle(self, *args, **options):
        # ...
        
        print 'Start'
        #News.objects.delete()
        for r in News.objects.filter(pk__gt=10):
            print r.delete()
        '''
        return True
        for i in range(1,50):
            record = News()
            record.title = 'Title %s' % i
            record.save() 
            print 'Saving %s' % i
        
        
        if options['url']:
            print 'Loadd from %s' % options['url']
        # ...
        print 'End'
        '''
