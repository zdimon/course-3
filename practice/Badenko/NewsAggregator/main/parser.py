# -*- coding: utf-8 -*-
import re, requests, bs4
from bs4 import BeautifulSoup
from .models import Article, Domain


class Parser(object):
    def updateDataFromSite(self):
        site = 'https://pythondigest.ru/'
        html = requests.get(site)
        bs = BeautifulSoup(html.text, 'html.parser')    
        for garbage in bs.find_all('div', class_='items-group-container'):
            for div in garbage.find_all('div', class_='issue-item'):            
                description = ''
                a = Article()
                for tag in div.children:
                    if isinstance(tag, bs4.element.Tag) and tag.name == 'a':
                        a.url = tag.get('href')
                        a.title = tag.text
                        d = Domain()
                        try:
                            d.url = re.sub(r'(.*://)?([^/?]+).*', r'\g<1>\g<2>', tag.get('href'))
                            d.save()
                            a.domain = d
                        except:
                            d = Domain.objects.get(url = re.sub(r'(.*://)?([^/?]+).*', r'\g<1>\g<2>', tag.get('href')))
                            a.domain = d
                        
                    if isinstance(tag, bs4.element.Tag) and tag.name == 'p':
                        description += tag.text
                a.description = description
                try:
                    a.save()
                except:
                    pass

                

