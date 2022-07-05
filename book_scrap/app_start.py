from book_scrap.best_seller import yes24
from book_scrap.data import book


def app():
    isbns = yes24.get_isbns()
    ids = book.get_book_ids(isbns)

    for t in zip(isbns, ids):
        if not t[1]:
            print(t[0])


if __name__ == '__main__':
    app()
