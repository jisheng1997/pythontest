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
import re

#目标：https://www.cnblogs.com/ 对该网站的blog进行爬取数据

def get_urls(url,headers):
    blogs_urls = []
    #循环得到十页的所有blog的链接
    for i in range(1,3):
        blogslist_url = url.format(i)
        res = requests.get(blogslist_url, headers=headers)
        if res.status_code == 200:
            html = etree.HTML(res.text)
            # 获取帖子的链接已列表的形式保存
            result = html.xpath("//div[@class='post-item-text']/a/@href")
            for j in result:
                blogs_urls.append(j)
        else:return "发生了错误，状态码：" + str(res.status_code)
        time.sleep(1)
    return blogs_urls

def get_data(urls,headers):
    blogs = []
    i = 1
    for url in urls:
        start_time = time.time()
        res = requests.get(url, headers=headers)
        print(('现在正在下载第{}篇博客').format(i),end="")
        if res.status_code == 200:
            blog = {}
            #对<span class="math inline">\(N\)</span>进行处理
            pattern = re.compile('<span,*?class="math.*?inline">(\()(.*?)(\))',re.S)
            html = etree.HTML(re.sub(pattern,'\\2' , res.text))
            # 获取贴子的标题并对标题进行处理
            title = html.xpath("//a[@id='cb_post_title_url']/span/text()")[0]
            # 获取贴子的正文
            article = html.xpath("string(//div[@id='cnblogs_post_body'])")
            # 用字典存储数据
            blog['title'] = title
            blog['article'] = article
            blogs.append(blog)
            time.sleep(0.2)
        else:return "发生了错误，状态码：" + str(res.status_code)
        i += 1
        end_time = time.time()
        print(",耗时" + str(round((end_time - start_time), 1)) + "秒")
    return blogs

def writefile(data):
    # 处理数据写进文件
    i = 1
    print("正在写入文件")
    with open('cnblogs.txt','w+',encoding='utf8') as file:
        for blog in data:
            file.write('*'*50+'第'+str(i)+'篇博客'+'*'*50+'\n'+blog['title'] + blog['article'] +'\n')
            i += 1
    print("文件写入完毕")

def main():
    start_time = time.time()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    base_url = "https://www.cnblogs.com/#p{}"
    headers_next = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','referer' : 'https://www.cnblogs.com/'}
    temp = get_data(get_urls(base_url, headers), headers_next)
    writefile(temp)
    end_time = time.time()
    print("程序总共耗时" + str(round((end_time - start_time), 1)) + "秒")

if __name__ == '__main__':
    main()






