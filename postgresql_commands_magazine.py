import psycopg2
from datetime import datetime
conn = psycopg2.connect(dbname='library_subscription', host='', user='postgres', password='')
cur = conn.cursor()

def fetch_data():
    cur.execute('SELECT * FROM MAGAZINE')
    rows = cur.fetchall()
    return rows


def insert_data_magazine(book_isbn, reader_passport_data, issue_date, deadline):
    try:
        query = "INSERT INTO MAGAZINE (book_isbn, reader_passport_data, issue_date, deadline) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (book_isbn, reader_passport_data, issue_date, deadline))
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()
    except Exception as e:
        conn.rollback()



def remove_data_magazine(book_isbn):
    try:
        cur.execute('DELETE FROM MAGAZINE WHERE book_isbn=%s', (book_isbn,))
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()
    except Exception as e:
        conn.rollback()


def update_data_magazine(book_isbn, reader_passport_data, issue_date, deadline):
    try:
        query = "UPDATE MAGAZINE SET reader_passport_data=%s, issue_date=%s, deadline=%s WHERE book_isbn=%s"
        cur.execute(query, (reader_passport_data, issue_date, deadline, book_isbn))
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()
    except Exception as e:
        conn.rollback()
        
def expired_readers():
    current_date = datetime.now().strftime('%Y-%m-%d')
    query = f"SELECT * FROM MAGAZINE WHERE deadline < '{current_date}'"
    cur.execute(query)
    expired_readers = cur.fetchall()

    return expired_readers


def close_connection():
    conn.close()


fetch_data()
