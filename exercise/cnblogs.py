#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : cnblogs.py
@Time    : 2020/8/14 16:36
@Author  : jisheng
"""
import requests
from lxml import etree
import time

#https://www.cnblogs.com/

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
base_url = "https://www.cnblogs.com/"
headers_next = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','referer' : 'https://www.cnblogs.com/'}

def get_urls(base_url):
    tiezi_urls = []
    # 获取浏览器响应
    res = requests.get(base_url, headers=headers)
    if res.status_code == 200:
        html = etree.HTML(res.text)
        # 获取帖子的链接已列表的形式保存
        result = html.xpath("//div[@class='post-item-text']/a/@href")
        for url in result:
            tiezi_urls.append(url)
    return tiezi_urls

def get_data(urls):
    for url in urls:
        res = requests.get(url, headers=headers_next)
        if res.status_code == 200:
            html = etree.HTML(res.text)
            # 获取帖子详细信息
            title = html.xpath("//h1[@class = 'postTitle']/a/span/text()")
            print(title)
            article = html.xpath("//h")
get_data(get_urls(base_url))




