#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : pixiv.py
@Time    : 2020/8/10 13:49
@Author  : jisheng
"""
import requests
import re
import os
import time
import threading

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.163 Safari/537.36",
    "Referer": "https://www.pixiv.net/tags/good/artworks?s_mode=s_tag"}  # 注意,他的referfer在pixiv,这东西搞了我好久


class Crowling:

    def __init__(self):
        self.keyword = '湊阿库娅'  # 搜索人物
        self.page = ''  # 打印页数
        self.filename = ''  # 保存的文件夹
        self.path = ''  # 保存地址
        self.lasted_path = ''  # 测试后的保存地址
        self.number = []  # 图片序号
        self.lasted = []  # 再次测试
        self.list = []  # 原图地址
        self.x = 0  # 图片序号
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.163 Safari/537.36",
            "Referer": "https://www.pixiv.net/tags/good/artworks?s_mode=s_tag"}  # 请求头

    # 将原图地址保存到self.list
    def insert(self):
        for new_page in range(1, int(self.page) + 1):
            url = 'https://api.pixivic.com/illustrations?illustType=illust&searchType=original&maxSanityLevel=6&page=' \
                  + str(new_page) + '&keyword=' + self.keyword + '&pageSize=30'
            html = requests.get(url).text
            all_url = re.findall("\"original\":.*?jpg", html)
            try:
                for i in all_url:
                    a = i.replace('"original":"', '')
                    a = a.replace(a, str(a))
                    self.list.append(a)

            except Exception as e:
                print(e)

    # 将slef.list的网址拿出来下载
    def crow(self, url):
        self.x = 0
        try:
            now_url = requests.get(url, headers=headers).content
            url_code = requests.get(url, headers=headers).status_code
            self.path = self.filename + str(self.x) + '.jpg'
            if url_code == 200:
                with open(self.path, 'wb') as p:
                    p.write(now_url)
            else:
                self.lasted.append(url)
                self.number.append(self.x)
            self.x += 1
            print('下载成功')

        except Exception as e:
            print(e)

    # 有时候访问过快，导致图片下不了，于是后面在此下载
    def test_lasted(self, text_url, num):
        if self.lasted:
            try:
                lasted_url = requests.get(text_url, headers=headers, timeout=2).content
                lasted_code = requests.get(text_url, headers=headers, timeout=2).status_code
                if lasted_code == 200:
                    self.lasted_path = self.filename + str(num) + '.jpg'
                    with open(self.lasted_path, 'wb') as p:
                        p.write(lasted_url)
                    print('下载成功')
                    self.lasted.remove(text_url)
                else:
                    print('下载失败')
                    self.lasted.remove(text_url)
            except Exception as e:
                print(e)

    # 调用之前的方法
    def __call__(self):
        print('+++++++++++++')
        print('+  P        +')
        print('+  I   D    +')
        print('+  X   O    +')
        print('+      w    +')
        print('+      N    +')
        print('+++++++++++++')
        main_people = input('你想打印什么：')
        page_number = input('你想打印几页：')
        self.keyword = main_people
        self.page = page_number
        # 创建文件夹
        if not os.path.exists(main_people):
            os.mkdir(main_people)
        self.filename = str(main_people) + '//'
        tlist = []
        llsit = []
        self.insert()
        a = time.time()
        # 多线程并发，要不然慢出天际
        for i in self.list:
            t1 = threading.Thread(target=self.crow, args=(i,))
            t1.start()
            tlist.append(t1)

        for i in tlist:
            i.join()

        for i in range(len(self.lasted)):
            t2 = threading.Thread(target=self.test_lasted, args=(self.lasted[i], self.number[i]))
            t2.start()
            llsit.append(t2)

        for i in llsit:
            i.join()

        print('共用时：' + str(time.time() - a))


# 调用
crowing = Crowling()
crowing()