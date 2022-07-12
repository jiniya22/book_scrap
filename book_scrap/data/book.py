import pymysql


datasource = {'dbType': 'mysql', 'host': '127.0.0.1', 'port': '3306', 'username': 'test', 'password': 'test',
              'database': 'book'}


def get_book_ids(isbns):
    ids = [None] * len(isbns)

    with pymysql.connect(host=datasource['host'], user=datasource['username'], password=datasource['password'],
                         db=datasource['database'], charset="utf8", cursorclass=pymysql.cursors.DictCursor) as conn:
        with conn.cursor() as cur:
            for i in range(len(isbns)):
                if not isbns[i]:
                    continue
                sql = "SELECT id FROM book WHERE isbn13 = %s LIMIT 1" % isbns[i]
                cur.execute(sql)
                result = cur.fetchone()
                if result:
                    ids[i] = result['id']
    return ids


def update_best_seller(book_ids):
    with pymysql.connect(host=datasource['host'], user=datasource['username'], password=datasource['password'],
                         db=datasource['database'], charset="utf8", cursorclass=pymysql.cursors.DictCursor) as conn:
        with conn.cursor() as cur:
            for i in range(len(book_ids)):
                if book_ids[i]:
                    sql = """
                    INSERT INTO best_seller(id, book_id)
                    VALUES (%s, %s)
                    ON DUPLICATE KEY UPDATE book_id = VALUES(book_id)
                    """ % (i + 1, book_ids[i])
                else:
                    sql = """
                    DELETE FROM best_seller WHERE id = %s
                    """ % (i + 1)
                cur.execute(sql)
                conn.commit()
    print('best_seller update done!')


def update_new_book(book_ids):
    with pymysql.connect(host=datasource['host'], user=datasource['username'], password=datasource['password'],
                         db=datasource['database'], charset="utf8", cursorclass=pymysql.cursors.DictCursor) as conn:
        with conn.cursor() as cur:
            for i in range(len(book_ids)):
                if book_ids[i]:
                    sql = """
                    INSERT INTO new_book(id, book_id)
                    VALUES (%s, %s)
                    ON DUPLICATE KEY UPDATE book_id = VALUES(book_id)
                    """ % (i + 1, book_ids[i])
                else:
                    sql = """
                    DELETE FROM new_book WHERE id = %s
                    """ % (i + 1)
                cur.execute(sql)
                conn.commit()
    print('new_book update done!')
