import os
import psycopg2
os.chdir(__file__.replace(os.path.basename(__file__), ''))

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()

def addEntry(name, age):
    cur.execute("INSERT INTO posts(name, age) VALUES(%s, %s)", [name, age])
    conn.commit()

def show():
    cur.execute("SELECT * FROM posts")
    return cur.fetchall()

def createTable():
    cur.execute("DROP TABLE IF EXISTS posts")
    cur.execute(""" CREATE TABLE posts (
        name TEXT,
        age INTEGER
    )""")
    conn.commit()

if __name__ == '__main__':
    createTable()
