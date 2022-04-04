"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/28 21:38
@File        : HJ96 表示数字.py
"""


# HJ96 表示数字

# 描述
# 将一个字符中所有的整数前后加上符号“*”，其他字符保持不变。连续的数字视为一个整数。
# 数据范围：字符串长度满足 1 \le n \le 100 \1≤n≤100
# 输入描述：输入一个字符串
# 输出描述：字符中所有出现的数字前后加上符号“*”，其他字符保持不变


def convertStr(str):

    ss = ''
    pre_ = ''
    for s in str:
        if s.isdigit():
            if not pre_.isdigit():
                ss += '*'
        else:
            if pre_.isdigit():
                ss += '*'
        ss += s
        pre_ = s

    if s.isdigit():
            ss += '*'
    print(ss)


convertStr('ddsds2e243df321')
