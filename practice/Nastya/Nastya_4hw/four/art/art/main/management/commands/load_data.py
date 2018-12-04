from django.core.management.base import BaseCommand, CommandError
from main.models import *
import requests
from bs4 import BeautifulSoup
url='http://art-news.com.ua/'
r=requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
class Command(BaseCommand):
    def handle(self,*argument,**option):
        Category.objects.all().delete()
        Art.objects.all().delete()
        print 'START'
        i=1
        block=soup.find_all('div',{'column half'})
        for l in block:
            record=Art()
            record.title=l.find('h2').find('a').text
            record.link=l.find('h2').find('a').get('href')
            record.content=l.find('div',{'excerpt text-font'}).text
            cat=l.find('span',{'listing-meta'}).find('a').text
            if Category.objects.filter(name = cat).exists():
                category = Category.objects.get(name=cat)
                record.category = category
            else:
                newCat=Category()
                newCat.name=cat
                newCat.save()
                category = Category.objects.get(name=cat)
                record.category = category
            record.save()
            print 'Saving %s' % i
            i+=1
