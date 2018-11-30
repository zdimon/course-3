import requests
from bs4 import BeautifulSoup
import os



def get_url (url):

    r = requests.get(url)
    encoded_page = r.text.encode('utf-8')
    f = open(os.path.join(os.getcwd(), 'raw_file.txt'), 'w')
    f.write(encoded_page)
    f.close()

    return encoded_page


def get_issue_items (html):
    soup = BeautifulSoup( html, 'lxml' )
    divs = soup.find_all( "div", {"class": "issue-item"} )

    text_list = list()
    href_list = list()
    descr_list = list()
    output_dir = os.path.join(os.getcwd(),'output')
    try:
        os.mkdir(output_dir)
        data_file = open( os.path.join( output_dir, 'data.txt' ), 'w' )
    except:
        data_file = open(os.path.join(output_dir, 'data.txt'), 'w')

    element_id = 0
    for div in divs:
        for a in div.find_all('a', {"class": "issue-item-title"}):
            text_list.append(a.get_text())
            href_list.append(a['href'])
            if a.next_sibling.next_sibling is not None:
                element = a.next_sibling.next_sibling.get_text()
                descr_list.append(element)
            else:
                descr_list.append('')
            element_id +=1

    for i in range (0, len(href_list)):
        item = 'item '+ str(i)+ ' ' + text_list[i] + ' ==> ' + href_list[i]+'\n' + descr_list[i] + '\n\n'
        data_file.write(item.encode('utf-8'))

    data_file.close()

def main():
    url = 'https://pythondigest.ru/'
    get_issue_items(get_url(url))

if __name__ == '__main__':
    main()







