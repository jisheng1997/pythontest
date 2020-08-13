#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : measure_time.py
@Time    : 2020/8/13 23:27
@Author  : jisheng
"""

import time
start_time = time.time()
end_time = time.time()
print("程序运行了" + str(round((end_time-start_time),1)) + '秒，也太慢了吧')