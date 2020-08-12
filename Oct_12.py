#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : Oct_12.py
@Time    : 2020/8/12 11:41
@Author  : jisheng
"""

import requests
import json
from lxml import etree

path1 = "https://www.taobao.com"
path2 = "https://httpbin.org/get"
path3 = "https://github.com/timeline.json"
path4 = "http://ibeifeng.com"
dict1 = {"username":"jisheng"
         ,"password":"123456"
         ,"age":24,"sex":"man"}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
# res1 = requests.get(path1,headers = headers)
# res2 = requests.get(path2,headers = headers,params=dict1)
# res3 = requests.get(path3,headers = headers,stream = True)
res4 = requests.get(path4,headers = headers)


# print(res3.json())
# print(res4.raw.read(100))
# print(res4.cookies)
# print(res4.cookies['ECS[visit_times]'])


