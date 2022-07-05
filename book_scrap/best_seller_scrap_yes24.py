from bs4 import BeautifulSoup
import requests


def app_start():
    url_prefix = 'https://www.yes24.com/'
    book_links = get_book_links(url_prefix)

    isbns = []
    for book_link in book_links:
        isbns.append(get_isbn13(url_prefix + book_link))
    print(isbns)


def get_book_links(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.select('#bestList .yBestOl .rnk_lnk')

    links = []
    for r in results:
        links.append(r['href'])

    return links


def get_isbn13(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    isbn13 = soup.select_one('#infoset_specific table > tbody > tr:nth-child(3) > td').get_text()
    return isbn13


if __name__ == '__main__':
    app_start()

