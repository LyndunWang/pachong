# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:56:16 2021

@author: dell
"""

import requests
import time
from bs4 import BeautifulSoup

def get_movie(url):
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    req = requests.get(url, headers = headers)
    a = BeautifulSoup(req.text, 'html.parser')
    items = a.find_all('div', class_ = "hd")
    for i in items:
        movie = i.find('a')        
        addr = movie['href']
        b = movie.find('span')
        
        name = b.text
                
        print(name, addr)
url = 'https://movie.douban.com/top250?start={0}'
url_all = [url.format(i*25) for i in range(25)]
for x in url_all:
    get_movie(x)
    time.sleep(1)    