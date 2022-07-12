from bs4 import BeautifulSoup
import requests
from . import get_isbn13


def get_isbns():
    url_prefix = 'https://www.yes24.com'
    book_links = get_book_links(url_prefix + '/24/Category/NewProduct')
    isbns = []
    for book_link in book_links:
        isbn = get_isbn13(url_prefix + book_link)
        isbns.append(isbn)
    return isbns


def get_book_links(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.select('#topBooksUl_001 > li > .goods_info > p.goods_name > a')

    links = []
    for r in results:
        links.append(r['href'])

    return links
