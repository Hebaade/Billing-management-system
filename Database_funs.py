import sqlite3
def logintable():
    con = sqlite3.connect('login.db')
    cursor = con.cursor()
    cursor.execute("""  create table IF NOT EXISTS login(
                username TEXT PRIMARY KEY NOT NULL,
                password TEXT NOT NULL
                ) """)
    con.commit()
    con.close()


def addUser(username, password):
    con = sqlite3.connect('login.db')
    cursor = con.cursor()
    cursor.execute('insert into login values(?,?)', (username, password))
    con.commit()
    con.close()


def showAllUsers():
    con = sqlite3.connect('login.db')
    cursor = con.cursor()
    data = cursor.execute('select * from login')
    con.commit()
    return data
