from django.core.management.base import BaseCommand, CommandError
from main.models import News


class Command(BaseCommand):
    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            '--url',
            dest ='url',
            help ='Parsing site items, links and descriptions',
        )

    def handle(self, *args, **options):
        # ...
        print 'Start'
        import requests
        from bs4 import BeautifulSoup

        url = 'https://pythondigest.ru/'
        r = requests.get( url )
        encoded_page = r.text.encode( 'utf-8' )

        soup = BeautifulSoup(encoded_page, 'html.parser' )
        divs = soup.find_all( "div", {"class": "issue-item"} )

        text_list = list()
        href_list = list()
        descr_list = list()

        for div in divs:
            for a in div.find_all('a', {"class": "issue-item-title"}):
                text_list.append(a.get_text())
                href_list.append(a['href'])
                if a.next_sibling.next_sibling is not None:
                    element = a.next_sibling.next_sibling.get_text()
                    descr_list.append(element.encode('utf-8'))
                else:
                    descr_list.append('')
        full_list = zip(text_list,href_list,descr_list)
        News.objects.all().delete()
        counter = 0
        for i in full_list:
            item = News(item_title=i[0], item_link=i[1], item_short_descr=i[2])
            item.save()
            counter +=1
            print 'Saving %s' %counter
            
        print 'End'
            
        
        # ...
