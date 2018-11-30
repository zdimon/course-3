#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
if not os.path.exists("OUTPUT"):
    os.mkdir("OUTPUT")
url='https://pythondigest.ru/'
r=requests.get(url)
with open('test.html','w') as f:
    f.write(r.text.encode('utf-8'))
soup = BeautifulSoup(r.text,"html.parser")
linkList=soup.find_all('a',{'class':'issue-item-title'})
links=[]
for l in linkList:
    links.append(l.get('href'))
link=1
for x in links:
    m=requests.get(x)
    with open('OUTPUT/output_%d.html' % (link),'w') as f:
        f.write(m.text.encode('utf-8'))
        link+=1
