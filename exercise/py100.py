# -- encoding:utf-8 --
# https://www.runoob.com/python/python-100-examples.html
# 需求：
# 在这个网站中 得到所有的100个案例的题目和代码：
import requests
from lxml import etree
import time
#https://www.runoob.com/python/python-exercise-example1.html
#https://www.runoob.com/python/python-exercise-example3.html
#https://www.runoob.com/python/python-exercise-example7.html
#https://www.runoob.com/python/python-exercise-example31.html

for i in range(1,101):
    url = 'https://www.runoob.com/python/python-exercise-example%d.html'%i
    r = requests.get(url).text
    html = etree.HTML(r)
    # print(html)
    #得到题目和代码
    #题目：
    title = html.xpath("//div[@id='content']/p[2]/text()")[0]
    # print(title)
    code = html.xpath("string(//div[@class='hl-main'])")
    # print(code)
    time.sleep(1)
    with open('py100.txt','a',encoding='utf8') as file:
        file.write(title+code+'\n'+'='*50+'\n')
    print('现在下载到第%d个实例了'%i)
