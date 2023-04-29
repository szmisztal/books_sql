import sqlite3
from sqlite3 import Error
import tables
from create_connection_to_db import create_connection

def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

if __name__ == '__main__':
    db_file = "books_db"
    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, tables.create_books_sql)
        execute_sql(conn, tables.create_authors_sql)
        conn.close()

