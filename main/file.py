#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : file.py
@Time    : 2020/8/11 10:11
@Author  : jisheng
"""
import os
#file文件夹路径  E:\PythonProjects\test\file
path = 'E://PythonProjects//test//file//'
filename = 'hellopython.txt'
#打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，
#即原有内容会被删除。如果该文件不存在，创建新文件。
file = open(path + filename,'w+')
file.write('hello,i m jisheng')

str = file.readline()
print(str)
file.close()