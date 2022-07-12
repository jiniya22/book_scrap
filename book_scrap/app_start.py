from best_seller import yes24 as best_seller_yes24
from data import book as data_book
from chaeking import book as chaeking_book


def app():
    isbns = best_seller_yes24.get_isbns()
    book_ids = data_book.get_book_ids(isbns)

    for i in range(len(book_ids)):
        if not book_ids[i]:
            book_ids[i] = chaeking_book.get_id_by_isbn(isbns[i])

    data_book.update_best_seller(book_ids)


if __name__ == '__main__':
    app()
