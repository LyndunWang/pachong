# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:58:11 2021

@author: dell
"""

import requests
import time

s = requests.Session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    
    }
s.headers.update(headers)
#s.post('https://wpblog.x0y1.com/wp-login.php', data = data)
data = {
    'log':'codetime',
    'pwd':'shanbay520',
    'wp-submit': '登录',
    'redirect_to':'https://wpblog.x0y1.com',
    'testcookie': '1'     
    }

commentx = '这是wlc的1个评论'
n = 1
data2  = {
    'comment': commentx,
    'submit':'发表评论',
    'comment_post_ID': '8',
    'comment_parent': '0'    
    
    }

#r = requests.post('https://wpblog.x0y1.com/wp-login.php', headers = headers, data = data)
s.post('https://wpblog.x0y1.com/wp-login.php', data = data)
s.post('https://wpblog.x0y1.com/wp-login.php', data = data)
while 1:
    
    
    result = s.post('https://wpblog.x0y1.com/wp-comments-post.php', data = data2)
    commentx = '这是wlc的第'+chr(n)+'个评论'
    time.sleep(10)
    print(result.status_code)
    if n == 5:
        break
    n += 1



