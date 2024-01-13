import psycopg2

conn = psycopg2.connect(dbname='library_subscription', host='', user='postgres', password='')
cur = conn.cursor()

def fetch_data():
    cur.execute('SELECT * FROM READERS')
    rows = cur.fetchall()
    return rows


def insert_data_reader(passport_data, full_name, phone_number, registration_date):
    try:
        query = "INSERT INTO READERS (passport_data, full_name, phone_number, registration_date) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (passport_data, full_name, phone_number, registration_date))
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()
    except Exception as e:
        conn.rollback()



def remove_data_reader(passport_data):  
    try:
        cur.execute('DELETE FROM READERS WHERE passport_data=%s', (passport_data,))
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()
    except Exception as e:
        conn.rollback()

def update_data_reader(passport_data, full_name, phone_number, registration_date):
    try:
        query = "UPDATE READERS SET full_name=%s, phone_number=%s, registration_date=%s WHERE passport_data=%s"
        cur.execute(query, (full_name, phone_number, registration_date,passport_data))
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()
    except Exception as e:
        conn.rollback()


def close_connection():
    conn.close()


fetch_data()
