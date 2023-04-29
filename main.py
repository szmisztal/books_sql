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

def add_author(conn, author):
    sql = """INSERT INTO authors(first_name, last_name, birth_date, death_date)
             VALUES(?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sql, author)
    conn.commit()
    return cur.lastrowid
def add_book(conn, book):
    sql = """INSERT INTO books(author_id, title, year_of_publication, genre, short_description)
             VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
    return cur.lastrowid

if __name__ == '__main__':
    db_file = "books_db"
    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, tables.create_books_sql)
        execute_sql(conn, tables.create_authors_sql)

    author = ("Andrzej", "Sapkowski", "1948-06-21", None)
    author_id = add_author(conn, author)
    book = (author_id, "Ostatnie życzenie", 2014, "Fantasy", "Ciachanie potworów")
    book_2 = (author_id, "Miecz przeznaczenia", 2014, "Fantasy", "Więcej ciachania potworów")
    book_id = add_book(conn, book)
    book_2_id = add_book(conn, book_2)
    conn.close()




