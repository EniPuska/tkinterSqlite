import sqlite3

def connection():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book(ID INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()

def insertBook(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book VALUES (null, ?, ?, ?, ?)", (title, author, year, isbn))
    connection.commit()
    connection.close()

def viewBooks():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    connection.close()
    return rows

def searchBook(title = "", author = "", year = "", isbn = ""):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows

def deleteBook(ID):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE ID = ?", (ID, ))
    connection.commit()
    connection.close()

def update(ID, title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE book set title = ?, author = ?, year = ?, isbn = ? WHERE ID = ?", (title, author, year, isbn , ID))
    connection.commit()
    connection.close()

connection() 