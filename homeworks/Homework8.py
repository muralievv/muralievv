import sqlite3

def create_table():
    connect = sqlite3.connect('library.db')
    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS library(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(20) NOT NULL
        )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
        author VARCHAR(35) NOT NULL,
        year INTEGER NOT NULL,
        genre VARCHAR (20),
        available VARCHAR (10),
        book_id INTEGER NOT NULL,
        FOREIGN KEY (book_id) REFERENCES library(id)
        )
        ''')
    connect.commit()
    connect.close()
    #create_table()


def insert_test_db():
    connect = sqlite3.connect('library.db')
    cursor = connect.cursor()
    # cursor.execute(
    #     'INSERT INTO library (title) VALUES (?)',
    #     ("Psychology",)
    # )

    cursor.execute(
        'INSERT INTO books (author, year, genre, available, book_id) VALUES (?,?,?,?,?)',
        ('M.N.M', 2024, 'psychology', 'yes', 3)
    )
    connect.commit()
    connect.close()
    print("Данные успешно добавлены")
# create_table()
# insert_test_db()

def get_book_info():
    connect = sqlite3.connect('library.db')
    cursor = connect.cursor()
    cursor.execute('''
    SELECT library.title, books.author, books.year
    FROM library INNER JOIN books ON book_id = books.book_id
    ''')
    users = cursor.fetchall()
    print(users)
get_book_info()

def get_newest_book():
    connect = sqlite3.connect('library.db')
    cursor = connect.cursor()
    cursor.execute(
        'SELECT library.title, MAX(books.year) FROM library INNER JOIN books on library.id = books.book_id'
    )
    users = cursor.fetchone()
    print(users)
get_newest_book()
def create_my_view():
    connect = sqlite3.connect('library.db')
    cursor = connect.cursor()
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS my_view1 AS
    SELECT library.title, books.author, books.year
    FROM library INNER JOIN books ON library.id = books.book_id'''
                   )
    connect.commit()
    connect.close()
create_my_view()
