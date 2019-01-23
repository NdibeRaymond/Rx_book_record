import sqlite3
def connect():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER,isbn INTEGER)")
    con.commit()
    con.close()

def add_record(title,author,year,isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    con.commit()
    con.close()

def view_all():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    row = cur.fetchall()
    con.close()
    return row

def search(title = "",author = "",year = "",isbn = ""):
    z = [0,0,0,0]
    count = 0
    search_input = [title,author,year,isbn]
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    for each in search_input:
        if len(each) > 0:
            if count == 0:
                z[0] = 1
            if count == 1 :
                z[1] = 1
            if count == 2:
                z[2] = 1
            if count == 3:
                z[3] = 1
        count += 1
    count = 0
    if z == [1,1,1,1]:
        cur.execute("SELECT * FROM book WHERE title = ? AND author = ? AND year = ? AND isbn = ?",(title,author,year,isbn))
    elif z == [1,1,1,0]:
        cur.execute("SELECT * FROM book WHERE title = ? AND author = ? AND year = ?",(title,author,year))
    elif z == [1,1,0,1]:
        cur.execute("SELECT * FROM book WHERE title = ? AND author = ? AND isbn = ?",(title,author,isbn))
    elif z == [1,1,0,0]:
        cur.execute("SELECT * FROM book WHERE title = ? AND author = ?",(title,author))
    elif z == [1,0,1,1]:
        cur.execute("SELECT * FROM book WHERE title = ? AND year = ? AND isbn = ?",(title,year,isbn))
    elif z == [1,0,1,0]:
        cur.execute("SELECT * FROM book WHERE title = ? AND year = ?",(title,year))
    elif z == [1,0,0,1]:
        cur.execute("SELECT * FROM book WHERE title = ? AND isbn = ?",(title,isbn))
    elif z == [1,0,0,0]:
        cur.execute("SELECT * FROM book WHERE title = ?",(title,))
    elif z == [0,1,1,1]:
        cur.execute("SELECT * FROM book WHERE author = ? AND year = ? AND isbn = ?",(author,year,isbn))
    elif z == [0,1,1,1]:
        cur.execute("SELECT * FROM book WHERE author = ? AND year = ? AND isbn = ?",(author,year,isbn))
    elif z == [0,1,0,1]:
        cur.execute("SELECT * FROM book WHERE author = ? AND isbn = ?",(author,isbn))
    elif z == [0,1,0,0]:
        cur.execute("SELECT * FROM book WHERE author = ?",(author,))
    elif z == [0,0,1,1]:
        cur.execute("SELECT * FROM book WHERE year = ? AND isbn = ?",(year,isbn))
    elif z == [0,0,1,0]:
        cur.execute("SELECT * FROM book WHERE year = ?",(year,))
    elif z == [0,0,0,1]:
        cur.execute("SELECT * FROM book WHERE isbn = ?",(isbn,))

    z = [0,0,0,0]

    row = cur.fetchall()
    con.close()
    return row

def delete(id):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    con.commit()
    con.close()

def update(id,title,author,year,isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? where id = ?",(title,author,year,isbn,id))
    con.commit()
    con.close()

connect()
