from book_scrap.best_seller import yes24
from book_scrap.data import data_book
from book_scrap.chaeking import book


def app():
    isbns = yes24.get_isbns()
    book_ids = data_book.get_book_ids(isbns)

    for i in range(len(book_ids)):
        if not book_ids[i]:
            book_ids[i] = book.get_id_by_isbn(isbns[i])

    data_book.update_best_seller(book_ids)


if __name__ == '__main__':
    app()
