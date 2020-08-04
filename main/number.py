#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : number.py
@Time    : 2020/8/4 14:14
@Author  : jisheng
"""

import math
import cmath

#变量表
var1 = -1
var2 = 4.4
var3 = 3
list1 = [1,2,3,4,5,6]

#返回数字的绝对值 fabs(x)为绝对值的浮点数
print(abs(var1))
#返回数字的上入整数
print(math.ceil(var2))
#返回数字的下舍整数
print(math.floor(var2))
#如math.log(math.e)返回1.0,math.log(100,10)返回2.0
print(math.log(100,10),end=" ")
print(math.log(math.e))
#返回以10为基数的x的对数，如math.log10(100)返回 2.0
print(math.log10(100))
#返回给定参数的最大最小值，参数可以为序列。
print(max(1,2,3,4,10),end=" ")
print(max(list1),end=" ")
print(min(3,4,10),end=" ")
print(min(list1))
#返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
print(math.modf(114.514))
#x**y 运算后的值。
print(pow(var3,var1))
#返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print(round(11.4514,2))
#返回数字x的平方根
print(math.sqrt(16))




