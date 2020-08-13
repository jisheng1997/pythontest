#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : pixiv2.py
@Time    : 2020/8/10 13:55
@Author  : jisheng
"""

import requests
from bs4 import BeautifulSoup

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.baidu.com/',
    'Connection': 'keep-alive',
}
keyword = "百合"
url = "https://pixivic.com/keywords?tag={0}&illustType=illust&VNK=b1091747".format(keyword)
res = requests.get(url,headers = headers)
html = res.text
soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())
print(soup.link.name)
