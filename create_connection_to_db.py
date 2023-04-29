import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sql version: {sqlite3.version}")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            
