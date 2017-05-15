__author__ = 'Harme'
from lxml import html
from lxml import etree
import requests
import sqlite3
import os
import re
from datetime import date as dt

class Scraper:

    def __init__(self, url):
        print('Initialising Scraper')
        tree = self.get_page(url)
        #self.get_info(tree)
        print('hi')
        date = tree.xpath('//div[@class="week-info text-center"]/span[@class="date"]/text()')
        date = self.stripDate(date[0])
        print(date)

    def get_page(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        MAX_RETRIES = 20

        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
        session.mount('https://', adapter)
        session.mount('http://', adapter)

        page = requests.get(url, headers=headers)
        tree = html.fromstring(page.content)

        return tree

    def get_info(self, tree):
        #TITLES

        titles = tree.xpath('//div[@class="title-credit text-center"]/text()')
     #   print(tree.xpath('//div[@class="title-credit text-center"]/text()'))
        for title in titles:
            title = re.sub('\\n\s*', "", title)
           # print(title)
        #print(tree.xpath('//[@title="title-credit"]/text()'))
        #print(tree.xpath("string()"))

        #CREDIT

        credits = tree.xpath('//span[@class="credit"]/text()')
        for c in credits:
            break
            # print(c)

        #DETAILS

        details = tree.xpath('//div[@class="title-stats row-fluid"]/child::*/strong[1]/text()')
        #weken
        #hoogste notering
        #punten
        #jaar
        top_dict = {}  #2017-19, val: 40x hit_dict

        return

    def stripDate(self, datestring):
        #Input format: [' (6 mei 2017)']
        m = re.search('[a-zA-Z]+', datestring)
        print(m.group())
        #month table

        a = ['01','02','03','04','05','06','07','08','09','10','11','12']
        b= ['januari','februari','maart','april','mei','juni','juli','augustus','september','oktober','november','december']
        d = dict(zip(b,a))
        print(datestring)
        datestring = re.findall('\((.+)\)', str(datestring))[0]

        l = datestring.split(" ")
        l[1] = d[l[1]]
        print(l)
        datestring = "-".join(l)

        if datestring[1] is '-':
            datestring = "0" + datestring

        #date = dt.(datestring, '%d %m %Y')
        print(datestring)
        return datestring

Scraper("https://www.top40.nl/top40/2017/week-18")