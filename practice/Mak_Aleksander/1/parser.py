import urllib.request
import os
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def MyParse(html):
    soup = BeautifulSoup(html, features="html.parser")
    links = soup.find_all('a', class_='issue-item-title')
    linksS ={}
    for ln in links:
        linksS[ln.get('href')] = ln.text
    return linksS

def saveInFile(links, fileName):
    file = open(fileName, 'wt')
    for l in links.items():
        file.write(str(l)+ '\n')
    file.close
    

def main():
    links = MyParse(get_html('http://pythondigest.ru/'))
    script_dir = os.path.dirname(__file__)
    file = "output/test.txt"
    path=os.path.join(script_dir, file)
    saveInFile(links, path)
    
def prnt(arg):
    for a in arg.items():
        print(a)
        
if __name__ == '__main__':
    main()
