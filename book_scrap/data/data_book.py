import mariadb

datasource = {'dbType': 'mariadb', 'host': '127.0.0.1', 'port': '3306', 'username': 'test', 'password': 'test',
              'database': 'book'}


def get_book_ids(isbns):
    ids = [None] * 10

    with mariadb.connect(host=datasource['host'], user=datasource['username'], password=datasource['password'],
                         db=datasource['database']) as conn:
        with conn.cursor(named_tuple=True) as cur:
            for i in range(len(isbns)):
                sql = "SELECT id FROM book WHERE isbn13 = %s LIMIT 1" % isbns[i]
                cur.execute(sql)
                result = cur.fetchone()
                if result:
                    ids[i] = result.id
    return ids


def update_best_seller(book_ids):
    with mariadb.connect(host=datasource['host'], user=datasource['username'], password=datasource['password'],
                         db=datasource['database']) as conn:
        with conn.cursor(named_tuple=True) as cur:
            for i in range(len(book_ids)):
                if not book_ids[i]:
                    continue
                sql = """
                INSERT INTO best_seller(id, book_id)
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE book_id = VALUES(book_id)
                """ % (i + 1, book_ids[i])
                cur.execute(sql)
                conn.commit()
    print('best_seller update done!')
