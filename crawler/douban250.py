#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : douban250.py
@Time    : 2020/8/13 21:17
@Author  : jisheng
"""

import requests
import re
import time
from bs4 import BeautifulSoup
import pandas

start_time = time.time()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Host': 'movie.douban.com','Origin': 'movie.douban.com'}

headers_urls = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
#获取豆瓣250排行榜网址
top250_url = "https://movie.douban.com/top250?start={0}&filter="

directors = []
movie_names = []
years = []
starring = []
types = []
regions = []
language_list = []

def operate_url(url):
    urls = []
    for i in range(0,50,25):
        movielists_url = url.format(i)
        res = requests.get(movielists_url,headers = headers)
        if res.status_code == 200:
            pattern1 = re.compile('<div.*?class="item">.*?<div.*?class="pic">.*?<a.*?href="(.*?)">', re.S)
            # 去掉所有换行符，并用正则表达式去匹配每一个页面的具体电影
            movieinfo_url = re.findall(pattern1, res.text)
            for i in movieinfo_url :
                urls.append(i)
    return urls

def movie_info(urls):
    for i in range(0,10,1):
        res = requests.get(urls[i],headers = headers)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text,"lxml")

            #<span class='pl'>导演</span>: <span class='attrs'><a href="/celebrity/1047973/" rel="v:directedBy">弗兰克·德拉邦特</a></span>  获取电影导演名字
            directors.append(soup.find('a', rel="v:directedBy").text)

            #<span property="v:itemreviewed">肖申克的救赎 The Shawshank Redemption</span>   获取电影名字
            movie_names.append(soup.find('span',property="v:itemreviewed").text)

            #<span class="year">(1994)</span>  获取电影上映年份
            years.append(soup.find('span',class_="year").text)

            #<a href="/celebrity/1054521/" rel="v:starring">蒂姆·罗宾斯</a>   获取主演的名字（不止一个）
            star_temp = []
            for star in soup.find_all('a',rel="v:starring"):
                star_temp.append(star.text)
                starring.append(star_temp)

            #<span property="v:genre">剧情</span> / <span property="v:genre">犯罪</span><br/>   获取电影类型（不止一个）
            type_temp = []
            for type in soup.find_all('span',property="v:genre"):
                type_temp.append(type.text)
                types.append(type_temp)

            # #<span class="pl">制片国家/地区:</span> 美国<br/>   获取制片国家/地区
            region = soup.find('span',text="制片国家/地区:").next_sibling[1:]
            regions.append(region)

            #<span class="pl">语言:</span> 英语<br/>  获取语言
            language = soup.find('span',text="语言:").next_sibling[1:]
            language_list.append(language)

            #<span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="1994-09-10(多伦多电影节)">1994-09-10(多伦多电影节)</span>

            #<span class="pl">片长:</span> <span property="v:runtime" content="142">142分钟</span>

            #<strong class="ll rating_num" property="v:average">9.7</strong>   获取豆瓣评分

            #<span property="v:votes">2109734</span>人评价    获取评价人数

            #<span class ="all hidden" >20世纪40年代末，小有成就的青年银行家安迪（蒂姆·罗宾斯TimRobbins饰）因涉嫌杀害妻子及她的情人而锒铛入狱……</span>   获取故事简介



movie_info(operate_url(top250_url))
print(directors)
print(movie_names)
print(years)
print(starring)
print(types)
print(regions)


end_time = time.time()
print("程序运行了" + str(round((end_time-start_time),1)) + '秒，也太慢了吧')


