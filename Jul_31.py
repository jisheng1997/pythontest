#!/usr/bin/python3
import random
import numpy as np

def f1(arg1,arg2):
    print(arg1 + arg2)

# f1("hello",",world")
#
# f1(arg2=",world",arg1="hello")

def f2(a1,a2,a3,*tup_args,**dict_args):#*会存放所有未命名的变量参数，**会存放所有命名的变量参数
    print(a1+a2+a3)
    print(*tup_args)
    print(**dict_args)

# f2("ni","hao","zaijian")
# f2("ni","hao","zaijian","wo","xi","huan","ni")

# a = 3
# list1 = [1,2,3,4,5]
# def f3(b,list1):
#     b += 1
#     list1[0] = list1[4]
#     print(b);print(list1)

# f3(a,list1);print(a);print(list1)

def f4(x):
    x += 1
    return x

# print(f4(114513))

def choujiang():
    return random.choice(["恭喜，您中了特等奖","恭喜，您中了一等奖",
                          "恭喜，您中了二等奖","恭喜，您中了三等奖",
                          "参与奖","再来一次","谢谢","下次再来"])
# print(choujiang())

def rabbit(n):
    if n == 0 or n == 1:
        return 1
    else:
        return rabbit(n - 1) + rabbit(n - 2) #函数调用呈指数增加（1->2 2->4)
print(rabbit(20))

def fab(num):
    a = 0;b = 1
    for n in range(num):
        yield b
        a,b = b , a + b
# for n in fab(10):
#     print(n)

def f():
    print('start')
    a = yield 1
    print(a)
    print('middle....')
    b = yield 2  # 2这个值只是迭代值，调用next时候返回的值
    print(b)
    print('next')
    c = yield 3
    print(c)

# a = f()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(a.send('msg'))
# print(a.send('msg1'))
# print(next(a))

def f6():
    value1 = yield 1
    print(value1)
    value2 = yield 9
gen = f6()
# print(next(gen))
# print(gen.send(8))

def arithmetic(num1,num2,operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
# print(arithmetic(int(input("请输入第一个数字：")),
#                  int(input("请输入第二个数字：")),
#                  input("请输入运算符：")))

# factorial
def fac(num):
    result = 1
    for n in range(1,num + 1):
        result *= n
    return result
# print(fac(10))

def square(x):
    return x*x
# print(squ(5))

# list = lambda x : [i for i in x if i % 2 ==0]
# print(list([1,2,3,4,5,6,7,8,9,0,12]))









        



