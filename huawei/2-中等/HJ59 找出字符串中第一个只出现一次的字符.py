"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/1 11:00
@File        : HJ59 找出字符串中第一个只出现一次的字符.py
"""


# 描述
# 找出字符串中第一个只出现一次的字符
# 数据范围：输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000
# 输入描述：
# 输入一个非空字符串
#
# 输出描述：
# 输出第一个只出现一次的字符，如果不存在输出-1

def findOneStr(s):
    """
    HJ59 找出字符串中第一个只出现一次的字符
    :param s:
    :return:
    """

    t = ''
    record = {}
    for a in s:
        record[a] = record.get(a,0) + 1

    for k in record:
        # print(record[k])
        if record[k] == 1:
            t = k
            break

    if t == '':
        print('-1')
    else:
        print(t)

findOneStr('asdfasdfo')



