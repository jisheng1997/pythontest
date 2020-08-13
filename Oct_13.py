#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : Oct_13.py
@Time    : 2020/8/13 10:12
@Author  : jisheng
"""
# json.dumps()用于将dict类型的数据转成str，
# 因为如果直接将dict类型的数据写入json文件中会发生报错，
# 因此在将数据写入时需要用到该函数。
import requests
import re

#黄色图片地址
headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.baidu.com/',
            'Connection': 'keep-alive',
        }
proxies = {
    'https':'https://114.239.126.231:4216'
}
url1 = "https://www.taobao.com"
url2 = "https://httpbin.org/"
url3 = "https://github.com/timeline.json"
url4 = "http://ibeifeng.com"
url5 = "https://www.pixiv.net"
url6 = "https://isure.stream.qqmusic.qq.com/C400004g1plV0KiHJC.m4a?guid=5887483477&vkey=57D27292C0E8D32FEFA99B2C3C99530228405C7C2A1C0500A3F9EDBCC0A0D4F93B453BD8A455CF503D9CA7E4B885BDA6C72F70F227D125B3&uin=6072&fromtag=66"
gif_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1597295180281&di=cf676713e75317824f7ba891a73d0227&imgtype=0&src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F201908%2F08%2F20190808003013_mn5Fm.thumb.700_0.gif"
# res1 = requests.get(gif_url,stream = True)
# res2 = requests.get(url6,headers = headers,stream = True)
# with open('file//xiaohuangya.jpg','wb') as file:
#     file.write(res1.raw.read())

# with open("file//mea.gif",'wb') as file:
#     file.write(res2.content)

# with open('file/1.mp4','wb') as file:
#     for i in res2.iter_content(1024*10):
#         file.write(i)

# from requests.exceptions import ConnectTimeout,ConnectionError,RequestException
# try:
#     res3 = requests.get(url5).text
#     print(res3)
# except ConnectTimeout:
#     print("超时辣，快检查一下网络设置")
# except ConnectionError:
#     print("连接错误辣，你行不行啊")
# except RequestException as e:
#     print("出现了其他错误，你好菜哦")

# res4 = requests.get("http://httpbin.org/get",proxies = proxies,headers = headers).text
# print(res4)



