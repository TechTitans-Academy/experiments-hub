import psycopg2
import time
from psycopg2.extras import RealDictCursor

def get_connection(retries=10, delay=2):
    """
    Attempts to connect to the PostgreSQL database with retries.
    """
    attempt = 0
    while attempt < retries:
        try:
            conn = psycopg2.connect(
                host='db',
                database='votesdb',
                user='postgres',
                password='postgres'
            )
            return conn
        except psycopg2.OperationalError as e:
            print(f"[DB] Connection failed: {e}")
            attempt += 1
            print(f"[DB] Retrying in {delay} seconds... ({attempt}/{retries})")
            time.sleep(delay)
    raise Exception("[DB] Could not connect to the database after multiple attempts.")

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            animal TEXT PRIMARY KEY,
            count INTEGER DEFAULT 0
        )
    ''')
    for animal in ['elephant', 'lion', 'cat', 'dog']:
        cur.execute(
            'INSERT INTO votes (animal, count) VALUES (%s, %s) ON CONFLICT (animal) DO NOTHING',
            (animal, 0)
        )
    conn.commit()
    cur.close()
    conn.close()

def update_vote(animal, count):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('UPDATE votes SET count = %s WHERE animal = %s', (count, animal))
    conn.commit()
    cur.close()
    conn.close()

