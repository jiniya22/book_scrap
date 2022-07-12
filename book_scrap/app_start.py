from yes24 import best_seller as yes24_best_seller, new_book as yes24_new_book
from data import book as data_book
from chaeking import book as chaeking_book


def best_seller():
    isbns = yes24_best_seller.get_isbns()
    book_ids = data_book.get_book_ids(isbns)

    update_book_ids_by_isbns(isbns, book_ids)

    data_book.update_best_seller(book_ids)


def new_book():
    isbns = yes24_new_book.get_isbns()
    book_ids = data_book.get_book_ids(isbns)

    update_book_ids_by_isbns(isbns, book_ids)

    data_book.update_new_book(book_ids)


def update_book_ids_by_isbns(isbns, book_ids):
    for i in range(len(book_ids)):
        if not book_ids[i]:
            book_ids[i] = chaeking_book.get_id_by_isbn(isbns[i])


if __name__ == '__main__':
    best_seller()
    new_book()

