#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : string.py
@Time    : 2020/8/6 22:53
@Author  : jisheng
"""
#
str1 = ''
str2 = 'hello'
str3 = 'python'
str4 = 'hello\tpython\t\nI\tlove\tyou'
zhongwen = '你好'
shuzi = '123654'
shuzizifu = '\u00BD'
xiaoxie = 'xiaoxie'
daxie = 'DAXIE'
daxiaoxie = 'DaXiaoXie'
kongbai = '    '
shijinzhi = 'python 1997'
title = 'This Is A Title'
title2 = 'this is a title2'
list1 = ['我','今年','24岁',',','是','学生']

print('------------以下为字符串操作--------------')

#连接字符串
print('str2 + str3 输出结果：', str2 + str3)
print('str2 + world 输出结果：',str2 + ',world')
#重复输出字符串
print('str2 * 2 输出结果：', str2 * 2)
#输出字符串第一个字符
print('str2[0] 输出结果：', str2[0])
#输出第一个到倒数第二个的所有字符
print('str2[0:-1] 输出结果：',str2[0:-1])
#输出从第三个开始到第五个的字符
print('str2[2:5] 输出结果：',str2[2:5])
#输出从第三个开始后的所有字符
print('str2[2:] 输出结果：',str2[2:])
#在字符串前面添加一个 r (可以大小写)，表示原始字符串，不会发生转义
print(r'hello\nrunoob')
#使用反斜杠(\)+n转义特殊字符
print('hello\nrunoob')

#in和not in判断字符是否在字符串中
if "H" in str2:
    print("H 在变量 str2 中")
else:
    print("H 不在变量 str2中")

if "M" not in str2:
    print("M 不在变量 str2 中")
else:
    print("M 在变量 str2 中")

print('------------以下是字符串函数-------------')
#1.将字符串的第一个字符转换为大写
print(str2.capitalize())
#2.返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
print(str2.center(len(str2)+10, '*'))
#3.返回 str 在 string 里面出现的次数
print(str2.count('l',0,len(str2)))
#4.把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
print(str4.expandtabs(tabsize=15))
#5.检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。
#6.检查字符串是否以 obj 结束，如果是，返回 True,否则返回 False.
print(str2.startswith('H'),str2.endswith('o'))
#7.检测str是否包含在字符串中，如果包含返回开始的索引值，否则返回-1
#跟find()方法一样，只不过如果str不在字符串中会报一个异常。
#类似于 find()函数，不过是从右边开始查找.
#类似于 index()，不过是从右边开始.
print(str2.find('ll'),str2.index('lo'),str2.rfind('e'),str2.rindex('h'))
#10.如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False
#11.如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
#12.如果字符串只包含数字则返回 True 否则返回 False.
#13.如果字符串中只包含数字字符，则返回 True，否则返回 False
#14.如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
#15.如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
#16.如果字符串中只包含空白，则返回 True，否则返回 False.
#17.如果字符串是标题化的(见 title())则返回 True，否则返回 False
#18.检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
print(str2.isalnum(),zhongwen.isalpha(),shuzi.isdigit(),shuzizifu.isnumeric(),
      xiaoxie.islower(),daxie.isupper(),kongbai.isspace(),title.istitle(),shijinzhi.isdecimal())
#18.以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
print(str1.join(list1))
#19.返回字符串长度
print(len(str4))
#20.返回一个原字符串左对齐或右对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
print(str2.ljust(20,'*'),str2.rjust(20,'*'))
#22.转换字符串中所有大写字符为小写/所有小写字符为大写/大写转换为小写，小写转换为大写
print(daxie.lower(),xiaoxie.upper(),daxiaoxie.swapcase())
#25.截掉字符串左边和右边的空格或指定字符。
#在字符串上执行 lstrip()和 rstrip()
print(str2.lstrip('he'),str2.rstrip('lo'),str2.strip('hlo'))
#28.创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
#根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
str_trantab = str.maketrans(str3,shuzi)
print(str4.translate(str_trantab))
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(b'python'.translate(bytes_tabtrans, b'o'))
#29.返回字符串 str 中最大的字母和最小的字母。
print(max(str2),min(str2))
#31.把将字符串中的str1替换成 str2,如果max指定，则替换不超过max次。
print(str2.replace('e','a',1))
#33.以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
print(title.split(' ',2))
#34.按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，
#如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
print(str4.splitlines(keepends=True))
#35.返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写
print(title2.title())
#36.返回长度为 width 的字符串，原字符串右对齐，前面填充0
print(str2.zfill(20))