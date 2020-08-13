#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : douban_example.py
@Time    : 2020/8/13 21:29
@Author  : jisheng
"""
import requests
from bs4 import BeautifulSoup
import re
import pandas

headers = {
    'Host': 'movie.douban.com',
    'Origin': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36',
}
base_url = 'https://movie.douban.com/top250?start={}&filter='

response = requests.get('https://movie.douban.com/top250?start=0&filter=', headers=headers)
if response.status_code == 200:
    # print(response.text)
    pass

pattern1 = re.compile('<div.*?class="item">.*?<div.*?class="pic">.*?<a.*?href="(.*?)">',
                      re.S)  # 去掉所有换行符，并用正则表达式去匹配每一个页面的具体电影
urls = re.findall(pattern1, response.text)

directors = []  # 导演

names = []  # 电影名

stars = []  # 主演

countrys = []  # 电影的出产地

languages = []  # 电影语言

headers_urls = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}


# <span property="v:itemreviewed">肖申克的救赎 The Shawshank Redemption</span>
# <a href="/celebrity/1047973/" rel="v:directedBy">弗兰克·德拉邦特</a>
# <a href="/celebrity/1054521/" rel="v:starring">蒂姆·罗宾斯</a>
def base_urls(base_url):
    urls = []
    # 这里我们只能前两页做测试，所以range只设置到了50
    # for i in range(0, 275, 25):
    #     true_url = base_url.format(i)
    #     print(true_url)
    for i in range(0, 50, 25):
        true_url = base_url.format(i)
        print(true_url)

        response = requests.get(true_url, headers=headers)
        if response.status_code == 200:
            # print(response.text)

            pattern1 = re.compile('<div.*?class="item">.*?<div.*?class="pic">.*?<a.*?href="(.*?)">', re.S)
            # 去掉所有换行符，并用正则表达式去匹配每一个页面的具体电影
            url = re.findall(pattern1, response.text)
            # 因为这里是用findall，他返回的是一个列表，如果我们直接append，会导致列表嵌套，故我们这里用个for循环提取出列表的元素再append进去
            print(url)
            for i in url:
                urls.append(i)
    return urls


def parse_url(urls):
    # 因为只拿前两页做测试，所以range设置到50
    for i in range(0, 50, 1):
        res = requests.get(urls[i], headers=headers_urls)
        print(res)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'lxml')
            # 爬取电影名
            name = (soup.find('span', property="v:itemreviewed"))
            names.append(name.text)
            # print(names)

            # 爬取导演
            director = soup.find('a', rel="v:directedBy")
            directors.append(director.text)
            # print(director.text)

            # 爬取明星
            star_save = []
            for star in soup.find_all('a', rel="v:starring"):
                star_save.append(star.text)
                stars.append(star_save)
            # print(stars)

            # 爬取制片国家
            # <span class="pl">制片国家/地区:</span> 美国<br>
            # 学到的知识点：通过匹配文本内容找下个兄弟节点
            country = soup.find('span', text='制片国家/地区:').next_sibling[1:]
            countrys.append(country)
            # print(countrys)

            # 爬取影片语言
            # <span class="pl">语言:</span>
            language = soup.find('span', text='语言:').next_sibling[1:]
            languages.append(language)
            # print(language)


# print(directors)
# print(true_director)
# print(a)
if __name__ == '__main__':
    base = base_urls(base_url)
    # print(base)
    # print(len(base))
    # parse_url(base)
    # print(countrys)
    # print(directors)
    # print(languages)
    # print(names)
    # #
    # # 最后我们将数据写入到一个excel表格里
    # info = {'Filmname': names, 'Directors': directors, 'Country': countrys, 'Languages': languages}
    # pdfile = pandas.DataFrame(info)

    # pdfile.to_excel('DoubanFilm.xlsx', sheet_name="豆瓣电影")