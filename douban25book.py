# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:36:02 2021

@author: dell
"""

import requests
from bs4 import BeautifulSoup
import time

def get_book(url):
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
  }
    req = requests.get(url, headers = headers)
    books = BeautifulSoup(req.text, 'html.parser')
    items = books.find_all('div', class_ = 'pl2')
    for i in items:
        book = i.find('a')
        name = book['title']
        addr = book['href']
        print(name, addr)

url = 'https://book.douban.com/top250?start={0}'
book_all = [url.format(i*25) for i in range(25)]

for x in book_all:
    get_book(x)
    time.sleep(1)