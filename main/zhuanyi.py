#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : zhuanyi.py
@Time    : 2020/8/13 14:28
@Author  : jisheng
"""

import re
str = 'abcad?cdadca?ca*cdgaajcakca7caAcada_cCadavaCDavacavavc'

str2 = 'a2ba324sf24sdgf2'

str3 = '''313156566@qq.com
    hjasd23@163.com
    http://www.abc.com.cn
    https://www.sae.com
    ftp://www.nnn.org
    ftps://www.jksad.net'''

# pattern1 = re.compile("[a-zA-Z]+://[a-z][A-Z]+\.[a-zA-Z0-9]{1,100}(\.[a-zA-Z]+)")
# for i in re.finditer(pattern1,str3):
#     print(i.group(0))
#
str4 ='你好'
pattern2 = re.compile("^[\u4e00-\u9fa5]+$")
print(re.match(pattern2,str4))
if re.match(pattern2,str4):
    print("字符全是中文")
else:print("字符不全是中文")

#贪婪模式
example = "<div>test1</div><div>test2</div>"

# greedPattern = re.compile("<div>.*</div>")
# notGreedPattern = re.compile("<div>.*?</div>")
# greedResult = greedPattern.search(example)
# notGreedResult = notGreedPattern.search(example)
# print("greedResult = %s" % greedResult.group())
# print("notGreedResult = %s" % notGreedResult.group())

pattern3 = re.compile('[a-z]+')
str4 = 'mmmla2nnnn2b37g8d'
print(list(filter(None,re.split(pattern3,str4))))


# 3.写出一个正则表达式，过滤网页上的所有JS脚本(即把scrīpt标记及其内容都去掉)
script="以下内容不显示：<script language='javascript'>alert('cc');" \
       "</script><p>fdgdfgdgsdg</p><script>alert('dd');</script>"

pattern4 = re.compile("<script.*?>.*?</script>",re.S)
print(re.sub(pattern4,"",script))

# 4. 通过正则表达式把img标签中的src路径匹配出来
str5 ='''
    <img name="photo" src="../public/img/img1.png" />
    <img name='news' src='xxx.jpg' title='news' /> 
    '''

# 5.将任意的电话号码13811119999变成138****9999
str6 = "13812349999"
pattern5 = re.compile("([0-9]{3})[0-9]{4}([0-9]{4})")
print(re.sub(pattern5,'\\1'+'****'+'\\2',str6))
