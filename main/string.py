#!/usr/bin/python3

str2 = 'Hello'
str3 = 'Python'

print('------------以下为字符串操作--------------')

# 连接字符串
print('str2 + str3 输出结果：', str2 + str3)
print('str2 + world 输出结果：',str2 + ',world')
# 重复输出字符串
print('str2 * 2 输出结果：', str2 * 2)
# 输出字符串第一个字符
print('str2[0] 输出结果：', str2[0])
# 输出第一个到倒数第二个的所有字符
print('str2[0:-1] 输出结果：',str2[0:-1])
# 输出从第三个开始到第五个的字符
print('str2[2:5] 输出结果：',str2[2:5])
# 输出从第三个开始后的所有字符
print('str2[2:] 输出结果：',str2[2:])
# 在字符串前面添加一个 r (可以大小写)，表示原始字符串，不会发生转义
print(r'hello\nrunoob')
# 使用反斜杠(\)+n转义特殊字符
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
# 将字符串的第一个字符转换为大写


