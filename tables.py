create_authors_sql = """
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE,
    death_date DATE
);
"""

create_books_sql = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    author_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    year_of_publication INTEGER NOT NULL,
    genre TEXT,
    short_description TEXT,
    FOREIGN KEY (author_id) REFERENCES authors (id)
);
"""

