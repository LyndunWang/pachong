# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:46:45 2021

@author: dell
"""

import requests
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
lasthotcommentid = " "
for pagenum in range(5):
    params = {
    'g_tk': '5381',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'GB2312',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0',
    'cid': '205360772',
    'reqtype': '2',
    'biztype': '1',
    'topid': '212877900',
    'cmd': '8',
    'needmusiccrit': '0',
    'pagenum': pagenum,
    'pagesize': '25',
    'lasthotcommentid': lasthotcommentid,
    'domain': 'qq.com',
    'ct': '24',
    'cv': '10101010'
    }
    res = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?', headers=headers, params=params)
    data = res.json()
    for a in data['comment']['commentlist']:
        print('{0}:{1}'.format(a['nick'], a['rootcommentcontent']))
    lasthotcommentid = data['comment']['commentlist'][-1]['rootcommentid']
    time.sleep(1)