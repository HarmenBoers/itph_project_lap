from lxml import html
from lxml import etree
import requests
import sqlite3
import os


class Scraper:
    def __init__(self, url):
        print('Initialising Scraper')
        self.url = url
        self.song_info = self.get_song_info(url)

    def get_page(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        #url = self.url
        #url = 'http://www.azlyrics.com/lyrics/aaliyah/intro.html'
        MAX_RETRIES = 20

        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
        session.mount('https://', adapter)
        session.mount('http://', adapter)
        print('Connecting to AZLyrics.com')
        page = requests.get(url, headers=headers)
        tree = html.fromstring(page.content)
        return tree

    def get_song_info(self, url):
        tree = self.get_page(url)
        print('Parsing Information')
        lyric = tree.xpath('//div[@class="ringtone"]/following-sibling::div[1]/text()')
        song_title = tree.xpath('//div[@class="ringtone"]/following-sibling::b[1]/text()')
        artist = tree.xpath('//div[@class="lyricsh"]/h2/b/text()')
        # js = tree.xpath('//script[@type="text/javascript"]/text()')
        # print("".join(js))

        "".join(artist).strip(" LYRICS")
        artist = "".join(artist).strip(" LYRICS")
        song_title = "".join(song_title).strip('"')
        lyric = "".join(lyric)
        return artist, song_title, lyric
#Scraper('http://www.azlyrics.com/lyrics/aaliyah/intro.html')