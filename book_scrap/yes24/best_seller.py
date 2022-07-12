from bs4 import BeautifulSoup
import requests

from . import get_isbn13


def get_isbns():
    url_prefix = 'https://www.yes24.com/'
    book_links = get_book_links(url_prefix)

    isbns = []
    for book_link in book_links:
        isbns.append(get_isbn13(url_prefix + book_link))
    return isbns


def get_book_links(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.select('#bestList .yBestOl .rnk_lnk')

    links = []
    for r in results:
        links.append(r['href'])

    return links
