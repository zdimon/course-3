import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
from main.models import News, Category


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--url',
            dest ='url',
            help ='Parsing site items, links and descriptions',
        )
    def handle(self, *args, **options):

        parser = Parser()
        parser.parse_category()
        parser.parse_category_articles()


class Parser():

    def __init__(self):
        News.objects.all().delete()
        self.url = 'https://xakep.ru/'
        self.title_list = []
        self.href_list = []
        self.description = []
        self.article = []
        self.category = 'Main'

    def soup(self, *args):
        try:
            r = requests.get(*args)
        except:
            r = requests.get(self.url)
        encoded_page = r.text.encode( 'utf-8' )
        soup = BeautifulSoup(encoded_page, 'html.parser' )
        return soup

    def parse_category(self):
        Category.objects.all().delete()
        soup = self.soup(self.url)
        category_title = []
        category_link = []
        for div in soup.find_all("div", {"class": "secondary-menu"}):
            for li in div.find_all('li'):
                category_title.append(li.get_text())
                category_link.append(li.find('a')['href'])
        category_title.append(self.category)
        category_link.append(self.url)
        category = zip(category_title, category_link)
        return category

    def main_page(self, url):
        self.title_list = []
        self.href_list = []
        self.description = []
        self.article = []
        soup = self.soup(url)
        divs = soup.find_all("div", {"class": "block-article-content-wrapper"})
        for div in divs:
            for p in div.find_all("p", {"class": "block-exb"}):
                self.description.append(p.get_text())
            for h in div.find_all("h3"):
                a = h.find("a")
                self.title_list.append(a.get_text())
                self.href_list.append(a['href'])
        return self.href_list

    def each_article(self, category, url_list):
        main = Category(name=category)
        main.save()
        for link in url_list:
            soup = self.soup( link )
            div = soup.find( "div", {"class": "bdaia-post-content"} )
            p_list = div.find_all( "p" )
            description = []
            for p in p_list:
                description.append( p.get_text() )
            self.article.append(u''.join( description ).encode('utf-8'))
        full = zip( self.title_list, self.href_list, self.description, self.article)
        for i in full:
            item = News( item_title=i[0], item_link=i[1], item_short_descr=i[2], article=i[3], category = main)
            item.save()
            i = []

    def parse_category_articles(self):
        cat_list = self.parse_category()
        for i in cat_list:
            url = i[1]
            category = i[0]
            print 'Parsing %s' % category, url
            self.each_article(category, self.main_page(url))


