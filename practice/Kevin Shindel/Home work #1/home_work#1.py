# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup

if not os.path.exists("OTHER"):
	os.mkdir("OTHER")
	

url='https://pythondigest.ru/'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
mass=[]
counter=0

for link in soup.find_all('a'):
	mass.append(str(link.get('href')))
	with open('OTHER/index.txt','w') as f:
		for i in mass:
			counter+=1
			#print("%s %s" %(i,counter))
			 
			if (i.find("http")) != -1:
				try:
					x=requests.get(i,timeout=3)
					with open('OTHER/%s.html' % counter,'w') as d:
						d.write(x.text.encode('utf-8'))
						print("Sucess!")
				except:
					print("Timeout...")
					pass				
			else:
				try:
					i = url+i
					x=requests.get(i,timeout=3)
					with open('OTHER/%s.html' % counter,'w') as d:
						d.write(x.text.encode('utf-8'))
						print("Sucess!")
				except:
					print("Timeout...")
					pass
