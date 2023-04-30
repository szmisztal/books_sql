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

def select_all(conn, table):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    return rows

def select_where(conn, table, query):
   cur = conn.cursor()
   values = tuple(query.values())
   conditions = ' AND '.join(f'{k} = ?' for k in query.keys())
   cur.execute(f"SELECT * FROM {table} WHERE {conditions}", values)
   rows = cur.fetchall()
   return rows

def update(conn, table, set_values, where):
    cur = conn.cursor()
    set_update = ', '.join(f"{k} = ?" for k in set_values.keys())
    where_update = ' AND '.join(f"{k} = ?" for k in where.keys())
    values = tuple(set_values.values()) + tuple(where.values())
    cur.execute(f"UPDATE {table} SET {set_update} WHERE {where_update}", values)
    conn.commit()

if __name__ == '__main__':
    db_file = "books_db"
    conn = create_connection(db_file)
    cur = conn.cursor()
    if conn is not None:
        execute_sql(conn, tables.create_books_sql)
        execute_sql(conn, tables.create_authors_sql)

    author = ("Andrzej", "Sapkowski", "1948-06-21", None)
    author_id = add_author(conn, author)
    author_2 = ("J.R.R", "Tolkien", "1892-01-03", None)
    author_2_id = add_author(conn, author_2)
    book = (author_id, "Ostatnie życzenie", 2014, "Fantasy", "Ciachanie potworów")
    add_book(conn, book)
    book_2 = (author_id, "Miecz przeznaczenia", 2014, "Fantasy", "Więcej ciachania potworów")
    add_book(conn, book_2)
    book_3 = (author_2_id, "Drużyna Pierścienia", 1954, "Dark Fantasy", "Wycieczka do Mordoru")
    add_book(conn, book_3)
    book_4 = (author_2_id, "Dwie Wieże", 1954, "Dark Fantasy", "Wycieczki do Mordoru ciąg dalszy")
    add_book(conn, book_4)
    book_5 = (author_2_id, "Powrót Króla", 1955, "Dark Fantasy", "Koniec wycieczki")
    add_book(conn, book_5)
    print(select_all(conn, "books"))
    print(select_where(conn, "authors", {"first_name": "Andrzej"}))
    print(select_where(conn, "books", {"genre": "Fantasy"}))
    print(update(conn, "authors", {"first_name": "John Ronald Reuel"}, {"id": 2}))
    print(select_all(conn, "authors"))
    conn.close()




