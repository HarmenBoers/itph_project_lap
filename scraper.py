from lxml import html
from lxml import etree
import requests
import sqlite3
import os


class Scraper:
    def __init__(self, url):
        print('Initialising Scraper')
        self.url = url
        self.song_info = self.get_song_info()
        self.db_store()

    def get_page(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        url = self.url
        #url = 'http://www.azlyrics.com/lyrics/aaliyah/intro.html'
        MAX_RETRIES = 20

        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
        session.mount('https://', adapter)
        session.mount('http://', adapter)

        page = requests.get(url, headers=headers)
        tree = html.fromstring(page.content)

        return tree

    def get_song_info(self):
        tree = self.get_page()
        lyric = tree.xpath('//div[@class="ringtone"]/following-sibling::div[1]/text()')
        song_title = tree.xpath('//div[@class="ringtone"]/following-sibling::b[1]/text()')
        artist = tree.xpath('//div[@class="lyricsh"]/h2/b/text()')
        # js = tree.xpath('//script[@type="text/javascript"]/text()')
        # print("".join(js))

        "".join(artist).strip(" LYRICS")
        print(etree.tostring(tree))
        artist = "".join(artist).strip(" LYRICS")
        song_title = "".join(song_title).strip('"')
        lyric = "".join(lyric)

        return artist, song_title, lyric

    def db_store(self):
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
        print(self.song_info)
        conn.execute(sql, self.song_info)


        cur = conn.cursor()
        cur.execute('select * from Songs')
        rows = cur.fetchall()
        for row in rows:
            print(row)
        conn.commit()
        print("Database created and opened successfully")

#Scraper('http://www.azlyrics.com/lyrics/aaliyah/intro.html')