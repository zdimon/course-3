import requests
from bs4 import BeautifulSoup
import os
import re


def get_url (url):

    r = requests.get(url)
    encoded_page = r.text.encode('utf-8')
    f = open(os.path.join(os.getcwd(), 'raw_file.txt'), 'w')
    f.write(encoded_page)
    f.close()

    return encoded_page


def get_issue_items (html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find_all('div', class_='in')
    text_list = list()
    href_list = list()
    text_pattern = re.compile(r'.*>(.*)</a>')
    output_dir = os.path.join(os.getcwd(),'output')
    try:
        os.mkdir(output_dir)
        data_file = open( os.path.join( output_dir, 'data.txt' ), 'w' )
    except:
        data_file = open(os.path.join(output_dir, 'data.txt'), 'w')


    for div in divs:
        for a in div.find_all('a', class_="issue-item-title"):
            text_list.append(re.findall(text_pattern, str(a)))
            href_list.append(a['href'])
    for i in range (0, len(href_list)):
        item = ''.join(text_list[i]) + ' ==> ' + str(href_list[i])+'\n'
        data_file.write(item)

    data_file.close()

def main():
    url = 'https://pythondigest.ru/'
    get_issue_items(get_url(url))

if __name__ == '__main__':
    main()







