__author__ = 'Harmen'
import sqlite3
import os

def test_conn():
    conn = sqlite3.connect('songs.db')
    cur = conn.cursor()
    cur.execute('select * from Songs')
    rows = cur.fetchall()
    for row in rows:
        print('hi')
        print(row)
    conn.commit()
    print("Database created and opened successfully")

'''
This def expects a song_info list / tuple with Artist, Songname, Lyric
'''
def db_store(song_info):
    db_is_new = not os.path.exists('songs.db')
    conn = sqlite3.connect('songs.db')
    if db_is_new:
        print('Creating schema')
        sql = '''create table if not exists Songs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        artist TEXT,
        songname TEXT,
        lyric TEXT);'''
        conn.execute(sql)  # shortcut for conn.cursor().execute(sql)
    else:
        print('Schema exists\n')
    sql = '''INSERT INTO Songs
    (artist, songname, lyric)
    VALUES(?, ?, ?);'''
    print(song_info)
    conn.execute(sql, song_info)
    conn.commit()

test_conn()