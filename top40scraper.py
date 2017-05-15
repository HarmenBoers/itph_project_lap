__author__ = 'Harme'
from lxml import html
from lxml import etree
import requests
import sqlite3
import os
import re
from datetime import date as dt

class Scraper:

    def __init__(self):
        print('Firing Up Scraper!')

   #     for year in range(1965,2017):
    #        for week in range(1,53):
        top40_dict = {}
        year = 2017
        week = 19

        #generate url
        url = "https://www.top40.nl/top40/" + str(year) + "/week-" + str(week)
        print(url)

        #retrieve html page to parse
        tree = self.get_page(url)

        #retrieve date
        date = tree.xpath('//div[@class="week-info text-center"]/span[@class="date"]/text()')
        date = self.stripDate(date[0])
        top40_dict['Date'] = date

        #retrieve songs
        self.get_info(tree, top40_dict)
        print(top40_dict)



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

    def get_info(self, tree, top40_dict):


        titles = tree.xpath('//span[@class="title"]/text()')
        credits = tree.xpath('//span[@class="credit"]/text()')
        details = tree.xpath('//div[@class="title-stats row-fluid"]/child::*/strong[1]/text()')

        print(titles)
     #  print(tree.xpath('//div[@class="title-credit text-center"]/text()'))
        for x in range(0, 40):
            hit_dict = {}
            hit_dict['title'] = re.sub('\\n\s*', "", titles[x])
            hit_dict['credit'] = credits[x]
            hit_dict['weken'] = details[x*4]
            hit_dict['hoogste_notering'] = details[x*4+1]
            hit_dict['punten'] = details[x*4+2]
            hit_dict['jaar'] = re.sub('\\n\s*', "", details [x*4+3])
            print(hit_dict)
            top40_dict[x+1] = hit_dict


           # print(title)
        #print(tree.xpath('//[@title="title-credit"]/text()'))
        #print(tree.xpath("string()"))

        #DETAILS


        #weken
        #hoogste notering
        #punten
        #jaar

        return

    def stripDate(self, datestring):
        #Input format: [' (6 mei 2017)']
        m = re.search('[a-zA-Z]+', datestring)

        #month table
        a = ['01','02','03','04','05','06','07','08','09','10','11','12']
        b= ['januari','februari','maart','april','mei','juni','juli','augustus','september','oktober','november','december']
        d = dict(zip(b,a))
        datestring = re.findall('\((.+)\)', str(datestring))[0]

        l = datestring.split(" ")
        l[1] = d[l[1]]
        datestring = "-".join(l)

        if datestring[1] is '-':
            #day number must be zero-padded
            datestring = "0" + datestring

        #date = dt.(datestring, '%d %m %Y')
        return datestring

Scraper()