from django.core.management.base import BaseCommand, CommandError
from main.models import News

import requests
import unicodecsv as csv
from bs4 import BeautifulSoup

url='https://pythondigest.ru/'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--url',dest='url',help='Url address',)
		
    def handle(self, *args, **options):	
        for div in soup.find_all('div',class_='issue-item'):
            a=div.find('a',class_='issue-item-title')
            links=a.get('href')
            title=a.string		
            for p in div.findChildren('p'):
                if p.text != '':
                    content=p.text
                    break
                else:
                    content='"Empty content"'
            record=News()
            record.title=title
            record.content=content
            record.url=links
            record.save()
            print('Saving data... %s' % content)
		
            if options['url']:
                print('Load from %s' % options['url'])