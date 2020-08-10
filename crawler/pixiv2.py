#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : pixiv2.py
@Time    : 2020/8/10 13:55
@Author  : jisheng
"""

import requests
from bs4 import BeautifulSoup
import json

image_id = []
your_proxy = ''
session = ''
page = ''
member_id = ''
url1 = 'https://www.pixiv.net/ajax/illust/' + image_id + '/pages'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Referer': 'https://www.pixiv.net/artworks/' + image_id}

if your_proxy != '':
    request = session.get(url1, proxies={'http': 'http://' + your_proxy, 'https': 'https://' + your_proxy})
else:
    request = session.get(url1)
    soup1 = BeautifulSoup(request.content, "html.parser")
    original = json.loads(soup1.string)['body'][page]['urls']['original']
    if your_proxy != '':
        img_res = requests.get(original, headers=head,
        proxies={'http': 'http://' + your_proxy, 'https': 'https://' + your_proxy})
    else:
        img_res = requests.get(original)
        with open('./image/' + str(member_id) + '_' + image_id + '_p' + str(page) + '.jpg',
        'wb') as jpg:
            jpg.write(img_res.content)