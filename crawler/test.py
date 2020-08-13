#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2020/8/10 13:13
@Author  : jisheng
"""
import requests
import os

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.baidu.com/',
    'Connection': 'keep-alive',
}

#百度图片搜索关键字返回前十张
# picname = input("请输入想要搜索的图片： ")
# url="https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=0%2C0&fp=detail&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=0&lpn=0&st=-1&word={0}&z=0&ic=&hd=&latest=&copyright=&s=undefined&se=&tab=0&width=&height=&face=undefined&istype=2&qc=&nc=&fr=&simics=&srctype=&bdtype=0&rpstart=0&rpnum=0&cs=2118014413%2C2628016235&catename=&force=undefined&cardserver=&tabname=&pn=0&rn=30&gsm=2&1597298804074=".format(picname)
# res0 = requests.get(url,headers=headers)
# res0.encoding = res0.apparent_encoding
# res0 = res0.json()  # dict
# pic_list = []
# now = os.getcwd()
# now = os.path.join(now, "../pic")
# if not os.path.exists(now):
#     os.mkdir(now)
# os.chdir(now)
# for i in range(10):
#     res = requests.get(res0["data"][i]["middleURL"],headers = headers)
#     file_name = str(i) + '.jpg'
#     with open(file_name, 'wb') as f:
#         f.write(res.content)

keyword = "百合"
url = "https://pixivic.com/keywords?tag={0}&illustType=illust&VNK=b1091747".format(keyword)
res = requests.get(url,headers = headers)
html = res.text
soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())
print(soup.link.name)

