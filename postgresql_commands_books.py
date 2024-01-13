import psycopg2

conn = psycopg2.connect(dbname='library_subscription', host='', user='postgres', password='')
cur = conn.cursor()

def fetch_data():
    cur.execute('SELECT * FROM BOOKS')
    rows = cur.fetchall()
    return rows


def insert_data_book(isbn, author, name, volume, binding, cost):
    try:
        query = "INSERT INTO BOOKS (isbn, author, name, volume, binding, cost) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (isbn, author, name, volume, binding, cost))
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()
    except Exception as e:
        conn.rollback()



def remove_data_book(isbn):
    try:
        cur.execute('DELETE FROM BOOKS WHERE isbn=%s', (isbn,))
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()
    except Exception as e:
        conn.rollback()


def update_data_book(author, name, volume, binding, cost, isbn):
    try:
        query = "UPDATE BOOKS SET author=%s, name=%s, volume=%s, binding=%s, cost=%s WHERE isbn =%s"
        cur.execute(query, (author, name, volume, binding, cost, isbn))
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()
    except Exception as e:
        conn.rollback()

def average_cost():
    try:
        cur.execute('SELECT AVG(cost) AS avarage_cost FROM BOOKS')
        value = cur.fetchone()
        return value
    except psycopg2.IntegrityError as e:
        conn.rollback()
    except Exception as e:
        conn.rollback()

def close_connection():
    conn.close()


fetch_data()
