#!/usr/bin/python3

str = 'Runoob'
str2 = "Hello"
str3 = "Python"

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

print('------------------------------')

print("a + b 输出结果：", str2 + str3)
print("a * 2 输出结果：", str2 * 2)
print("a[1] 输出结果：", str2[1])
print("a[1:4] 输出结果：", str2[1:4])

if "H" in str2:
    print("H 在变量 str2 中")
else:
    print("H 不在变量 str2中")

if "M" not in str2:
    print("M 不在变量 str2 中")
else:
    print("M 在变量 str2 中")

print('------------------------------')


