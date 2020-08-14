#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : Oct_14.py
@Time    : 2020/8/14 14:15
@Author  : jisheng
"""

from lxml import etree
with open('file/web.html','r') as file:
    file1 = file.read()

HtmlElement = etree.HTML(file1)
res1 = HtmlElement.xpath('//div[@id="menu"]/a/text()')
res2 = HtmlElement.xpath('//div[@id="menu"]/a/@href')
res3 = HtmlElement.xpath('string(//div[@id="menu"])')
res4 = HtmlElement.xpath('//div[@class="left"]/a/@href')
res5 = HtmlElement.xpath('//div[@class="right"]/a[position()<4]')
for i in res5:
    print(i.text)

