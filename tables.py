create_books_sql = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    year_of_publication INTEGER NOT NULL,
    genre TEXT
);
"""

create_authors_sql = """
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE,
    death_date DATE,
    book_id INTEGER NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books (id)
);
"""
