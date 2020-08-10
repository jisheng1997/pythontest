#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : list.py
@Time    : 2020/8/6 22:53
@Author  : jisheng
"""

#列表索引从0开始。列表可以进行截取、组合
#列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
#列表的数据项不需要具有相同的类型

#变量表
list1 = ['Google', 'python', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
tuple1 = ('I','love','python')

print('------------以下是列表的获取，修改，删除-------------')

print ("list1[0]: ", list1[0])
print ("list1[-2]: ", list1[-2])
print ("list2[1:5]: ", list2[1:5])
print ("list3[1:]: ", list3[1:])
#你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项
print ("第三个元素为 : ", list1[2])
list1[2] = 2001
print ("更新后的第三个元素为 : ", list1[2])
print ("原始列表 : ", list1)
del list1[3]
print ("删除第三个元素 : ", list1)

print('-----------------以下是列表脚本操作符-------------------')

#1.长度  2.组合  3.重复  4.元素是否存在于列表中
print(len(list2),list2+list3,list1*4,3 in list2)
#5.迭代
for x in list1:
    print(x,end=' ')
print('')

print('-------------------以下是嵌套列表--------------------')

list4 = [list1,list2,list3]
print("list4: ",list4)
print("list4[1]: ",list4[1])
print("list4[2][3]: ",list4[2][3])

print('-------------------以下是列表函数&方法---------------------')

#列表元素个数/返回列表元素最大值/返回列表元素最小值
print(len(list2),max(list2),min(list2))
#将元组转换为列表
print(list(tuple1))
#在列表末尾添加新的对象
list1.append('baidu')
print(list1)

