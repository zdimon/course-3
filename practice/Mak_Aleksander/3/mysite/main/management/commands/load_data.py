from django.core.management.base import BaseCommand
from main.models import Poem
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):

    def handle(self, *args, **options):
        # ...

        print('Start')
        Poem.objects.all().delete()

        url = "http://perashki.ru/piro/all"
        r = requests.get(url)
        encoded_page = r.text.encode('utf-8')
        soup = BeautifulSoup(encoded_page, features="html.parser")
        core_div = soup.find("div", {"id": "PiroList"})
        divs = core_div.find_all("div", {"class": "TextContainer"})

        for div in divs:
            poem = Poem()
            poem.content = div.find("div", {"class": "Text"}).get_text()
            poem.author = div.find("a").get_text()
            poem.date = div.find("span", {"class": "date"}).get_text()
            poem.save()
        print("End")
