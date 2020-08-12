#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2020/8/10 13:13
@Author  : jisheng
"""
import requests
from bs4 import BeautifulSoup

url="https://www.taobao.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
html = requests.get(url,headers=headers)
val = BeautifulSoup(html.text, 'html.parser')
print(val.find())