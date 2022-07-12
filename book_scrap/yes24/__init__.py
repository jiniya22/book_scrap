from bs4 import BeautifulSoup
import requests


def get_isbn13(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    ele = soup.select_one('#infoset_specific table > tbody > tr:nth-child(3) > td')
    return ele.get_text() if ele else None
