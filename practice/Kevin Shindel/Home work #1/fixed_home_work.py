# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup

if not os.path.exists("OTHER"):
	#os.mkrir("OTHER")
	os.mkdir("OTHER")
	

url='https://pythondigest.ru/'
r=requests.get(url)
with open('OTHER/index.txt','w') as f:
    f.write(r.text.encode('utf-8'))
soup=BeautifulSoup(r.text,'html.parser')
mass=[]
counter=0


#################
import sys
from requests.exceptions import ConnectionError, Timeout
################

try:

    for link in soup.findAll('a'):
        mass.append(str(link.get('href')))

    #with open('OTHER/index.txt','w') as f:
    for i in mass:
        counter+=1
	    #print("%s %s" %(i,counter))
	     
        if (i.find("http")) != -1:
            try:
                x=requests.get(i,timeout=3)
                with open('OTHER/%s.html' % counter,'w') as d:
                    d.write(x.text.encode('utf-8'))
                    print("Sucess!")
            except (ConnectionError, Timeout):
                print("Timeout...")
                pass				
        else:
            try:
                i = url+i
                x=requests.get(i,timeout=3)
                with open('OTHER/%s.html' % counter,'w') as d:
                    d.write(x.text.encode('utf-8'))
                    print("Sucess!")
            except (ConnectionError, Timeout):
                print("Timeout...")
                pass
					    
except (KeyboardInterrupt, SystemExit):
    sys.exit('Goobye!!!')
    
    
    
