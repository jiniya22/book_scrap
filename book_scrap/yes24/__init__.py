from bs4 import BeautifulSoup
import requests


def get_isbn13(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.select('#infoset_specific table > tbody > tr > th')
    for i in range(len(tags)):
        if tags[i].get_text() == 'ISBN13':
            ele = soup.select_one('#infoset_specific table > tbody > tr:nth-child({}) > td'.format(i + 1))
            break
    return ele.get_text() if ele else None
