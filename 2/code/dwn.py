# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
url = 'https://realpython.com'
rez = requests.get(url)
with open('out/index.html','w') as f:
    f.write(rez.text.encode('utf-8'))
soup = BeautifulSoup(rez.text, 'html.parser')
for i in soup.findAll('a'):
    href = i['href']
    if (i['href'].find('http')==-1):
        href = url+href
    
    print 'Loading.....%s' % href
    name = i['href'].replace('/','_')+'.html'
    if href !='/':
        
        r = requests.get(href)
        with open('out/%s' % name,'w') as f:
            f.write(r.text.encode('utf-8'))
