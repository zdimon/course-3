from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        
        # Named (optional) arguments
        parser.add_argument(
            '--url',
            dest='url',
            help='Load news',
        )

    def handle(self, *args, **options):
        # ...
        print 'Start'
        if options['url']:
            print 'From url %s' % options['url']
        # ...
        print 'Stop'
