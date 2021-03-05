import sqlite3

def db_create():
    conn = sqlite3.connect('main_url.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS urls(
        url text,
        shorted_url text)""")

    conn.close()

def insert_urls(url: str, shorted_url: str):

    conn = sqlite3.connect('main_url.db')
    cursor = conn.cursor()

    data = [url, shorted_url]
    cursor.execute("""INSERT INTO urls VALUES (?,?)""", data)
    conn.commit()

